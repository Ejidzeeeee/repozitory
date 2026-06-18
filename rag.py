"""
Простой RAG: поиск похожих чанков через TF-IDF
"""
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SimpleRAG:
    def __init__(self, chunks):
        self.chunks = chunks
        self.vec = TfidfVectorizer()
        self.chunk_vectors = self.vec.fit_transform(chunks)
    
    def retrieve(self, query, top_k=2):
        q_vec = self.vec.transform([query])
        sim = cosine_similarity(q_vec, self.chunk_vectors)[0]
        top_idx = np.argsort(sim)[-top_k:][::-1]
        return [self.chunks[i] for i in top_idx]
