# Lucene Custom Analyzer

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

The code demonstrates a whitespace tokenizer, lowercase filter, and a small
stopword set.

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/examples/custom_analyzer && mvn -B compile exec:java"
```
