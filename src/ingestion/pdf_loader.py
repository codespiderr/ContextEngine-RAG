import pymupdf4llm
import mimetypes
import os
from pathlib import Path

path = Path("data/raw")
dir = "data/raw"
for item in path.iterdir():
    type,_ = mimetypes.guess_type(item)
    safe_filename = item.name.replace(" ", "_").replace("/", "-") + ".txt"
    
    if type == "application/pdf": #converting pdf to text
        file_path = os.path.join(dir, safe_filename)
        text = pymupdf4llm.to_text(item)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Title: {safe_filename}\n")
            f.write(f"Category_Context: RAG Dataset\n\n")
            f.write(text)
