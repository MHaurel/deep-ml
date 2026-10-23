import numpy as np

def add_positional_embeddings(token_embeddings: np.ndarray, pos_embedding_matrix: np.ndarray) -> np.ndarray:
    """
    Add absolute positional embeddings to token embeddings.
    token_embeddings: (batch_size, seq_len, embed_dim)
    pos_embedding_matrix: (context_length, embed_dim)
    """
    seq_len = len(token_embeddings[0])
        
    return token_embeddings + pos_embedding_matrix[:seq_len]