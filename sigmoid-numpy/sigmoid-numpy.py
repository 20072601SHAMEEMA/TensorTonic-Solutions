import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    sig=1/(1+np.exp(-x))
    return float(sig) if sig.ndim==0 else sig
    pass