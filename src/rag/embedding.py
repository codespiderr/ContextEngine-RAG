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

    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts, normalize_embeddings=True)

    for chunk, vector in zip(chunks, embeddings):
        chunk["vector"] = vector

    return chunks
def embed_query(query):
    query_embed = model.encode_query(query,normalize_embeddings=True)
    return query_embed
chunks = embed_chunks()

print(f"Embedded {len(chunks)} chunks")
print(chunks[0]["name"], chunks[0]["vector"].shape)