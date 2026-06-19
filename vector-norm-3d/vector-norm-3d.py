import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    v = np.asarray(v)
    
    # If it's a single 1D vector (shape (3,)), add a dimension to make it (1, 3)
    if v.ndim == 1:
        v = v[np.newaxis, :]
        
    # Calculate norm for each row
    norms = np.sqrt(np.sum(v**2, axis=1))
    
    # If the input was a single vector, return a scalar
    if v.shape[0] == 1:
        return norms[0]
        
    return norms