"""Execute the deterministic threat inventory and risk examples."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent.parent
DATA = HERE / "data/threat_risk_data.json"
records = json.loads(DATA.read_text(encoding="utf-8"))

print("CHAPTER 05 THREAT AND RISK")
print("Working directory: /workspace/labs/chapter_05_threat_and_risk")
print("Data file: data/threat_risk_data.json")

print("\n=== Example 1: asset and trust-boundary inventory ===")
for component in records["components"]:
    print(
        f"{component['name']}: protect {component['asset']} at "
        f"{component['boundary']} ({component['owner']})"
    )

print("\n=== Example 2: transparent ordinal risk register ===")
risks = []
for source in records["risks"]:
    risk = dict(source)
    risk["priority"] = risk["likelihood"] * risk["impact"]
    risk["rating_note"] = "ordinal comparison; review with evidence"
    risks.append(risk)
for risk in sorted(risks, key=lambda row: (-row["priority"], row["id"])):
    print(
        risk["id"],
        risk["priority"],
        risk["threat"],
        "owner=",
        risk["owner"],
        "|",
        risk["rating_note"],
    )

print("\n=== Example 3: repeated-denial review signal ===")
events = records["audit_events"]
denials = Counter(event["actor"] for event in events if event["outcome"] == "deny")
alerts = {actor: count for actor, count in denials.items() if count >= records["denial_threshold"]}
evidence_ids = [event["correlation_id"] for event in events if event["actor"] in alerts]
print("denials:", dict(denials))
print("review signals:", alerts)
print("evidence IDs:", evidence_ids)
assert alerts == {"alice": 3}
assert evidence_ids == ["c1", "c2", "c3"]

print("\n=== Evidence classification ===")
print("Configured control: risk-treatment suggestions are recorded; no production control is configured")
print("Tested control: deterministic repeated-denial review signal; PASS")
print("Failed control: none exercised by this risk-only model; no effectiveness claim is made")
print("Untested control: resource-specific role, payload limit, and restore rehearsal")
print("Residual risk: live enforcement, alert timing, audit-store integrity, and recovery remain unverified")
print("\nCHAPTER 05 THREAT AND RISK SMOKE TEST PASSED")
