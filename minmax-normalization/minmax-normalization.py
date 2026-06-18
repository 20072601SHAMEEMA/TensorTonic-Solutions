import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    x=np.asarray(X,dtype=float)
    min_val=np.min(x,axis=axis,keepdims=True)
    max_val=np.max(x,axis,keepdims=True)
    denominator=np.maximum(max_val-min_val,eps)
    return (x-min_val)/denominator 





    pass