# CourseSearch Lucene example

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

This standalone example indexes two short documents and searches for
`security`.

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/examples/course_search_lucene && mvn -B compile exec:java"
```
