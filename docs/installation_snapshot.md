---
title: "Installation snapshot"
---

{{< include execution_context.md >}}

This page records the installation and terminal flow found in the supplied source examples. The canonical course checkout is `C:\UPES\Repos\Big_Data_Search_Security_L`; the commands below are kept recognisable so that classroom instructions remain traceable to the working examples.

## Host prerequisite

The source notes list Java and Maven as prerequisites for the Lucene example. In this repository, Java and Maven are installed inside the course development container so the learner does not need a host-side Java installation.

The only required host installation is Docker Desktop with Docker Compose available through `docker compose`.

Check PowerShell:

```powershell
docker version
docker compose version
```

Check Bash:

```bash
docker version
docker compose version
```

## Elasticsearch snapshot

From the repository root:

```powershell
docker compose -f docker/elasticsearch/docker-compose.yml up -d
docker compose -f docker/elasticsearch/docker-compose.yml ps
Invoke-RestMethod http://localhost:9200
```

The service uses the supplied single-node Elasticsearch example and the supplied `products.json` file. The basic teaching service intentionally follows the source configuration with security disabled; a separate secured configuration must be tested before any security-specific publication.

The source command sequence is preserved in [the Elasticsearch workbook](../workbooks/03_elasticsearch/README.md).

## Hadoop/HDFS snapshot

Build the supplied Python-enabled NameNode image:

```powershell
docker build --platform=linux/amd64 -t hadoop-namenode-python docker/hadoop
docker compose -f docker/hadoop/docker-compose.yml up -d
docker compose -f docker/hadoop/docker-compose.yml ps
```

Open the NameNode container and verify HDFS:

```powershell
docker exec -it namenode bash
hdfs dfs -ls /
hdfs dfs -mkdir -p /data/input
echo "Sample Data for Hadoop" > some_data.txt
hdfs dfs -put some_data.txt /data/input/
hdfs dfs -ls /data/input/
hdfs dfs -cat /data/input/some_data.txt
```

The word-count example uses the supplied `data.txt`, `mapper.py`, `reducer.py`, and `mr_execution_commands.txt`. The full sequence is documented in [the HDFS and MapReduce workbook](../workbooks/01_hdfs_mapreduce/README.md).

## Lucene snapshot

The source Lucene project is built with Maven and targets Java 17. In this repository it runs inside the course development container:

```powershell
.\scripts\run_lucene.ps1 -Example simple
.\scripts\run_lucene.ps1 -Example files
```

The equivalent Bash commands are:

```bash
bash scripts/run_lucene.sh simple
bash scripts/run_lucene.sh files
```

The source project contains `SimpleLuceneExample.java` and `LocalFileIndexer.java`. The workbook keeps those programs as the runnable examples and explains their output rather than replacing them with a Python search implementation.
