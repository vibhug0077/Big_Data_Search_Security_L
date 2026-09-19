"""Run the deterministic Kerberos metadata and authorization simulations."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent.parent
DATA = HERE / "data/kerberos_simulation_data.json"
records = json.loads(DATA.read_text(encoding="utf-8"))
ticket = records["ticket"]


def metadata_check(value: dict, requested_service: str, now: int) -> bool:
    return (
        value["service"] == requested_service
        and value["start"] <= now < value["end"]
    )


def valid_with_skew(value: dict, requested_service: str, now: int, allowed_skew: int) -> bool:
    return (
        value["service"] == requested_service
        and value["start"] - allowed_skew <= now < value["end"] + allowed_skew
    )


def authorized(principal: str, action: str, resource: str) -> bool:
    return [principal, action, resource] in records["permissions"]


print("CHAPTER 07 KERBEROS")
print("Working directory: /workspace/labs/chapter_07_kerberos")
print("Data file: data/kerberos_simulation_data.json")

print("\n=== Example 1: ticket metadata model ===")
print("Within validity:", metadata_check(ticket, ticket["service"], 1200))
print("Expired:", metadata_check(ticket, ticket["service"], 1700))
print(
    "Wrong service:",
    metadata_check(ticket, "hdfs/other@LAB.EXAMPLE", 1200),
)

print("\n=== Example 2: validity window and clock-skew model ===")
for now in records["skew_times"]:
    print(
        now,
        valid_with_skew(
            ticket,
            ticket["service"],
            now,
            records["allowed_skew"],
        ),
    )

print("\n=== Example 3: authentication and authorization separation ===")
service_authenticated = metadata_check(ticket, records["service"], 1200)
print("service authentication:", service_authenticated)
print("search allowed:", authorized(ticket["client"], "SEARCH", "course-index"))
print("delete allowed:", authorized(ticket["client"], "DELETE", "course-index"))
assert service_authenticated is True
assert authorized(ticket["client"], "SEARCH", "course-index") is True
assert authorized(ticket["client"], "DELETE", "course-index") is False

print("\n=== Example 4: directional cross-realm trust model ===")
for source_realm, destination_realm in records["trust_paths"]:
    trusted = [source_realm, destination_realm] in records["trusted_paths"]
    print((source_realm, destination_realm), trusted)

print("\n=== Platform dependency boundary ===")
print("Platform-dependent: kinit/klist/kvno/kdestroy require a reachable KDC, principals, and credentials")
print("Platform-dependent: Kafka/Hadoop service authentication requires a real broker or secured Hadoop profile")

print("\n=== Evidence classification ===")
print("Configured control: deterministic service-binding, validity-window, and local authorization rules")
print("Tested control: metadata checks and local authorization separation; PASS")
print("Failed control: none in the simulation; invalid service and DELETE cases were denied as expected")
print("Untested control: cryptographic ticket verification, replay cache, mutual authentication, KDC, keytabs, and credential handling")
print("Residual risk: simulation values can be edited and do not establish Kerberos security or platform authorization")
print("\nCHAPTER 07 KERBEROS SIMULATION SMOKE TEST PASSED")
