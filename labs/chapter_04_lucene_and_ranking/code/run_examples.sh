#!/usr/bin/env bash
set -euo pipefail

cleanup() {
  rm -rf /workspace/examples/lucene/src/main/resources/index
  rm -rf /workspace/examples/lucene/target
  rm -f /workspace/examples/lucene/cp.txt
}
trap cleanup EXIT

cd /workspace/examples/lucene
mvn -B clean compile
mvn -q dependency:build-classpath -Dmdep.outputFile=cp.txt
classpath="$(cat cp.txt)"

echo "=== supplied Lucene simple example ==="
java -cp "target/classes:${classpath}" org.example.SimpleLuceneExample
echo "LUCENE SIMPLE EXAMPLE PASSED"

echo "=== supplied Lucene local-file indexer ==="
java -cp "target/classes:${classpath}" org.example.fileSearch.LocalFileIndexer
echo "LUCENE FILE INDEXER PASSED"
