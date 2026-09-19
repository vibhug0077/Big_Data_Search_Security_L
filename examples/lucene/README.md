# Java Lucene examples

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

This Maven project contains `SimpleLuceneExample.java`, `LocalFileIndexer.java`,
and the three input text files under `src/main/resources/text_files/`.

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/examples/lucene && mvn -B clean compile && mvn -q dependency:build-classpath -Dmdep.outputFile=cp.txt && java -cp target/classes:$(cat cp.txt) org.example.SimpleLuceneExample && java -cp target/classes:$(cat cp.txt) org.example.fileSearch.LocalFileIndexer"
```

Maven `target/`, `cp.txt`, and the generated Lucene index are local build
artifacts and are ignored by Git.
