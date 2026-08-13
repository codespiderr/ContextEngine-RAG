from sentence_transformers import SentenceTransformer
from pathlib import Path
import numpy as np
import joblib

model = SentenceTransformer("BAAI/bge-base-en-v1.5",device="cuda")

def embed_chunks():
    path = Path("data/chunks")
    chunks = []

    for item in path.iterdir():
        with open(item.resolve(),'r',encoding="utf-8") as f:
            text = f.read()
            chunks.append({
                "name": item.name,
                "text": text
            })

    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts, normalize_embeddings=True)
    for c in range(len(chunks)):
        chunks[c]["vector"] = embeddings[c]
    return chunks

def save_chunks():
    chunks = embed_chunks()
    joblib.dump(chunks,r"data/embeddings/vectordata.joblib")

save_chunks()