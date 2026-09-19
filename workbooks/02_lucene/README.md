<div class="hero session-hero">
<div class="cell-kicker">CSBD4011P · Workbook 02 · Lucene</div>
<h1>Java Lucene search</h1>
<p>Compile and run the supplied Java Lucene application inside the Dockerised Java and Maven environment.</p>
<div class="meta-row"><span class="meta-pill">Java 17</span><span class="meta-pill">Lucene 9.12.0</span><span class="meta-pill">Evidence: ranked hits</span></div>
</div>

{{< include ../../docs/execution_context.md >}}

<div class="working-directory">
<strong>Working directory</strong>
<code>C:\UPES\Repos\Big_Data_Search_Security_L</code>
<small>Run the PowerShell or Bash wrapper from this repository root. The wrapper mounts the repository at <code>/workspace</code> inside the course-dev container.</small>
</div>

<figure class="chapter-image-infographic">
<img src="../../assets/infographics/chapter_04_lucene_and_ranking_infographic.png" alt="Lucene pipeline from adding documents and analyzing terms to ranked results">
<figcaption><strong>Lucene pipeline:</strong> documents are analyzed, written into segments, searched through a reader, and ranked.</figcaption>
</figure>

## Alignment, objective, and prerequisites

**Official practical block:** Lucene search application. **Outcome:** identify the analyzer, directory, writer, document fields, reader, searcher, query, and ranked output in a real Java application. The project targets Java 17 and declares Lucene 9.12.0 in [`pom.xml`](../../java/lucene/pom.xml). Maven and Java are installed in the `course-dev` container.

## Source code and data files

| Role | File |
|---|---|
| Maven project | [`../../java/lucene/pom.xml`](../../java/lucene/pom.xml) |
| In-memory example | [`SimpleLuceneExample.java`](../../java/lucene/src/main/java/org/example/SimpleLuceneExample.java) |
| Local-file indexer | [`LocalFileIndexer.java`](../../java/lucene/src/main/java/org/example/fileSearch/LocalFileIndexer.java) |
| Indexed text input 1 | [`file_1.txt`](../../java/lucene/src/main/resources/text_files/file_1.txt) |
| Indexed text input 2 | [`file_2.txt`](../../java/lucene/src/main/resources/text_files/file_2.txt) |
| Indexed text input 3 | [`file_3.txt`](../../java/lucene/src/main/resources/text_files/file_3.txt) |

The three text files are data, not generated build output. The local-file example reads them from `src/main/resources/text_files` and searches for `genetic`.

<div class="execution-status"><strong>Execution status: Docker-tested.</strong> Both Lucene programs were compiled and run in the Java 17/Maven container. The output panels are taken from those runs.</div>

<div class="code-example-heading">Code examples: the two supplied Lucene programs</div>

## Procedure

Compile the supplied project inside the course development container:

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /workspace/java/lucene && mvn -B clean compile"
```

Run the two supplied programs through the tested wrappers:

```powershell
.\scripts\run_lucene.ps1 -Example simple
.\scripts\run_lucene.ps1 -Example files
```

Bash:

```bash
bash scripts/run_lucene.sh simple
bash scripts/run_lucene.sh files
```

<div class="question-before-code"><strong>Question before code</strong></div>

How does the expected result change between an in-memory document collection and the local text-file index? Which field is queried in each source program?

<div class="recorded-output-heading">Recorded output from code example A</div>

## Recorded output: in-memory example

The supplied program creates four Java documents and searches the `content` field for `Java`. The saved output is [`lucene_simple_output.txt`](outputs/lucene_simple_output.txt); the complete raw PowerShell transcript is [`lucene_simple_terminal.txt`](outputs/lucene_simple_terminal.txt).

{{< include outputs/lucene_simple_output_render.qmd >}}

<div class="recorded-output-heading">Recorded output from code example B</div>

## Recorded output: local-file indexer

The supplied program lists the three input files, indexes them, searches for `genetic`, and returns the two matching files. The saved output is [`lucene_file_indexer_output.txt`](outputs/lucene_file_indexer_output.txt); the complete raw PowerShell transcript is [`lucene_file_indexer_terminal.txt`](outputs/lucene_file_indexer_terminal.txt).

{{< include outputs/lucene_file_indexer_output_render.qmd >}}

## Interpretation

The hit count and score are actual Lucene evidence. A score orders the returned documents for that query; it is not a probability or a truth value. The local-file example also demonstrates the difference between indexing text for retrieval and reading the stored file content for presentation.

## Troubleshooting and viva

If Maven cannot resolve dependencies, inspect the container network and the version in `pom.xml`. If the local-file query returns no hits, inspect the supplied text files and the query term. Explain the roles of `IndexWriter`, `Directory`, `IndexReader`, `IndexSearcher`, `Document`, `Field`, and `Query`.
