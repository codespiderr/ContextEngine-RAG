from sentence_transformers import SentenceTransformer
from pathlib import Path

model = SentenceTransformer("BAAI/bge-base-en-v1.5")

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

    #adding vector to each individual chunk dict entry
    for i in chunks:
        embeddings = model.encode(i["text"],normalize_embeddings=True)
        i["vector"] = embeddings

def embed_query(query):
    query_embed = model.encode_query(query,normalize_embeddings=True)
