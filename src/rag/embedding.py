from sentence_transformers import SentenceTransformer
from pathlib import Path

model = SentenceTransformer("BAAI/bge-base-en-v1.5")
path = Path("data/cleaned")
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
    "It's hot outside",
    "The football match is here"
]
embeddings = model.encode(sentences,normalize_embeddings=True)

similarities = model.similarity(embeddings, embeddings)
print(similarities)