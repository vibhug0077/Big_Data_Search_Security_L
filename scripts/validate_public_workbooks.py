"""Validate the public practical repository without requiring the private theory book."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LABS = sorted((ROOT / "labs").glob("chapter_*"))
REQUIRED_WORKBOOKS = [
    ROOT / "workbooks/00_environment/README.md",
    ROOT / "workbooks/01_hdfs_mapreduce/README.md",
    ROOT / "workbooks/02_lucene/README.md",
    ROOT / "workbooks/03_elasticsearch/README.md",
    ROOT / "workbooks/04_security_basics/README.md",
]
REQUIRED_FILES = [
    ROOT / "docs/execution_context.md",
    ROOT / "docs/installation_snapshot.md",
    ROOT / "docker/course-dev/Dockerfile",
    ROOT / "docker/course-dev/docker-compose.yml",
    ROOT / "docker/elasticsearch/docker-compose.yml",
    ROOT / "docker/hadoop/Dockerfile",
    ROOT / "docker/hadoop/docker-compose.yml",
    ROOT / "java/lucene/pom.xml",
    ROOT / "java/lucene/src/main/java/org/example/SimpleLuceneExample.java",
    ROOT / "java/lucene/src/main/java/org/example/fileSearch/LocalFileIndexer.java",
]
FORBIDDEN_PATHS = ("theory", "notebooks", "ASSESSMENT_BANK.qmd", "index.qmd", "about.qmd")
PRIVATE_ROOT = re.compile(r"C:\\UPES\\Repos\\Big_Data_Search_Security(?:[\\`\s]|$)")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []

    if len(LABS) != 10:
        fail(f"expected 10 chapter labs, found {len(LABS)}", failures)
    for lab in LABS:
        for child in ("README.md", "code", "data", "outputs"):
            if not (lab / child).exists():
                fail(f"missing {lab.relative_to(ROOT)}/{child}", failures)

    for path in [*REQUIRED_WORKBOOKS, *REQUIRED_FILES]:
        if not path.exists():
            fail(f"missing required public file: {path.relative_to(ROOT)}", failures)

    for path in ROOT.iterdir():
        if path.name in FORBIDDEN_PATHS:
            fail(f"private course content present in public repository: {path.name}", failures)

    for path in [*ROOT.rglob("*.md"), *ROOT.rglob("*.qmd"), *ROOT.rglob("*.py"), *ROOT.rglob("*.txt"), *ROOT.rglob("*.ipynb")]:
        if any(part in {".git", ".quarto", "_site", "target", "__pycache__"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if PRIVATE_ROOT.search(text):
            fail(f"private local root remains in {path.relative_to(ROOT)}", failures)
        broken_notebooks_link = "../" + "../notebooks/"
        broken_theory_link = "../" + "../theory/"
        if broken_notebooks_link in text or broken_theory_link in text:
            fail(f"broken private theory link remains in {path.relative_to(ROOT)}", failures)

    for path in ROOT.glob("workbooks/03_elasticsearch/*.ipynb"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            fail(f"invalid public notebook JSON: {path.relative_to(ROOT)}: {error}", failures)

    if failures:
        print("PUBLIC WORKBOOK VALIDATION FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print(f"PUBLIC WORKBOOK VALIDATION PASSED: {len(LABS)} labs, {len(REQUIRED_WORKBOOKS)} workbooks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
