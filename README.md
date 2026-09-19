# Big Data Search and Security — companion guide

This repository is a README-only companion for the Big Data Search and
Security course. It is not the published course book and it does not contain
duplicate course files.

The actual theory, workbooks, labs, data, Docker files, Java/Lucene project,
notebooks, scripts, and rendered course site are maintained in the public
course repository:

- [Big_Data_Search_Security course repository](https://github.com/vibhug0077/Big_Data_Search_Security)
- [Rendered course site](https://vibhug0077.github.io/Big_Data_Search_Security/)

All links below point to the source course repository on GitHub. Use the
`main` branch unless the instructor provides another branch.

## Local working locations

```text
Course source:
C:\UPES\Repos\Big_Data_Search_Security

This README-only companion:
C:\UPES\Repos\Big_Data_Search_Security_L

Container mount:
/workspace
```

Inside the Dockerised course environment, `/workspace` is the mounted course
repository. Commands in the course should be run from `/workspace` unless a
workbook states otherwise.

## Start here

1. Open the [course landing page](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/index.qmd).
2. Read the [installation snapshot](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/docs/installation_snapshot.md).
3. Read the [course source map](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/docs/source_map.md).
4. Select the theory chapter and its linked lab.
5. Open the corresponding workbook and inspect its supplied data files.
6. Run the command from `/workspace`.
7. Compare the run with the saved output capture.

Clone the actual course repository for local work:

```powershell
git clone https://github.com/vibhug0077/Big_Data_Search_Security.git C:\UPES\Repos\Big_Data_Search_Security
Set-Location C:\UPES\Repos\Big_Data_Search_Security
```

## Folder guide

| Folder | What it contains | How students use it |
|---|---|---|
| [`assets/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/assets) | Hero graphics, chapter infographics, and visual learning assets | View the visual explanation attached to the landing page, chapters, and workbooks. |
| [`data/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/data) | Shared synthetic teaching data | Use only the supplied files named by a workbook or lab. |
| [`docker/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/docker) | Course development, Hadoop, and Elasticsearch container definitions | Start the platform environment required by the selected workbook. |
| [`docs/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/docs) | Installation, provenance, execution context, source map, and student checklist | Confirm prerequisites, paths, evidence rules, and publication boundaries. |
| [`downloads/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/downloads) | Learner-facing download index and source links | Download the theory, lab, workbook, Docker, Java, data, and notebook material. |
| [`examples/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/examples) | Small supporting examples used by the course | Read the example before adapting it in a lab. |
| [`java/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/java) | Supplied Java 17/Lucene Maven project and text inputs | Build and run the real Lucene examples inside the course container. |
| [`labs/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/labs) | Ten chapter-wise lab guides with code, data, outputs, interpretation, and troubleshooting | Complete the lab after reading its theory chapter and workbook. |
| [`notebooks/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/notebooks) | Theory and legacy source notebooks | Read the saved theory examples and outputs; platform-dependent notebooks are labelled. |
| [`platform/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/platform) | Additional platform-specific supplied source | Use only when the required Hadoop, Kafka, KDC, Sentry, or credential infrastructure is available. |
| [`scripts/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/scripts) | Run wrappers, smoke tests, validators, and presentation audits | Run checks from the repository root before publishing or submitting work. |
| [`styles/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/styles) | Quarto styling for the landing page, theory, workbooks, code, and output panels | Normally leave unchanged; these styles keep source code and output readable. |
| [`tests/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/tests) | Static repository structure tests | Run the test suite after changing course files. |
| [`theory/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/theory) | Markdown source for the ten theory chapters | Use as the editable theory source behind the rendered chapter notebooks. |
| [`workbooks/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/workbooks) | Environment, Hadoop, Lucene, Elasticsearch, and security practical guides | Follow the command, data-file, output-capture, and interpretation sequence. |

### Generated and hidden folders

| Folder | Status and instruction |
|---|---|
| [`.github/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/.github) | Repository workflow and automation configuration. Change only when the publication or validation workflow requires it. |
| [`.quarto/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/.quarto) | Local Quarto working metadata. Do not use it as course source content. |
| [`_site/`](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/_site) | Generated HTML output from `quarto render`. Rebuild it locally; do not edit generated pages directly. |

The `.git/` directory is version-control metadata and is not course content.

## Chapter sequence

| Chapter | Theory | Lab | Main practical material |
|---:|---|---|---|
| 1 | [Search foundations](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/notebooks/01_Search_Foundations.ipynb) | [Chapter 1 lab](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/labs/chapter_01_search_foundations) | Inverted-index and retrieval examples |
| 2 | [Search platforms](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/notebooks/02_Search_Platforms.ipynb) | [Chapter 2 lab](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/labs/chapter_02_search_platforms) | Platform selection and workflow |
| 3 | [Elasticsearch data model](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/notebooks/03_Elasticsearch_Data_Model.ipynb) | [Chapter 3 lab](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/labs/chapter_03_elasticsearch_data_model) | Real Elasticsearch container |
| 4 | [Lucene and ranking](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/notebooks/04_Lucene_and_Ranking.ipynb) | [Chapter 4 lab](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/labs/chapter_04_lucene_and_ranking) | Real Java Lucene/Maven project |
| 5 | [Threat and risk](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/notebooks/05_Threat_and_Risk.ipynb) | [Chapter 5 lab](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/labs/chapter_05_threat_and_risk) | Risk scoring and evidence |
| 6 | [Controls and audit](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/notebooks/06_Controls_and_Audit.ipynb) | [Chapter 6 lab](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/labs/chapter_06_controls_and_audit) | Control matrix and audit events |
| 7 | [Kerberos](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/notebooks/07_Kerberos.ipynb) | [Chapter 7 lab](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/labs/chapter_07_kerberos) | Ticket metadata and platform boundary |
| 8 | [Sentry and authorization](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/notebooks/08_Sentry_and_Authorization.ipynb) | [Chapter 8 lab](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/labs/chapter_08_sentry_and_authorization) | RBAC simulation and platform notes |
| 9 | [Secure ingestion](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/notebooks/09_Secure_Ingestion.ipynb) | [Chapter 9 lab](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/labs/chapter_09_secure_ingestion) | Integrity, authentication, and deduplication |
| 10 | [Encryption and transport](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/notebooks/10_Encryption_and_Transport.ipynb) | [Chapter 10 lab](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/labs/chapter_10_encryption_and_transport) | AEAD, key wrapping, and TLS |

## Main workbooks

- [Workbook 00 — Environment and execution flow](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/workbooks/00_environment)
- [Workbook 01 — HDFS and Hadoop Streaming MapReduce](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/workbooks/01_hdfs_mapreduce)
- [Workbook 02 — Java Lucene search](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/workbooks/02_lucene)
- [Workbook 03 — Elasticsearch product search](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/workbooks/03_elasticsearch)
- [Workbook 04 — Supplied security examples](https://github.com/vibhug0077/Big_Data_Search_Security/tree/main/workbooks/04_security_basics)

## Root files

| File | Purpose |
|---|---|
| [`index.qmd`](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/index.qmd) | Single course landing page and navigation entry point. |
| [`about.qmd`](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/about.qmd) | Course scope, provenance, and publication boundary. |
| [`ASSESSMENT_BANK.qmd`](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/ASSESSMENT_BANK.qmd) | Six Bloom-mapped questions for each of the ten chapters. |
| [`_quarto.yml`](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/_quarto.yml) | Quarto render list, navigation, resources, and stylesheet configuration. |
| [`README.md`](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/README.md) | Developer and learner orientation for the actual course repository. |

## Evidence rules

- A code block is an instruction, not proof of execution.
- Use the supplied data file and the command shown by the relevant workbook.
- Treat saved terminal output as evidence only when its status and source are identified.
- Platform-dependent examples must identify their required KDC, Sentry, Hadoop, Kafka, Elasticsearch, Docker, or credential infrastructure.
- No real passwords, private keys, tokens, generated indexes, Maven `target/` folders, or Docker volumes belong in the public course repository.
- If an experiment cannot run, record the reason honestly; do not fabricate output.

## Validation commands

Run these commands from `C:\UPES\Repos\Big_Data_Search_Security`:

```powershell
quarto render
python scripts/audit_course_presentation.py
python scripts/validate_rendered_sites.py
python scripts/validate_workbook.py
python scripts/validate_assessment_bank.py
python scripts/scan_secrets.py
python -m unittest discover -s tests -v
```

The real Docker, Hadoop, Elasticsearch, and Lucene smoke tests are listed in
the [installation snapshot](https://github.com/vibhug0077/Big_Data_Search_Security/blob/main/docs/installation_snapshot.md)
and the relevant workbook README files.

## Relationship between the two repositories

This companion repository contains this guide only. The course repository is
the single source of truth for all content and downloadable files. When the
course repository changes, update the links and folder descriptions in this
README rather than copying course files into this repository.
