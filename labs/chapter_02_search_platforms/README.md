# Chapter 2 — Search platforms and workflow

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

- Code: `code/search_platforms.py`
Input data: `data/search_platforms_data.json`

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/labs/chapter_02_search_platforms && python3 code/search_platforms.py"
```

The script demonstrates matching, filtering, platform selection, stable
document IDs, authorization, and facet scope using the supplied JSON data.
