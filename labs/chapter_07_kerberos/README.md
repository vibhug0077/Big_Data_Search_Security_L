# Chapter 7 — Kerberos

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

- Runnable simulation: `code/kerberos_simulation.py`
- Input data: `data/kerberos_simulation_data.json`
- Platform source: `platform/` (Kafka and KDC configuration examples)

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/labs/chapter_07_kerberos && python3 code/kerberos_simulation.py"
```

Only the Python ticket-metadata simulation runs without external services. The
files in `platform/` require a KDC, Kafka, credentials, and service-specific
configuration.
