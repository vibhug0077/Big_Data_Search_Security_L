"""Run the supplied product example against the real local Elasticsearch service."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path("/workspace")
os.environ["ELASTICSEARCH_URL"] = os.environ.get(
    "ELASTICSEARCH_URL", "http://host.docker.internal:9200"
)
os.environ["ELASTICSEARCH_PRODUCTS"] = str(
    ROOT / "labs/chapter_03_elasticsearch_data_model/data/products.json"
)
result = subprocess.run(
    [sys.executable, str(ROOT / "scripts/smoke_test_elasticsearch.py")],
    cwd=ROOT,
    env=os.environ.copy(),
)
if result.returncode == 0:
    print("CHAPTER 03 ELASTICSEARCH DATA MODEL SMOKE TEST PASSED")
raise SystemExit(result.returncode)
