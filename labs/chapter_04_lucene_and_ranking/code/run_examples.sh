#!/usr/bin/env bash
set -euo pipefail

cleanup() {
  rm -rf /workspace/java/lucene/src/main/resources/index
}
trap cleanup EXIT

echo "=== supplied Lucene simple example ==="
bash /workspace/scripts/run_lucene_inside_container.sh simple
echo "LUCENE SIMPLE EXAMPLE PASSED"

echo "=== supplied Lucene local-file indexer ==="
bash /workspace/scripts/run_lucene_inside_container.sh files
echo "LUCENE FILE INDEXER PASSED"
