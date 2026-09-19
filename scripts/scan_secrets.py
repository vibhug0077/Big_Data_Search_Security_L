"""Scan publishable source files for high-confidence secret material."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".venv", "_site", ".quarto", "__pycache__", "target"}
TEXT_SUFFIXES = {
    ".md",
    ".qmd",
    ".py",
    ".json",
    ".txt",
    ".sql",
    ".yml",
    ".yaml",
    ".sh",
    ".ps1",
    ".ipynb",
}
PATTERNS = (
    ("private-key-block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    ("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
)


def main() -> int:
    findings: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT)
        for label, pattern in PATTERNS:
            if pattern.search(content):
                findings.append(f"{label}: {relative}")
    if findings:
        print("SECRETS SCAN FAILED", file=sys.stderr)
        print("\n".join(findings), file=sys.stderr)
        return 1
    print("SECRETS SCAN PASSED: no high-confidence private-key or token material found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
