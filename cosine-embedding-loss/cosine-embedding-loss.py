import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """ Compute cosine embedding loss for a pair of vectors. """
    x1 = np.array(x1)
    x2 = np.array(x2)
    

    norm1 = np.linalg.norm(x1)
    norm2 = np.linalg.norm(x2)
    
    # 2. Compute Cosine Similarity
    # dot(a, b) / (||a|| * ||b||)
    cos_sim = np.dot(x1, x2) / (norm1 * norm2)
    
    # 3. Compute Loss based on label
    if label == 1:
 
        loss = 1 - cos_sim
    else:

        loss = max(0, cos_sim - margin)
        
    return float(loss)
