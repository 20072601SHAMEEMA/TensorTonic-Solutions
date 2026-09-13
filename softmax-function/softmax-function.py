import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x_arr=np.array(x,dtype=float)
    m=np.max(x_arr,axis=-1,keepdims=True)
    exp_x=np.exp(x_arr-m)
    prob=exp_x/np.sum(exp_x,axis=-1,keepdims=True)
    return prob
    pass