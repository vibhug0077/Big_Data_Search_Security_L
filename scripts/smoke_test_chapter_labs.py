"""Execute the Chapter 1 and Chapter 2 local labs in the course container."""

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
    "chapter_01_search_foundations": "CHAPTER 01 SEARCH FOUNDATIONS SMOKE TEST PASSED",
    "chapter_02_search_platforms": "CHAPTER 02 SEARCH PLATFORMS SMOKE TEST PASSED",
}


def main() -> int:
    try:
        for lab, marker in LABS.items():
            command = (
                f"cd /workspace/labs/{lab} && "
                f"python3 code/{'search_foundations.py' if lab.startswith('chapter_01') else 'search_platforms.py'}"
            )
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
        print("CHAPTER 01-02 LOCAL LABS SMOKE TEST PASSED")
        return 0
    except (OSError, subprocess.CalledProcessError, RuntimeError) as exc:
        print(f"CHAPTER 01-02 LOCAL LABS SMOKE TEST FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
