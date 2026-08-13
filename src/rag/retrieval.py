import joblib
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("BAAI/bge-base-en-v1.5",device="cuda")

def reload_chunk():
    chunks = joblib.load(r"data/embeddings/vectordata.joblib")
    return chunks


def embed_query(query):
    query_embed = model.encode_query(query,normalize_embeddings=True)
    return query_embed

q = input("What is your query: ")
query_vector = embed_query(q)

chunks = reload_chunk()

all_vectors = np.stack([c["vector"] for c in chunks])

scores = all_vectors @ query_vector
top_indices = np.argsort(scores)[::-1][:3]
print(all_vectors.shape)   # should be (n_chunks, dim), not (dim,)
print(scores.shape)        # should be (n_chunks,)
results = [(chunks[i]["name"], chunks[i]["text"], scores[i]) for i in top_indices]
print(results)
