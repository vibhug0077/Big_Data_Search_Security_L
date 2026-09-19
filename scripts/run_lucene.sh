#!/usr/bin/env bash
set -euo pipefail

example="${1:-simple}"
if [[ "$example" == "simple" ]]; then
  class_name="org.example.SimpleLuceneExample"
elif [[ "$example" == "files" ]]; then
  class_name="org.example.fileSearch.LocalFileIndexer"
else
  echo "usage: $0 [simple|files]" >&2
  exit 2
fi

docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev \
  bash /workspace/scripts/run_lucene_inside_container.sh "$example"
