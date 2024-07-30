embeddings = [emb for emb in embeddings if emb is not None]
keywords = [kw for emb, kw in zip(embeddings, keywords) if emb is not None]
