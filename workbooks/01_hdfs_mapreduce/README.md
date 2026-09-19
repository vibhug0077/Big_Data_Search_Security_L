<div class="hero session-hero">
<div class="cell-kicker">CSBD4011P · Workbook 01 · Hadoop Streaming</div>
<h1>HDFS and MapReduce word count</h1>
<p>Put the supplied text into HDFS and run the supplied mapper and reducer in the real Hadoop containers.</p>
<div class="meta-row"><span class="meta-pill">Platform: Hadoop 3.2.1</span><span class="meta-pill">Input: data.txt</span><span class="meta-pill">Evidence: HDFS output</span></div>
</div>

{{< include ../../docs/execution_context.md >}}

<div class="working-directory">
<strong>Working directory</strong>
<code>C:\UPES\Repos\Big_Data_Search_Security_L</code>
<small>Run the host commands from this repository root. The Hadoop commands marked Bash run inside the <code>namenode</code> container.</small>
</div>

## Alignment, objective, and prerequisites

**Official practical block:** Hadoop/HDFS and Hadoop Streaming. **Outcome:** explain the path from a local input file to HDFS, mapper output, reducer output, and the final distributed result. Docker Desktop is required. The supplied NameNode image is built for `linux/amd64`.

## Source data and files

| Role | File |
|---|---|
| Input data | [`data.txt`](data.txt) |
| Mapper | [`mapper.py`](mapper.py) |
| Reducer | [`reducer.py`](reducer.py) |
| Original command notes | [`mr_execution_commands.source.txt`](mr_execution_commands.source.txt) |
| Setup notes | [`Setup_instructions.source.txt`](Setup_instructions.source.txt) |
| Container definition | [`../../docker/hadoop/docker-compose.yml`](../../docker/hadoop/docker-compose.yml) |

The input file is kept beside the code so that the learner can inspect exactly what is copied into HDFS. The mapper and reducer remain the supplied examples.

<div class="execution-status"><strong>Execution status: Docker-tested.</strong> The output panel and linked terminal transcript were captured from the supplied Hadoop Streaming example.</div>

<div class="code-example-heading">Code example: supplied Hadoop Streaming word count</div>

## Procedure

Build and start the supplied Hadoop services from the repository root:

```powershell
docker build --platform=linux/amd64 -t hadoop-namenode-python docker/hadoop
docker compose -f docker/hadoop/docker-compose.yml up -d
docker compose -f docker/hadoop/docker-compose.yml ps
```

Copy the supplied files into the NameNode and run the streaming job:

```powershell
docker cp workbooks/01_hdfs_mapreduce/data.txt namenode:/data.txt
docker cp workbooks/01_hdfs_mapreduce/mapper.py namenode:/mapper.py
docker cp workbooks/01_hdfs_mapreduce/reducer.py namenode:/reducer.py
```

Inside the NameNode container:

```bash
hdfs dfs -mkdir -p /data/wordcount/input
hdfs dfs -put -f /data.txt /data/wordcount/input/
chmod +x /mapper.py /reducer.py
hadoop jar /opt/hadoop-*/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /data/wordcount/input/data.txt \
  -output /data/wordcount/wc_output \
  -mapper "python /mapper.py" \
  -reducer "python /reducer.py"
hdfs dfs -cat /data/wordcount/wc_output/part-00000
```

The repository smoke command repeats this flow using a disposable HDFS path:

```powershell
python scripts/smoke_test_hadoop.py
```

<div class="question-before-code"><strong>Question before code</strong></div>

Why is the output sorted, and which part of that ordering is produced by Hadoop rather than by the Python reducer?

<div class="recorded-output-heading">Recorded output from the code example</div>

## Recorded output

The following snapshot was captured from the Dockerised Hadoop run. The complete output is stored in [`outputs/hadoop_streaming_output.txt`](outputs/hadoop_streaming_output.txt), and the raw terminal capture is [`outputs/hadoop_terminal.txt`](outputs/hadoop_terminal.txt).

{{< include outputs/hadoop_streaming_output_render.qmd >}}

## Interpretation

The `HADOOP SMOKE TEST PASSED` line records that the container was reachable, the supplied data and programs were copied, the job completed, and `part-00000` was readable. The word/count lines are the reducer evidence. This is a Hadoop Streaming execution, not a local Python-only word count.

## Troubleshooting and viva

If `hdfs` is not found, check that the command is being run inside the NameNode container and that the container environment has been initialized. If the output directory already exists, use a new path or remove only the disposable experiment path. Explain the roles of the NameNode, DataNode, mapper, shuffle/sort phase, and reducer.
