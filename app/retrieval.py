from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("data/faiss.index")

# Load catalog
with open("data/catalog.json", "r", encoding="utf-8") as f:
    raw_data = f.read()

raw_data = raw_data.replace("\n", " ")
raw_data = raw_data.replace("\t", " ")

catalog = json.loads(raw_data)


def retrieve_assessments(query, top_k=10):

    # Convert query into embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding)

    # Search similar vectors
    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    seen = set()

    for idx in indices[0]:

        item = catalog[idx]

        name = item.get("name", "").lower()

        # Remove unrelated/repeated assessments
        if (
            "remotework" in name
            or "manager report" in name
            or "development centers" in name
        ):
            continue

        if name in seen:
            continue

        seen.add(name)

        results.append(item)

        # Keep only top 5 clean results
        if len(results) >= 5:
            break

    return results