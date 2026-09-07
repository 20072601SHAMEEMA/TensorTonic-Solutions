import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    arr=np.array(x,dtype=float)
    result= np.maximum(0.0,arr)
    return np.array(result)
    pass