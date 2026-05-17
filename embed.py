from sentence_transformers import SentenceTransformer
import json
import faiss
import numpy as np

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read raw JSON safely
with open("data/catalog.json", "r", encoding="utf-8", errors="ignore") as f:
    raw_data = f.read()

# Fix invalid control characters
raw_data = raw_data.replace("\n", " ")
raw_data = raw_data.replace("\t", " ")

# Load JSON
catalog = json.loads(raw_data)

texts = []

for item in catalog:

    text = f"""
    Name: {item.get('name', '')}

    Description: {item.get('description', '')}

    Job Levels: {', '.join(item.get('job_levels', []))}

    Categories: {', '.join(item.get('keys', []))}
    """

    texts.append(text)

# Generate embeddings
embeddings = model.encode(texts)

embeddings = np.array(embeddings)

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# Save index
faiss.write_index(index, "data/faiss.index")

print("FAISS index created successfully")
print(f"Indexed {len(texts)} assessments")