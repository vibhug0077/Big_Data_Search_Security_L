# Big Data Search and Security — runnable examples

This public repository contains only runnable code, the data used by that
code, Docker configuration, and short run guides. Course reading is published
at [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

## Start here

```powershell
git clone https://github.com/vibhug0077/Big_Data_Search_Security_L.git
Set-Location Big_Data_Search_Security_L
docker version
docker compose version
```

Docker Desktop is required for the Hadoop, Elasticsearch, and Java examples.
The Docker environment supplies Python 3, Java 17, and Maven.

## Folders

| Folder | Contents |
|---|---|
| [`labs/`](labs) | Ten chapter-wise examples. Each folder has a `README.md`, `code/`, and a `data/` folder when input data is required. |
| [`examples/hadoop_streaming/`](examples/hadoop_streaming) | Hadoop Streaming mapper, reducer, and input text. |
| [`examples/lucene/`](examples/lucene) | Runnable Maven project for the supplied Java Lucene programs and text input. |
| [`examples/custom_analyzer/`](examples/custom_analyzer) | Runnable Lucene custom-analyzer Maven example. |
| [`examples/course_search_lucene/`](examples/course_search_lucene) | Small standalone Lucene search example. |
| [`examples/security_basics/`](examples/security_basics) | Integrity, RBAC, Kafka configuration, and dashboard source examples. |
| [`docker/`](docker) | Docker Compose and Dockerfile configuration required by the examples. |

Open the `README.md` in the required folder and run its listed command. The
repository deliberately does not include theory pages, infographics, rendered
output, output captures, source archives, validation scripts, or private
repository links.

## Docker commands

Build the shared teaching environment when needed:

```powershell
docker compose -f docker/course-dev/docker-compose.yml build
```

Start Elasticsearch for the Chapter 3 example:

```powershell
docker compose -f docker/elasticsearch/docker-compose.yml up -d
```

Start Hadoop for the Hadoop Streaming example:

```powershell
docker build --platform=linux/amd64 -t hadoop-namenode-python docker/hadoop
docker compose -f docker/hadoop/docker-compose.yml up -d
```

Stop a service after use with the matching `docker compose ... down` command.
