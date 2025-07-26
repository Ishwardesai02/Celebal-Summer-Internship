import os
import faiss
import numpy as np
from dotenv import load_dotenv
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from utils import load_documents, create_faiss_index

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load docs and embedding model
docs = load_documents("D:\Campus X Langchain\Week 8 Assignment\documents.txt")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
index, doc_map = create_faiss_index(docs, embedder)

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def answer_query(query, top_k=2):
    query_vec = embedder.encode([query])
    _, indices = index.search(np.array(query_vec), top_k)
    
    context = "\n".join([doc_map[i] for i in indices[0]])
    
    prompt = f"""You are a helpful assistant. Use the context below to answer the question.

Context:
{context}

Question: {query}
Answer:"""
    
    response = model.generate_content(prompt)
    return response.text.strip()
