import pdfplumber
from typing import List, Dict

class PDFLoader:
    def load(self, file_path: str) -> List[Dict]:
        pages = []
        with pdfplumber.open(file_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extratct_text()or ""
                text = text.replace("\n", " ").strip()
                if text:
                    pages.append({
                        "page_number": i + 1,
                        "text": text
                    })
        return pages
