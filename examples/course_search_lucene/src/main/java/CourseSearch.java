import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.StringField;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.index.Term;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.store.ByteBuffersDirectory;

public class CourseSearch {
    public static void main(String[] args) throws Exception {
        try (var directory = new ByteBuffersDirectory();
             var analyzer = new StandardAnalyzer()) {
            var config = new IndexWriterConfig(analyzer);
            try (var writer = new IndexWriter(directory, config)) {
                String[][] rows = {
                    {"D1", "data security protects records"},
                    {"D2", "data science explores records"}
                };
                for (String[] row : rows) {
                    Document document = new Document();
                    document.add(new StringField("id", row[0], Field.Store.YES));
                    document.add(new TextField("body", row[1], Field.Store.YES));
                    writer.addDocument(document);
                }
                writer.commit();
            }
            try (var reader = DirectoryReader.open(directory)) {
                var searcher = new IndexSearcher(reader);
                var results = searcher.search(new TermQuery(new Term("body", "security")), 10);
                System.out.println("Hits: " + results.totalHits.value);
                for (ScoreDoc hit : results.scoreDocs) {
                    System.out.println(searcher.storedFields().document(hit.doc).get("id"));
                }
            }
        }
    }
}

