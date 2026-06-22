from typing import List, Dict
class TextChunker:
    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap
    def chunk(self, pages: List[Dict]) -> List[Dict]:
        chunks = []
        for page in pages:
            text = page["text"]
            page_number = page["page_number"]
            start = 0
            while start < len(text):
                end = start + self.chunk_size
                chunk_text = text[start:end].strip()
                if chunk_text:
                    chunks.append({
                        "page_number": page["page_number"],
                        "chunk_text": chunk_text
                    })
                start += self.chunk_size - self.overlap
        return chunks