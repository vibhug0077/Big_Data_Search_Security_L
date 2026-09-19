"""Execute deterministic control-evidence and audit-event examples."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent.parent
DATA = HERE / "data/controls_audit_data.json"
records = json.loads(DATA.read_text(encoding="utf-8"))

print("CHAPTER 06 CONTROLS AND AUDIT")
print("Working directory: /workspace/labs/chapter_06_controls_and_audit")
print("Data file: data/controls_audit_data.json")

print("\n=== Example 1: control matrix evidence coverage ===")
locally_tested_controls = {"resource-specific role", "access audit review"}
for row in records["control_matrix"]:
    if row["control"] in locally_tested_controls:
        status = "tested in this local script"
    elif row["evidence"]:
        status = "untested; evidence reference only"
    else:
        status = "untested; evidence missing"
    print(row["risk"], row["control"], row["type"], status)

print("\n=== Example 2: audit-event normalization ===")
raw_events = records["audit_events"]
safe_keys = records["safe_event_fields"]
safe_events = [{key: event[key] for key in safe_keys} for event in raw_events]
print("safe events:", safe_events)
assert all("body" not in event for event in safe_events)
assert all(event["outcome"] in {"allow", "deny"} for event in safe_events)
print("redaction control: PASS")

print("\n=== Example 3: authorization positive and negative tests ===")
policy = {tuple(item) for item in records["policy"]}
policy_failures = []
for case in records["policy_tests"]:
    role, action, resource, expected = case
    actual = (role, action, resource) in policy
    result = "PASS" if actual == expected else "FAIL"
    print(result, role, action, resource, "actual=", actual)
    if actual != expected:
        policy_failures.append(case)
assert not policy_failures

print("\n=== Example 4: intentionally insecure control failure ===")
insecure_policy = policy | {("reader", "SELECT", "private_notes")}
role, action, resource, expected = records["insecure_negative_test"]
actual = (role, action, resource) in insecure_policy
print("FAILED CONTROL DETECTED", role, action, resource, "actual=", actual, "expected=", expected)
assert actual is True and expected is False

print("\n=== Evidence classification ===")
print("Configured control: authorization policy, audit-event field allow-list, and control-matrix records")
print("Tested control: audit redaction and secure policy positive/negative tests; PASS")
print("Failed control: intentionally insecure policy allowed reader access to private_notes; DETECTED")
print("Untested control: payload-size limit, restore rehearsal, TLS/certificate validation, and distributed enforcement")
print("Residual risk: local policy tests do not prove gateway, search, export, backup, or direct-storage enforcement")
print("\nCHAPTER 06 CONTROLS AND AUDIT SMOKE TEST PASSED")
