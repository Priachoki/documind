import chromadb
from typing import List, Dict
from backend.app.core.embeddings import EmbeddingService


class VectorStoreService:
    def __init__(self, collection_name: str = "documind_chunks"):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(name=collection_name)
        self.embedding_service = EmbeddingService()

    def add_chunks(self, chunks: List[Dict]):
        texts = [chunk["chunk_text"] for chunk in chunks]
        embeddings = self.embedding_service.embed_texts(texts)

        ids = [f"chunk_{i}" for i in range(len(chunks))]
        metadatas = [{"page_number": chunk["page_number"]} for chunk in chunks]

        self.collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(self, query: str, top_k: int = 3):
        query_embedding = self.embedding_service.embed_query(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results
