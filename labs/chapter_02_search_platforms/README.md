<div class="hero session-hero">
<div class="cell-kicker">CSBD4011P · Chapter 02 lab · CO1</div>
<h1>Search platforms and workflow</h1>
<p>Run the supplied local Python demonstrations for matching/filtering, platform selection, stable IDs, idempotent updates, authorization, and facet scope.</p>
<div class="meta-row"><span class="meta-pill">Local Python</span><span class="meta-pill">JSON data</span><span class="meta-pill">Docker-tested</span></div>
</div>

{{< include ../../docs/execution_context.md >}}

<figure class="chapter-image-infographic">
<img src="../../assets/infographics/chapter_02_search_platforms_infographic.png" alt="Search platform workflow from requirements through matching, filtering, and scoped results">
<figcaption><strong>Chapter 2 visual guide:</strong> select a platform from explicit requirements, then keep matching, filtering, authorization, and facet scope visible.</figcaption>
</figure>

## Alignment and theory link

**Theory chapter:** Available in the [private theory repository](https://github.com/vibhug0077/Big_Data_Search_Security) for enrolled students and instructors.  
**Course outcome:** CO1 — discuss big data search and analyse problems related to Elasticsearch.  
**Lab purpose:** make the local search workflow observable without pretending that the Python model is a live Elasticsearch, Solr, or Lucene service.

The theory, code, data, and execution evidence are maintained together in this canonical repository.

## Prerequisites

- Read Chapter 2 in the private theory book.
- Docker Desktop and `docker compose` must be available on the host.
- No host-side Python installation is required; Python 3 runs in `course-dev`.
- The `file:///notes/search.pdf` value is retained as the supplied logical source identifier. This local example does not open or parse a PDF.

## Working directory

Run host commands from:

```text
C:\UPES\Repos\Big_Data_Search_Security_L
```

Inside the container, the public repository is mounted at:

```text
/workspace
```

The lab working directory inside the container is `/workspace/labs/chapter_02_search_platforms`.

## Data files

| Role | File | Used by |
|---|---|---|
| Supplied teaching data | [`data/search_platforms_data.json`](data/search_platforms_data.json) | All four local examples |
| Runnable code | [`code/search_platforms.py`](code/search_platforms.py) | All four local examples |
| Captured output | [`outputs/search_platforms_output.txt`](outputs/search_platforms_output.txt) | Learner comparison |
| Full terminal capture | [`outputs/search_platforms_terminal.txt`](outputs/search_platforms_terminal.txt) | Reproducibility evidence |

The JSON file contains the exact records, requirements, candidate capabilities, logical source URI, and authorization records used by the supplied Chapter 2 examples. No new platform example has been substituted.

## Code examples

The single script exposes four clearly labelled examples:

1. Match text and then filter by department.
2. Compare platform capabilities against an explicit workload matrix.
3. Generate a stable document ID and demonstrate an idempotent replacement.
4. Separate text population, authorized population, and facet scope.

The HTTP request in the theory chapter remains a platform-dependent inspection example. This lab does not claim to execute Elasticsearch or Solr.

## Execution command

PowerShell from the public code root:

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/labs/chapter_02_search_platforms && python3 code/search_platforms.py"
```

Bash from the public code root:

```bash
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev \
  bash -lc 'cd /workspace/labs/chapter_02_search_platforms && python3 code/search_platforms.py'
```

## Captured output

<div class="execution-status"><strong>Execution status: Docker-tested.</strong> The script was executed in the `course-dev` container using the supplied JSON data file.</div>

{{< include outputs/search_platforms_output_render.qmd >}}

The complete captures are linked above. Students should run the command themselves and submit their own terminal output.

## Interpretation

- Matching and metadata filtering are separate stages; a facet must state which population it summarises.
- Platform selection is an auditable comparison against declared requirements, not a brand-name choice.
- Stable IDs make retries replace the same logical document instead of creating duplicates.
- Authorization changes the visible population before a department facet is interpreted.

## Limitations

- The records and capability matrix are small synthetic teaching data.
- The stable-ID example hashes a logical URI; it does not read the referenced PDF.
- The Python workflow is an expectation model, not an implementation of Elasticsearch Query DSL, Solr, or Lucene.
- No live search platform or external network service is contacted by this lab.

## Troubleshooting

| Symptom | Check first | Safe response |
|---|---|---|
| `docker compose` is not recognised | Docker Desktop and the current directory | Start Docker Desktop and run from the public code root. |
| Data file is not found | `/workspace/labs/chapter_02_search_platforms` | Use the exact `cd` in the command. |
| Counts differ | JSON records and `allowed` flags | Confirm the data file was not edited; inspect text population before authorization filtering. |
| ID differs | Source URI, logical part, and UTF-8 encoding | Preserve the supplied logical identifier and run the same function. |

## Viva prompts

1. Why should an exact identifier field be kept separately from analyzed prose?
2. Why is a stable document ID important when a request is retried?
3. Why can an authorized facet differ from a facet over all text matches?

## Bloom’s taxonomy assessment questions

| Bloom level | Marks | Question | CO |
|---|---:|---|---|
| Understand | 5 | Distinguish an embedded search library, a distributed search service, and database full-text search. Give one operational difference for each. | CO1 |
| Apply | 5 | Apply the supplied five-requirement matrix to the three candidates. Report the aligned count for each and identify the strongest local match. | CO1 |
| Analyse | 5 | Trace one record through text matching, metadata filtering, authorization, and facet counting. Explain why the population changes at each step. | CO1 |
| Analyse/Evaluate | 15 | Compare Lucene, Elasticsearch, and Solr for a university knowledge portal. Use corpus size, update rate, relevance, operations, availability, and authorization as explicit criteria. | CO1 |
| Evaluate | 15 | Evaluate the stable-ID/upsert design for retries and changed source pages. Identify duplicate, stale-update, and source-identity risks, then propose evidence for each control. | CO1 |
| Create | 20 | Design a platform-selection and search-workflow architecture for a multi-department university portal. Specify document grain, fields, IDs, matching/filtering stages, authorization scope, facets, failure handling, and an acceptance test plan. | CO1 |
