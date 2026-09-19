# Big Data Search and Security — public workbooks and labs

This is the public practical repository for the course. It contains the
student-facing workbooks, executable code, supplied data, Docker environments,
Java/Lucene project, platform-specific examples, lab guides, output captures,
and validation scripts.

The theory book, assessment bank, private source notes, and deployed course
site remain in the private course repository:

- [Private theory and course repository](https://github.com/vibhug0077/Big_Data_Search_Security)

This repository is the public source for practical work. Do not copy private
theory chapters or private course-book files here.

## Local and container roots

```text
Public practical repository:
C:\UPES\Repos\Big_Data_Search_Security_L

Container root:
/workspace
```

Inside the Dockerised course environment, the public repository is mounted at
`/workspace`. Run host commands from the public repository root and container
commands from `/workspace`.

## Quick start

```powershell
git clone https://github.com/vibhug0077/Big_Data_Search_Security_L.git C:\UPES\Repos\Big_Data_Search_Security_L
Set-Location C:\UPES\Repos\Big_Data_Search_Security_L
docker version
docker compose version
```

Read the [installation snapshot](docs/installation_snapshot.md), then choose
the relevant workbook and chapter lab. Every lab contains its own `code/`,
`data/`, and `outputs/` folders.

## Public folder guide

| Folder | Contents | Student use |
|---|---|---|
| [`.github/`](.github) | Public repository validation workflow | Runs practical structure and secret checks. |
| [`assets/`](assets) | Workbook and chapter infographics | Use the visual guide before the practical procedure. |
| [`data/`](data) | Shared teaching data | Use only the supplied files named by a workbook or lab. |
| [`docker/`](docker) | Course development, Hadoop, and Elasticsearch containers | Provides Java/Maven, Python, Hadoop, and Elasticsearch execution environments. |
| [`docs/`](docs) | Public execution context and installation instructions | Check prerequisites, roots, commands, and platform boundaries. |
| [`examples/`](examples) | Supporting runnable examples | Use as small reference examples for the labs. |
| [`java/`](java) | Java 17/Lucene Maven project and text resources | Build and execute the real Lucene programs. |
| [`labs/`](labs) | Ten chapter-wise practical labs | Follow the code, data, command, output, interpretation, and troubleshooting flow. |
| [`platform/`](platform) | Additional platform-specific source examples | Use only when the required KDC, Kafka, Hadoop, Sentry, or credentials exist. |
| [`scripts/`](scripts) | Container wrappers, smoke tests, and secret scan | Run practical checks from the public repository root. |
| [`styles/`](styles) | Shared workbook and lab presentation styles | Used when a workbook or lab page is rendered locally. |
| [`workbooks/`](workbooks) | Environment, Hadoop, Lucene, Elasticsearch, and security guides | Start here for installation and platform procedures. |

The private repository intentionally retains the theory Markdown, theory
notebooks, assessment bank, complete Quarto book, and generated course site.
The public repository contains the executable practical code needed to run the
examples without exposing private theory content.

## Chapter-to-lab map

| Chapter | Public lab | Main public code/data |
|---:|---|---|
| 1 — Search foundations | [`chapter_01_search_foundations/`](labs/chapter_01_search_foundations) | Local Python postings, token analysis, BM25, precision, and recall |
| 2 — Search platforms | [`chapter_02_search_platforms/`](labs/chapter_02_search_platforms) | Platform selection, filtering, document identity, and authorization |
| 3 — Elasticsearch data model | [`chapter_03_elasticsearch_data_model/`](labs/chapter_03_elasticsearch_data_model) | Real Elasticsearch smoke test, mappings, routing, and product data |
| 4 — Lucene and ranking | [`chapter_04_lucene_and_ranking/`](labs/chapter_04_lucene_and_ranking) | Supplied Java Lucene project, text files, indexing, and ranking |
| 5 — Threat and risk | [`chapter_05_threat_and_risk/`](labs/chapter_05_threat_and_risk) | Synthetic risk register and risk-evidence examples |
| 6 — Controls and audit | [`chapter_06_controls_and_audit/`](labs/chapter_06_controls_and_audit) | Control matrix, audit events, and authorization tests |
| 7 — Kerberos | [`chapter_07_kerberos/`](labs/chapter_07_kerberos) | Safe ticket metadata simulation and platform-specific source notes |
| 8 — Sentry and authorization | [`chapter_08_sentry_and_authorization/`](labs/chapter_08_sentry_and_authorization) | RBAC simulation, SQL policy example, and audit evidence |
| 9 — Secure ingestion | [`chapter_09_secure_ingestion/`](labs/chapter_09_secure_ingestion) | HMAC, trusted digest, schema validation, and duplicate handling |
| 10 — Encryption and transport | [`chapter_10_encryption_and_transport/`](labs/chapter_10_encryption_and_transport) | AES-GCM, DEK/KEK wrapping, TLS context, and transport gaps |

## Main workbooks

- [Workbook 00 — Environment and execution flow](workbooks/00_environment)
- [Workbook 01 — HDFS and Hadoop Streaming MapReduce](workbooks/01_hdfs_mapreduce)
- [Workbook 02 — Java Lucene search](workbooks/02_lucene)
- [Workbook 03 — Elasticsearch product search](workbooks/03_elasticsearch)
- [Workbook 04 — Supplied security examples](workbooks/04_security_basics)

## What each practical example must contain

Every chapter lab and workbook should identify:

1. working directory;
2. required Docker/platform dependency;
3. code example;
4. supplied data file;
5. execution command;
6. captured output or an honest platform-dependent label;
7. interpretation and limitations;
8. troubleshooting and viva prompts.

The `outputs/` folders contain saved evidence from tested examples. A saved
command is not proof by itself: check the status marker, input file, and output
description before interpreting a result.

## Run the local and container examples

```powershell
# Chapter 1 and 2 local labs in course-dev
python scripts/smoke_test_chapter_labs.py

# Chapters 5 and 6 dependency-free security labs
python scripts/smoke_test_chapter_05_06.py

# Chapters 7 and 8 simulations
python scripts/smoke_test_chapter_07_08.py

# Chapters 9 and 10 secure examples
python scripts/smoke_test_chapter_09_10.py

# Real Elasticsearch and Java Lucene checks
python scripts/smoke_test_chapter_03_04.py

# Hadoop smoke test, after the Hadoop container is running
python scripts/smoke_test_hadoop.py
```

Run Lucene directly:

```powershell
.\scripts\run_lucene.ps1 -Example simple
.\scripts\run_lucene.ps1 -Example files
```

Equivalent Bash commands:

```bash
bash scripts/run_lucene.sh simple
bash scripts/run_lucene.sh files
```

## Validation and safety

```powershell
python scripts/validate_public_workbooks.py
python scripts/scan_secrets.py
```

The public repository must not contain real passwords, tokens, private keys,
keytabs, generated Lucene indexes, Maven `target/` output, Docker volumes, or
private theory files. Kerberos, Sentry, Kafka, and secured Hadoop examples are
labelled `platform-dependent` unless their required infrastructure has been
genuinely tested.

## Relationship to the private course repository

The private repository is the source for the deployed theory book and course
navigation. This public repository is the source for the downloadable practical
material and executable examples. Links from private theory pages should point
to folders and files in this repository for code, data, workbooks, labs, and
captured outputs.
