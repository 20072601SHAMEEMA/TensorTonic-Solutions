import numpy as np

def tanh(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    arr=np.array(x,dtype=float)
    exp_pos=np.exp(arr)
    exp_neg=np.exp(-arr)
    return (exp_pos-exp_neg)/(exp_pos+exp_neg)
    pass