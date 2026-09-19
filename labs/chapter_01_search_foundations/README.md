# Chapter 1 — Search foundations

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

- Code: `code/search_foundations.py`
Input data: `data/search_foundations_data.json`

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/labs/chapter_01_search_foundations && python3 code/search_foundations.py"
```

The script prints tokenisation, postings, Boolean matching, BM25, precision,
and recall for the supplied records.
