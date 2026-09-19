param(
    [ValidateSet('simple', 'files')]
    [string]$Example = 'simple'
)

docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash /workspace/scripts/run_lucene_inside_container.sh $Example
