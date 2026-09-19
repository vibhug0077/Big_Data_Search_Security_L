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

cd /workspace/java/lucene
mvn -B clean compile
mvn -q dependency:build-classpath -Dmdep.outputFile=cp.txt
classpath="$(cat cp.txt)"
java -cp "target/classes:${classpath}" "$class_name"

