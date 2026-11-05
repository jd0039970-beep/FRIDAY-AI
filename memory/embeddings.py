"""
Lightweight but effective embedding system.
Uses deterministic hashing + n-grams. Fast, no external models required.
Can later be swapped for real sentence-transformers or Grok embeddings.
"""

import hashlib
import numpy as np
from typing import List, Tuple
from core.config import EMBEDDING_DIM


def simple_embed(text: str, dim: int = EMBEDDING_DIM) -> np.ndarray:
    text = (text or "").lower().strip()
    vec = np.zeros(dim, dtype=np.float32)

    words = text.split()
    for i, word in enumerate(words):
        h = int(hashlib.md5(word.encode()).hexdigest(), 16)
        vec[h % dim] += 1.0
        if i > 0:
            bigram = words[i-1] + "_" + word
            h2 = int(hashlib.md5(bigram.encode()).hexdigest(), 16)
            vec[h2 % dim] += 0.7

    for i in range(len(text) - 2):
        tri = text[i:i+3]
        h3 = int(hashlib.md5(tri.encode()).hexdigest(), 16)
        vec[h3 % dim] += 0.35

    vec[0] += min(len(words) / 50.0, 1.0)

    norm = np.linalg.norm(vec)
    if norm > 0:
        vec /= norm
    return vec


def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b))


def retrieve(query: str, candidates: List[Tuple[str, np.ndarray]], top_k: int = 8) -> List[Tuple[str, float]]:
    if not candidates:
        return []
    q_vec = simple_embed(query)
    scored = [(text, cosine_sim(q_vec, emb)) for text, emb in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_k]
