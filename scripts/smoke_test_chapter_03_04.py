"""Run the real Chapter 3 Elasticsearch and Chapter 4 Lucene labs."""

from __future__ import annotations

import sys
import time
import subprocess
from urllib.request import urlopen
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ES_COMPOSE = ["docker", "compose", "-f", "docker/elasticsearch/docker-compose.yml"]
DEV_COMPOSE = [
    "docker",
    "compose",
    "-f",
    "docker/course-dev/docker-compose.yml",
    "run",
    "--rm",
    "course-dev",
]


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, check=True, text=True, capture_output=True)


def wait_for_elasticsearch() -> None:
    for _ in range(30):
        try:
            with urlopen("http://localhost:9200/_cluster/health", timeout=3) as response:
                if response.status == 200:
                    return
        except OSError:
            time.sleep(2)
    raise RuntimeError("Elasticsearch did not become ready on localhost:9200")


def main() -> int:
    service_started = False
    try:
        run(ES_COMPOSE + ["up", "-d"])
        service_started = True
        wait_for_elasticsearch()

        elastic = run(
            DEV_COMPOSE
            + [
                "bash",
                "-lc",
                "cd /workspace/labs/chapter_03_elasticsearch_data_model && "
                "python3 code/elasticsearch_data_model_smoke.py",
            ]
        )
        if "CHAPTER 03 ELASTICSEARCH DATA MODEL SMOKE TEST PASSED" not in elastic.stdout:
            raise RuntimeError("Chapter 3 did not produce its evidence marker")
        print(elastic.stdout.rstrip())

        lucene = run(
            DEV_COMPOSE
            + [
                "bash",
                "-lc",
                "cd /workspace/labs/chapter_04_lucene_and_ranking && bash code/run_examples.sh",
            ]
        )
        for marker in ("LUCENE SIMPLE EXAMPLE PASSED", "LUCENE FILE INDEXER PASSED"):
            if marker not in lucene.stdout:
                raise RuntimeError(f"Chapter 4 did not produce marker: {marker}")
        print(lucene.stdout.rstrip())
        print("CHAPTER 03-04 PLATFORM LABS SMOKE TEST PASSED")
        return 0
    except (OSError, subprocess.CalledProcessError, RuntimeError) as exc:
        detail = exc.stdout if isinstance(exc, subprocess.CalledProcessError) else ""
        print(f"CHAPTER 03-04 PLATFORM LABS SMOKE TEST FAILED: {exc}\n{detail}", file=sys.stderr)
        return 1
    finally:
        if service_started:
            subprocess.run(ES_COMPOSE + ["down"], cwd=ROOT, check=False)


if __name__ == "__main__":
    raise SystemExit(main())
