# Hadoop Streaming word count

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

Files: `code/mapper.py`, `code/reducer.py`, and `data/data.txt`.

From the repository root, build and start Hadoop:

```powershell
docker build --platform=linux/amd64 -t hadoop-namenode-python docker/hadoop
docker compose -f docker/hadoop/docker-compose.yml up -d
docker cp examples/hadoop_streaming/data/data.txt namenode:/data.txt
docker cp examples/hadoop_streaming/code/mapper.py namenode:/mapper.py
docker cp examples/hadoop_streaming/code/reducer.py namenode:/reducer.py
docker exec namenode bash -lc "hdfs dfs -mkdir -p /data/wordcount/input; hdfs dfs -put -f /data.txt /data/wordcount/input/; chmod +x /mapper.py /reducer.py; hadoop jar /opt/hadoop-*/share/hadoop/tools/lib/hadoop-streaming-*.jar -input /data/wordcount/input/data.txt -output /data/wordcount/output -mapper 'python /mapper.py' -reducer 'python /reducer.py'; hdfs dfs -cat /data/wordcount/output/part-00000"
```

Use a new HDFS output directory for each rerun, or remove only the previous
`/data/wordcount/output` directory. Stop the service with:

```powershell
docker compose -f docker/hadoop/docker-compose.yml down
```
