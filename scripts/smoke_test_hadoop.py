"""Check the supplied Hadoop container and run the supplied streaming example."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = ROOT / "workbooks/01_hdfs_mapreduce"


def run(*args: str) -> str:
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout + result.stderr


def main() -> int:
    try:
        run("docker", "inspect", "namenode")
        run("docker", "cp", str(WORKBOOK / "data.txt"), "namenode:/data.txt")
        run("docker", "cp", str(WORKBOOK / "mapper.py"), "namenode:/mapper.py")
        run("docker", "cp", str(WORKBOOK / "reducer.py"), "namenode:/reducer.py")
        command = (
            "set -e; "
            "hdfs dfsadmin -safemode wait; "
            "hdfs dfs -rm -r -f /data/workbook_smoke >/dev/null 2>&1 || true; "
            "hdfs dfs -mkdir -p /data/workbook_smoke/input; "
            "hdfs dfs -put /data.txt /data/workbook_smoke/input/data.txt; "
            "chmod +x /mapper.py /reducer.py; "
            "hadoop jar /opt/hadoop-*/share/hadoop/tools/lib/hadoop-streaming-*.jar "
            "-input /data/workbook_smoke/input/data.txt "
            "-output /data/workbook_smoke/output "
            "-mapper 'python /mapper.py' -reducer 'python /reducer.py'; "
            "hdfs dfs -cat /data/workbook_smoke/output/part-00000"
        )
        output = run("docker", "exec", "namenode", "bash", "-c", command)
        if not output.strip():
            raise RuntimeError("Hadoop Streaming returned empty output")
        print("HADOOP SMOKE TEST PASSED")
        print(output)
        return 0
    except (OSError, subprocess.CalledProcessError, RuntimeError) as exc:
        print(f"HADOOP SMOKE TEST FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
