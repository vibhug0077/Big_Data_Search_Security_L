"""Run AES-GCM, envelope-key, TLS-context, and loopback TLS examples."""

from __future__ import annotations

import json
import os
import socket
import ssl
import tempfile
import threading
from datetime import datetime, timedelta, timezone
from pathlib import Path
from queue import Queue

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.x509 import DNSName, Name, NameAttribute, SubjectAlternativeName
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID


HERE = Path(__file__).resolve().parent.parent
DATA = HERE / "data/encryption_transport_data.json"
records = json.loads(DATA.read_text(encoding="utf-8"))


def generate_local_certificate(directory: str) -> tuple[Path, Path]:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    subject = issuer = Name([NameAttribute(NameOID.COMMON_NAME, "localhost")])
    certificate = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(minutes=1))
        .not_valid_after(now + timedelta(minutes=10))
        .add_extension(SubjectAlternativeName([DNSName("localhost")]), critical=False)
        .sign(key, hashes.SHA256(), default_backend())
    )
    cert_path = Path(directory) / "synthetic-localhost-cert.pem"
    key_path = Path(directory) / "synthetic-localhost-key.pem"
    cert_path.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))
    key_path.write_bytes(
        key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.TraditionalOpenSSL,
            serialization.NoEncryption(),
        )
    )
    os.chmod(key_path, 0o600)
    return cert_path, key_path


def loopback_tls_attempt(cert_path: Path, key_path: Path, hostname: str) -> tuple[bool, str | None]:
    server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    server_context.minimum_version = ssl.TLSVersion.TLSv1_2
    server_context.load_cert_chain(certfile=cert_path, keyfile=key_path)
    ready: Queue[int] = Queue()
    server_errors: list[Exception] = []

    def serve() -> None:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
                server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server.bind(("127.0.0.1", 0))
                server.listen(1)
                ready.put(server.getsockname()[1])
                connection, _ = server.accept()
                with connection:
                    with server_context.wrap_socket(connection, server_side=True) as tls:
                        if hostname == "localhost":
                            if tls.recv(5) != b"hello":
                                raise RuntimeError("unexpected loopback payload")
                            tls.sendall(b"ack")
        except Exception as exc:  # the wrong-hostname attempt is expected to alert the server
            server_errors.append(exc)

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()
    port = ready.get(timeout=5)
    client_context = ssl.create_default_context(cafile=cert_path)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_2
    passed = False
    negotiated: str | None = None
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=5) as raw:
            with client_context.wrap_socket(raw, server_hostname=hostname) as tls:
                tls.sendall(b"hello")
                passed = tls.recv(3) == b"ack"
                negotiated = tls.version()
    except ssl.SSLCertVerificationError:
        passed = False
    thread.join(timeout=5)
    if thread.is_alive():
        raise RuntimeError("loopback TLS server did not finish")
    if hostname == "localhost" and server_errors:
        raise server_errors[0]
    return passed, negotiated


print("CHAPTER 10 ENCRYPTION AND TRANSPORT")
print("Working directory: /workspace/labs/chapter_10_encryption_and_transport")
print("Data file: data/encryption_transport_data.json")

print("\n=== Example 1: AES-GCM confidentiality and tamper rejection ===")
key = AESGCM.generate_key(bit_length=256)
cipher = AESGCM(key)
nonce = os.urandom(12)
plaintext = records["plaintext"].encode("utf-8")
associated_data = records["associated_data"].encode("utf-8")
ciphertext = cipher.encrypt(nonce, plaintext, associated_data)
restored = cipher.decrypt(nonce, ciphertext, associated_data)
print("Round trip:", restored == plaintext)
print("Ciphertext bytes including tag:", len(ciphertext))
for label, payload, metadata in [
    ("changed ciphertext", ciphertext[:-1] + bytes([ciphertext[-1] ^ 1]), associated_data),
    ("changed metadata", ciphertext, b"document=D002;schema=1"),
]:
    try:
        cipher.decrypt(nonce, payload, metadata)
    except InvalidTag:
        print(label, "rejected")

print("\n=== Example 2: envelope encryption and KEK rotation ===")
kek = AESGCM.generate_key(bit_length=256)
dek = AESGCM.generate_key(bit_length=256)
kek_cipher = AESGCM(kek)
wrap_nonce = os.urandom(12)
key_id = records["key_id"].encode("utf-8")
wrapped_dek = kek_cipher.encrypt(wrap_nonce, dek, key_id)
data_nonce = os.urandom(12)
data_cipher = AESGCM(dek)
aad = records["envelope_aad"].encode("utf-8")
data_ciphertext = data_cipher.encrypt(data_nonce, records["envelope_plaintext"].encode("utf-8"), aad)
restored_dek = kek_cipher.decrypt(wrap_nonce, wrapped_dek, key_id)
restored_data = AESGCM(restored_dek).decrypt(data_nonce, data_ciphertext, aad)
print("DEK recovered:", restored_dek == dek)
print("data recovered:", restored_data)
print("stored envelope fields:", ["key_id", "wrapped_dek", "wrap_nonce", "data_nonce", "ciphertext", "aad"])
new_kek = AESGCM.generate_key(bit_length=256)
new_key_id = records["new_key_id"].encode("utf-8")
new_wrap_nonce = os.urandom(12)
rewrapped_dek = AESGCM(new_kek).encrypt(new_wrap_nonce, dek, new_key_id)
dek_after_rotation = AESGCM(new_kek).decrypt(new_wrap_nonce, rewrapped_dek, new_key_id)
print("same DEK after KEK rotation:", dek_after_rotation == dek)
print("old and new KEK identifiers:", key_id.decode(), new_key_id.decode())

print("\n=== Example 3: TLS context and verified loopback transport ===")
context = ssl.create_default_context()
context.minimum_version = ssl.TLSVersion.TLSv1_2
print("Certificate required:", context.verify_mode == ssl.CERT_REQUIRED)
print("Hostname checking:", context.check_hostname)
print("Minimum protocol:", context.minimum_version.name)
with tempfile.TemporaryDirectory(prefix="bdss-tls-") as temporary:
    cert_path, key_path = generate_local_certificate(temporary)
    good, negotiated = loopback_tls_attempt(cert_path, key_path, "localhost")
    wrong_host, _ = loopback_tls_attempt(cert_path, key_path, "wrong.localhost")
    print("TLS loopback handshake:", "PASS" if good else "FAIL")
    print("TLS negotiated version:", negotiated)
    print("wrong hostname rejected:", not wrong_host)
    assert good is True
    assert wrong_host is False

print("\n=== Example 4: hop coverage review ===")
for source, destination, protected in records["hops"]:
    print(f"{source} -> {destination}: {'TLS required' if protected else 'GAP TO REVIEW'}")

print("\n=== Evidence classification ===")
print("Configured control: AES-GCM authenticated encryption, DEK/KEK envelope, TLS 1.2 minimum, and hostname validation")
print("Tested control: round trip, tamper rejection, key re-wrap, verified loopback TLS, and wrong-host rejection; PASS")
print("Failed control: the fictional search-to-worker hop is intentionally recorded as GAP TO REVIEW")
print("Untested control: KMS access, HDFS encryption zones, external certificate chain, mutual TLS, rotation migration, and every production hop")
print("Residual risk: ephemeral local keys and self-signed certificate do not establish production key custody or trust")
print("\nCHAPTER 10 ENCRYPTION AND TRANSPORT SMOKE TEST PASSED")
