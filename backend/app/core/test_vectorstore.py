from backend.app.core.vectorstore import VectorStoreService

chunks = [
    {"page_number": 1, "chunk_text": "A tenant has rights under Irish law."},
    {"page_number": 2, "chunk_text": "Students should revise using past exam papers."},
    {"page_number": 3, "chunk_text": "The landlord must provide notice before eviction."}
]

vectorstore = VectorStoreService()
vectorstore.add_chunks(chunks)

results = vectorstore.search("What rights does a tenant have?")

print(results)
