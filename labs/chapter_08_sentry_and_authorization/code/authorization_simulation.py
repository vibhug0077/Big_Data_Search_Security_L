"""Run deterministic RBAC, deny-by-default, and revocation simulations."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent.parent
DATA = HERE / "data/authorization_simulation_data.json"
records = json.loads(DATA.read_text(encoding="utf-8"))


def effective_privileges(user: str, groups: dict, group_roles: dict, role_privileges: dict):
    roles = sorted(
        {
            role
            for group in groups.get(user, [])
            for role in group_roles.get(group, [])
        }
    )
    privileges = sorted(
        {
            tuple(privilege)
            for role in roles
            for privilege in role_privileges.get(role, [])
        }
    )
    return roles, privileges


def allowed(user: str, action: str, resource: str, groups, group_roles, role_privileges) -> bool:
    _, privileges = effective_privileges(user, groups, group_roles, role_privileges)
    return [action, resource] in [list(item) for item in privileges]


groups = records["groups"]
group_roles = records["group_roles"]
role_privileges = records["role_privileges"]

print("CHAPTER 08 SENTRY AND AUTHORIZATION")
print("Working directory: /workspace/labs/chapter_08_sentry_and_authorization")
print("Data file: data/authorization_simulation_data.json")

print("\n=== Example 1: effective privileges ===")
for user in ["alice", "bob", "service-indexer", "unknown"]:
    print(user, effective_privileges(user, groups, group_roles, role_privileges))

print("\n=== Example 2: allowed and denied policy cases ===")
failures = []
for user, action, resource, expected in records["policy_cases"]:
    actual = allowed(user, action, resource, groups, group_roles, role_privileges)
    result = "PASS" if actual == expected else "FAIL"
    print(result, user, action, resource, actual)
    if actual != expected:
        failures.append([user, action, resource, expected, actual])
assert not failures

print("\n=== Example 3: local role revocation snapshot ===")
before = set(effective_privileges("bob", groups, group_roles, role_privileges)[1])
revoked_group_roles = {group: list(roles) for group, roles in group_roles.items()}
revoked_group_roles["assistants"].remove("reviewer")
after = set(effective_privileges("bob", groups, revoked_group_roles, role_privileges)[1])
print("removed:", sorted(before - after))
print("retained:", sorted(after))
assert ("SELECT", "restricted_review_queue") in before - after
assert ("SELECT", "public_notes") in after

print("\n=== Platform dependency boundary ===")
print("Platform-dependent: historical Sentry SQL requires compatible Sentry/Hive integration")
print("Platform-dependent: real enforcement requires Hive, Impala, Solr, or storage integration and policy propagation")

print("\n=== Evidence classification ===")
print("Configured control: local group-to-role-to-privilege policy with deny-by-default")
print("Tested control: effective privilege calculation, positive/negative cases, and local revocation snapshot; PASS")
print("Failed control: none in the secure simulation; no end-to-end enforcement failure was exercised")
print("Untested control: Sentry service, Hive/Impala/Solr enforcement, caches, exports, facets, direct storage, and credentials")
print("Residual risk: local policy state may differ from the effective decision at a real distributed enforcement point")
print("\nCHAPTER 08 SENTRY AND AUTHORIZATION SIMULATION SMOKE TEST PASSED")
