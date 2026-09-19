# Chapter 9 — Secure ingestion

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

- Code: `code/secure_ingestion_examples.py`
- Input data: `data/ingestion_data.json`

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/labs/chapter_09_secure_ingestion && python3 code/secure_ingestion_examples.py"
```

The script demonstrates schema validation, integrity checks, duplicate
handling, and rejection of invalid supplied payloads.
