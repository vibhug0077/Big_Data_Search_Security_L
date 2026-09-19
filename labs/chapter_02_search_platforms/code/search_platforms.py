"""Run the supplied Chapter 2 local search-platform workflow examples."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path


LAB_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = LAB_ROOT / "data" / "search_platforms_data.json"
DATA = json.loads(DATA_PATH.read_text(encoding="utf-8"))

print("CHAPTER 02 SEARCH PLATFORMS")
print("Working directory:", Path.cwd())
print("Data file:", DATA_PATH.relative_to(LAB_ROOT).as_posix())

print("\n=== Example 1: text matching and metadata filtering ===")
records = DATA["records"]
query_terms = {"data", "security"}
matched = [r for r in records if query_terms & set(r["body"].split())]
filtered = [r for r in matched if r["department"] == "CSE"]
print("Text matches:", [r["id"] for r in matched])
print("Filtered matches:", [r["id"] for r in filtered])
print("Counts within filtered results:", dict(Counter(r["department"] for r in filtered)))

print("\n=== Example 2: auditable platform selection ===")
phase1_requirements = DATA["requirements"]
phase1_candidates = DATA["candidates"]
for name, capabilities in phase1_candidates.items():
    satisfied = sum(
        capabilities[key] == required
        for key, required in phase1_requirements.items()
    )
    print(name, f"{satisfied}/{len(phase1_requirements)} requirements aligned")

print("\n=== Example 3: stable IDs and idempotent upserts ===")
phase1_registry = {}


def phase1_document_id(source_uri, logical_part):
    raw = f"{source_uri}\0{logical_part}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:12]


def phase1_upsert(source_uri, logical_part, body):
    doc_id = phase1_document_id(source_uri, logical_part)
    previous = phase1_registry.get(doc_id)
    phase1_registry[doc_id] = {
        "id": doc_id,
        "body": body,
        "version": 1 if previous is None else previous["version"] + 1,
    }
    return "created" if previous is None else "replaced", phase1_registry[doc_id]


upsert = DATA["upsert"]
print(phase1_upsert(upsert["source_uri"], upsert["logical_part"], upsert["body"]))
print(phase1_upsert(upsert["source_uri"], upsert["logical_part"], upsert["body"]))
print("stored documents:", len(phase1_registry))
print("source URI is an identifier only; no PDF is opened")

print("\n=== Example 4: matching, authorization, and facet scope ===")
phase1_records = DATA["authorized_records"]
phase1_terms = {"data", "security"}
phase1_text_hits = [
    r for r in phase1_records if phase1_terms & set(r["body"].split())
]
phase1_visible_hits = [r for r in phase1_text_hits if r["allowed"]]
print("text population:", len(phase1_text_hits))
print("authorized population:", len(phase1_visible_hits))
print(
    "authorized facets:",
    dict(Counter(r["department"] for r in phase1_visible_hits)),
)

print("\nCHAPTER 02 SEARCH PLATFORMS SMOKE TEST PASSED")
