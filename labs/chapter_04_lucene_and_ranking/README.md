# Chapter 4 — Lucene and ranking

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

- Runner: `code/run_examples.sh`
- Java source and input text: [`../../examples/lucene/`](../../examples/lucene)

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/labs/chapter_04_lucene_and_ranking && bash code/run_examples.sh"
```

The runner compiles the supplied Maven project, runs the in-memory and
local-file Lucene examples, then removes generated build and index files.
