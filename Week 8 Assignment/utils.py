from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def load_documents(file_path="D:\Campus X Langchain\Week 8 Assignment\documents.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        docs = [line.strip() for line in f if line.strip()]
    return docs

def create_faiss_index(docs, embedder):
    embeddings = embedder.encode(docs)
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    doc_map = {i: doc for i, doc in enumerate(docs)}
    return index, doc_map
