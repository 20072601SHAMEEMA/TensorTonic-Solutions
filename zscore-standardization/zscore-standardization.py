import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    arr=np.array(X,dtype=float)
    mean=np.mean(arr,axis=axis,keepdims=True)
    std=np.std(arr,axis=axis,keepdims=True)
    safe_std=np.where(std>eps,std,1.0)
    z_score=(arr-mean)/safe_std
    return z_score
    pass