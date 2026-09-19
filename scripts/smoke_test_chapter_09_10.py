"""Run the Chapter 9 and Chapter 10 secure examples in course-dev."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMPOSE = [
    "docker",
    "compose",
    "-f",
    "docker/course-dev/docker-compose.yml",
    "run",
    "--rm",
    "course-dev",
]
LABS = {
    "chapter_09_secure_ingestion": (
        "code/secure_ingestion_examples.py",
        "CHAPTER 09 SECURE INGESTION SMOKE TEST PASSED",
    ),
    "chapter_10_encryption_and_transport": (
        "code/encryption_transport_examples.py",
        "CHAPTER 10 ENCRYPTION AND TRANSPORT SMOKE TEST PASSED",
    ),
}


def main() -> int:
    try:
        for lab, (script, marker) in LABS.items():
            command = f"cd /workspace/labs/{lab} && python3 {script}"
            result = subprocess.run(
                COMPOSE + ["bash", "-lc", command],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            if marker not in result.stdout:
                raise RuntimeError(f"{lab} did not produce its evidence marker")
            print(result.stdout.rstrip())
        print("CHAPTER 09-10 SECURITY LABS SMOKE TEST PASSED")
        return 0
    except (OSError, subprocess.CalledProcessError, RuntimeError) as exc:
        detail = exc.stdout if isinstance(exc, subprocess.CalledProcessError) else ""
        print(f"CHAPTER 09-10 SECURITY LABS SMOKE TEST FAILED: {exc}\n{detail}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
