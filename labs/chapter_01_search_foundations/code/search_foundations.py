"""Run the supplied Chapter 1 local search-foundation examples."""

from __future__ import annotations

from collections import Counter, defaultdict
import json
import math
from pathlib import Path
import re
import unicodedata


LAB_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = LAB_ROOT / "data" / "search_foundations_data.json"
DATA = json.loads(DATA_PATH.read_text(encoding="utf-8"))

print("CHAPTER 01 SEARCH FOUNDATIONS")
print("Working directory:", Path.cwd())
print("Data file:", DATA_PATH.relative_to(LAB_ROOT).as_posix())

print("\n=== Example 1: positional inverted index ===")
documents = DATA["documents"]


def analyze(text):
    return re.findall(r"[a-z0-9]+", text.lower())


postings = defaultdict(lambda: defaultdict(list))
for document_id, text in documents.items():
    for position, term in enumerate(analyze(text)):
        postings[term][document_id].append(position)

terms = analyze("data security")
candidates = set(postings[terms[0]]) & set(postings[terms[1]])
phrase_hits = {
    doc
    for doc in candidates
    if any(p + 1 in postings["security"][doc] for p in postings["data"][doc])
}
print("AND:", sorted(candidates))
print("Phrase:", sorted(phrase_hits))
relevant = {"D1", "D4"}
precision = len(candidates & relevant) / len(candidates)
recall = len(candidates & relevant) / len(relevant)
print("Precision:", round(precision, 3), "Recall:", recall)

print("\n=== Example 2: token analysis ===")
phase1_samples = DATA["analysis_samples"]


def phase1_analyze(text):
    normalized = unicodedata.normalize("NFKC", text).casefold()
    return re.findall(r"[a-z0-9]+(?:\+[+#])?", normalized)


for sample in phase1_samples:
    print(sample, "->", phase1_analyze(sample))

print("\n=== Example 3: transparent BM25 oracle ===")
phase1_docs = DATA["bm25_documents"]
phase1_tokens = {
    doc_id: phase1_analyze(text) for doc_id, text in phase1_docs.items()
}
phase1_lengths = {
    doc_id: len(tokens) for doc_id, tokens in phase1_tokens.items()
}
phase1_average_length = sum(phase1_lengths.values()) / len(phase1_lengths)
phase1_query = DATA["query"]
phase1_k1, phase1_b = 1.2, 0.75


def phase1_bm25(doc_id, query_terms):
    tokens = phase1_tokens[doc_id]
    counts = Counter(tokens)
    score = 0.0
    for term in query_terms:
        document_frequency = sum(
            term in set(values) for values in phase1_tokens.values()
        )
        idf = math.log(
            1
            + (len(phase1_tokens) - document_frequency + 0.5)
            / (document_frequency + 0.5)
        )
        frequency = counts[term]
        length_factor = (
            1
            - phase1_b
            + phase1_b * phase1_lengths[doc_id] / phase1_average_length
        )
        score += idf * (frequency * (phase1_k1 + 1)) / (
            frequency + phase1_k1 * length_factor
        )
    return score


phase1_ranking = sorted(
    ((doc_id, phase1_bm25(doc_id, phase1_query)) for doc_id in phase1_docs),
    key=lambda item: (-item[1], item[0]),
)
for doc_id, score in phase1_ranking:
    print(doc_id, round(score, 3), phase1_lengths[doc_id])

print("\n=== Example 4: precision and recall ===")
phase1_retrieved = DATA["retrieved"]
phase1_relevant = set(DATA["relevant"])
phase1_hits = set(phase1_retrieved) & phase1_relevant
phase1_precision = len(phase1_hits) / len(phase1_retrieved)
phase1_recall = len(phase1_hits) / len(phase1_relevant)
print({
    "retrieved": len(phase1_retrieved),
    "relevant_in_retrieved": len(phase1_hits),
    "precision": round(phase1_precision, 3),
    "recall": phase1_recall,
})

print("\nCHAPTER 01 SEARCH FOUNDATIONS SMOKE TEST PASSED")
