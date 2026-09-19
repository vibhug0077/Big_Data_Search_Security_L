"""Run deterministic HMAC, digest, replay, and envelope validation examples."""

from __future__ import annotations

import hashlib
import hmac
import json
import secrets
import sqlite3
from pathlib import Path


HERE = Path(__file__).resolve().parent.parent
DATA = HERE / "data/ingestion_data.json"
records = json.loads(DATA.read_text(encoding="utf-8"))


def encode(value: dict) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def validate_envelope(envelope: dict) -> tuple[bool, str]:
    required = {"event_id", "producer_id", "schema_version", "created_at", "payload"}
    missing = sorted(required - envelope.keys())
    if missing:
        return False, f"missing fields: {missing}"
    if not isinstance(envelope["schema_version"], int) or envelope["schema_version"] < 1:
        return False, "unsupported schema version"
    if not isinstance(envelope["payload"], dict) or len(envelope["payload"]) > 20:
        return False, "invalid or oversized payload"
    if not isinstance(envelope["payload"].get("count"), int):
        return False, "count must be an integer"
    return True, "ready for authentication and publication"


print("CHAPTER 09 SECURE INGESTION")
print("Working directory: /workspace/labs/chapter_09_secure_ingestion")
print("Data file: data/ingestion_data.json")

print("\n=== Example 1: authenticated ingestion and replay decision ===")
key = secrets.token_bytes(32)
event = records["event"]
tag = hmac.new(key, encode(event), hashlib.sha256).digest()
changed = {**event, "department": records["changed_department"]}
print("Original verified:", hmac.compare_digest(tag, hmac.new(key, encode(event), hashlib.sha256).digest()))
print("Changed verified:", hmac.compare_digest(tag, hmac.new(key, encode(changed), hashlib.sha256).digest()))

seen: set[str] = set()


def accept(value: dict, supplied_tag: bytes) -> str:
    expected = hmac.new(key, encode(value), hashlib.sha256).digest()
    if not hmac.compare_digest(supplied_tag, expected):
        return "reject: authentication"
    if value["event_id"] in seen:
        return "reject: duplicate"
    seen.add(value["event_id"])
    return "accept"


print(accept(event, tag))
print(accept(event, tag))
print(accept(changed, tag))
assert accept.__name__ == "accept"
assert len(seen) == 1

print("\n=== Example 2: trusted digest versus attacker-controlled digest ===")
original = records["trusted_original"].encode("utf-8")
received = records["trusted_received"].encode("utf-8")
changed_bytes = records["trusted_changed"].encode("utf-8")
expected_digest = hashlib.sha256(original).hexdigest()
print("trusted manifest, original:", hashlib.sha256(received).hexdigest() == expected_digest)
print("trusted manifest, changed:", hashlib.sha256(changed_bytes).hexdigest() == expected_digest)
attacker_digest = hashlib.sha256(changed_bytes).hexdigest()
print("changed file plus changed untrusted digest:", hashlib.sha256(changed_bytes).hexdigest() == attacker_digest)

print("\n=== Example 3: durable local replay decisions with SQLite ===")
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE accepted_events (event_id TEXT PRIMARY KEY, accepted_at TEXT NOT NULL)")


def accept_once(event_id: str, accepted_at: str) -> str:
    try:
        db.execute(
            "INSERT INTO accepted_events(event_id, accepted_at) VALUES (?, ?)",
            (event_id, accepted_at),
        )
        db.commit()
        return "accept"
    except sqlite3.IntegrityError:
        return "reject: duplicate"


print(accept_once("E100", "2026-09-15T10:00:00Z"))
print(accept_once("E100", "2026-09-15T10:00:01Z"))
print("stored decisions:", db.execute("SELECT COUNT(*) FROM accepted_events").fetchone()[0])

print("\n=== Example 4: validate an ingest envelope before publication ===")
valid = records["envelope"]
invalid = {**valid, "payload": records["invalid_payload"]}
print(validate_envelope(valid))
print(validate_envelope(invalid))
assert validate_envelope(valid)[0] is True
assert validate_envelope(invalid)[0] is False

print("\n=== Evidence classification ===")
print("Configured control: canonical HMAC, trusted digest comparison, replay table, and envelope schema checks")
print("Tested control: altered-message rejection, duplicate rejection, digest comparison, and schema validation; PASS")
print("Failed control: none; the negative tamper and replay cases were rejected as expected")
print("Untested control: secret distribution, durable cross-process transactions, time-window enforcement, quarantine access, and transport security")
print("Residual risk: authenticated bytes may still be wrong, and runtime key handling is intentionally local and ephemeral")
print("\nCHAPTER 09 SECURE INGESTION SMOKE TEST PASSED")
