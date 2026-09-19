# Chapter 10 — Encryption and transport

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

- Code: `code/encryption_transport_examples.py`
- Input data: `data/encryption_transport_data.json`

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/labs/chapter_10_encryption_and_transport && python3 code/encryption_transport_examples.py"
```

The script uses only synthetic teaching values and prints the encryption,
wrapping, and transport-check results.
