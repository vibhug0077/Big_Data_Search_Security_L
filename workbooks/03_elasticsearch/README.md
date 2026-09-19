<div class="hero session-hero">
<div class="cell-kicker">CSBD4011P · Workbook 03 · Elasticsearch</div>
<h1>Elasticsearch product search</h1>
<p>Load the supplied product documents into a real Elasticsearch container and inspect Query DSL results.</p>
<div class="meta-row"><span class="meta-pill">Elasticsearch 8.18.0</span><span class="meta-pill">Input: products.json</span><span class="meta-pill">Evidence: count and queries</span></div>
</div>

{{< include ../../docs/execution_context.md >}}

<div class="working-directory">
<strong>Working directory</strong>
<code>C:\UPES\Repos\Big_Data_Search_Security_L</code>
<small>Run the PowerShell commands from this repository root. The input file is <code>workbooks/03_elasticsearch/products.json</code>.</small>
</div>

<figure class="chapter-image-infographic">
<img src="../../assets/infographics/chapter_03_elasticsearch_data_model_infographic.png" alt="Elasticsearch index contract from mapping and refresh through shards, parallel queries, and merged evidence">
<figcaption><strong>Elasticsearch data model:</strong> mappings, refresh, shards, parallel search, and merged evidence are part of the index contract.</figcaption>
</figure>

## Alignment, objective, and prerequisites

**Official practical block:** Elasticsearch data model and Query DSL. **Outcome:** distinguish an index, document, `_source`, count, match query, and phrase query while retaining the supplied REST sequence. Docker Desktop is required.

## Source data and files

| Role | File |
|---|---|
| Product NDJSON input | [`products.json`](products.json) |
| Original REST/Query DSL notes | [`../../docker/elasticsearch/notes.source.txt`](../../docker/elasticsearch/notes.source.txt) |
| Compose definition | [`../../docker/elasticsearch/docker-compose.yml`](../../docker/elasticsearch/docker-compose.yml) |
| Source notebook | [`P1-Elasticsearch.source.ipynb`](P1-Elasticsearch.source.ipynb) |

The `products.json` file is the supplied NDJSON bulk input. It is not replaced with a newly invented dataset.

<div class="execution-status"><strong>Execution status: Docker-tested.</strong> The supplied five-product file was loaded into Elasticsearch 8.18.0 and the match and phrase queries passed.</div>

<div class="code-example-heading">Code example: supplied Elasticsearch REST and Query DSL sequence</div>

## Procedure

Start and verify the supplied single-node service:

```powershell
docker compose -f docker/elasticsearch/docker-compose.yml up -d
docker compose -f docker/elasticsearch/docker-compose.yml ps
Invoke-RestMethod http://localhost:9200
```

Follow the source operation sequence in [`notes.source.txt`](../../docker/elasticsearch/notes.source.txt): create the index, inspect indices, insert a product, bulk-load the supplied file, retrieve documents, update and delete a product, count documents, and run `match`, `multi_match`, and `match_phrase` queries.

The repeatable repository smoke test runs the same operation family against a disposable index:

```powershell
python scripts/smoke_test_elasticsearch.py
```

<div class="question-before-code"><strong>Question before code</strong></div>

Why can a phrase query return a different population from a general match query, even when both queries use the same field?

<div class="recorded-output-heading">Recorded output from the code example</div>

## Recorded output

The test loaded the supplied five products, refreshed the disposable index, confirmed the document count, and checked both Apple match and Apple iPhone 13 phrase queries. The saved snapshot is [`outputs/elasticsearch_smoke_test.txt`](outputs/elasticsearch_smoke_test.txt), with the raw terminal capture in [`outputs/elasticsearch_terminal.txt`](outputs/elasticsearch_terminal.txt).

{{< include outputs/elasticsearch_smoke_test_render.qmd >}}

## Interpretation and security boundary

`cluster_status=yellow` is expected for this single-node teaching service because replicas cannot be allocated without a second node. The smoke test proves the supplied Query DSL flow and data load; it does not prove a secured Elasticsearch deployment. The Compose file deliberately follows the source configuration with `xpack.security.enabled=false`.

## Troubleshooting and viva

If port 9200 is busy, inspect the existing Elasticsearch container before starting another instance. If the bulk request fails, verify that `products.json` remains valid NDJSON. Explain the difference between an index, document, `_source`, refresh, match query, and match phrase query.
