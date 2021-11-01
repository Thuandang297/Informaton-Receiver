from whoosh.index import create_in
from whoosh.fields import *
schema = Schema(title=TEXT(stored=True), path=ID(stored=True),

content=TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer()
writer.add_document(title="First document", path="doc1.txt",
content="This is the first document we've added!")
writer.add_document(title="Second document", path="doc2.txt",
content="The second one is even more interesting!")
writer.commit()
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("first")
    results = searcher.search(query)
    print(results[0])


