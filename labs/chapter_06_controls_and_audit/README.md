# Chapter 6 — Controls and audit

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

- Code: `code/controls_audit_examples.py`
- Input data: `data/controls_audit_data.json`

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/labs/chapter_06_controls_and_audit && python3 code/controls_audit_examples.py"
```

The script evaluates the supplied control matrix and prints audit-event
results, including control status and residual-risk evidence.
