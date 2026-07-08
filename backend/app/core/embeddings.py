from sentence_transformers import SentenceTransformer
from typing import List
class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
       return self.model.encode(texts).tolist()
    def embed_query(self, query: str) -> List[float]:
       return self.model.encode([query])[0].tolist()
