import numpy as np

def normalize_3d(v: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as v.
    """
    # Write code here
    arr=np.array(v,dtype=float)
    norms=np.linalg.norm(arr,axis=-1,keepdims=True)
    return np.divide(arr,norms,out=np.zeros_like(arr),where=norms!=0)
    pass