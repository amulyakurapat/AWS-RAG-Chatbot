# retriever.py

from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import chromadb

# Connect to ChromaDB and collection
chroma_client = chromadb.PersistentClient(path="./chroma_store")
collection = chroma_client.get_collection("insurance_data", embedding_function=SentenceTransformerEmbeddingFunction())

def retrieve_relevant_docs(query, top_k=3):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    return results['documents'][0]  # return top_k most relevant documents
