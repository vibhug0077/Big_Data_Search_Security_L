# Chapter 3 — Elasticsearch data model

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

- Code: `code/elasticsearch_data_model_smoke.py`
- Input data: `data/products.json` (Bulk NDJSON)
- Additional source: `code/elasticsearch_query_dsl.ipynb`

```powershell
docker compose -f docker/elasticsearch/docker-compose.yml up -d
docker compose -f docker/course-dev/docker-compose.yml run --rm `
  -e ELASTICSEARCH_URL=http://host.docker.internal:9200 course-dev `
  bash -lc "cd /workspace/labs/chapter_03_elasticsearch_data_model && python3 code/elasticsearch_data_model_smoke.py"
docker compose -f docker/elasticsearch/docker-compose.yml down
```

A successful run prints `ELASTICSEARCH EXAMPLE PASSED` and `count=5`. The
script creates and removes a disposable local index.
