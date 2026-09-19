# Chapter 8 — Sentry and authorization

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

- Runnable simulation: `code/authorization_simulation.py`
- Input data: `data/authorization_simulation_data.json`
- Platform policy: `platform/sentry_hive_roles.sql`

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/labs/chapter_08_sentry_and_authorization && python3 code/authorization_simulation.py"
```

The Python simulation is standalone. The SQL policy file requires a configured
Sentry/Hive environment and is not executable in the shared course container.
