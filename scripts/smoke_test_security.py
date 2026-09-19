"""Run the dependency-free supplied security examples in the course container."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = "/workspace/workbooks/04_security_basics"
COMPOSE = ["docker", "compose", "-f", "docker/course-dev/docker-compose.yml", "run", "--rm", "course-dev"]


def run_in_container(command: str) -> str:
    result = subprocess.run(
        COMPOSE + ["bash", "-c", command],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def main() -> int:
    try:
        py_files = sorted((ROOT / "workbooks/04_security_basics").glob("*.source.py"))
        quoted = " ".join(f"{SOURCE}/{path.name}" for path in py_files)
        run_in_container(f"python3 -m py_compile {quoted}")
        tampering = run_in_container(
            f"cd /tmp && python3 {SOURCE}/tampering_example.source.py"
        )
        rbac = run_in_container(
            f"cd /tmp && python3 {SOURCE}/RoleBasedAccess.source.py"
        )
        if "After Tampering : False" not in tampering:
            raise RuntimeError("tampering example did not reject modified data")
        if "Unauthorized access" not in rbac:
            raise RuntimeError("RBAC example did not reject the guest access")
        print("SECURITY SOURCE SMOKE TEST PASSED")
        print("syntax_checked=" + str(len(py_files)))
        return 0
    except (OSError, subprocess.CalledProcessError, RuntimeError) as exc:
        print(f"SECURITY SOURCE SMOKE TEST FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

