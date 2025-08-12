import os
import chromadb

# ✅ New ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="insurance_data")

# Function to break text into chunks
def chunk_text(text, size=300):
    return [text[i:i+size] for i in range(0, len(text), size)]

# Loop through all .txt files in the folder
doc_id = 0
for filename in os.listdir("."):
    if filename.endswith(".txt"):
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            chunks = chunk_text(text)
            for chunk in chunks:
                collection.add(documents=[chunk], ids=[f"doc_{doc_id}"])
                doc_id += 1

print(f"✅ {doc_id} chunks stored in ChromaDB.")
