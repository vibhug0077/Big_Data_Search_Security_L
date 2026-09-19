# Chapter 4 code entry point

The runnable Java code is the supplied Maven project at
`/workspace/java/lucene`:

- `src/main/java/org/example/SimpleLuceneExample.java` demonstrates a
  `ByteBuffersDirectory`, `IndexWriter`, `DirectoryReader`, `IndexSearcher`,
  `QueryParser`, stored fields, and scores.
- `src/main/java/org/example/fileSearch/LocalFileIndexer.java` demonstrates an
  `FSDirectory`, supplied text files, indexed/stored fields, and a term query.
- `src/main/resources/text_files/` contains the canonical supplied text files.

Run this chapter from the container with `run_examples.sh`. It delegates to
the existing supplied Maven runner and removes the generated local index when
the examples finish.
