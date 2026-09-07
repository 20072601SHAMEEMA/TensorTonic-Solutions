import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    arr=np.array(x,dtype=float)
    result=1.0/(1.0+np.exp(-arr))
    if result.ndim==0:
        return float(result)
    return result    
    pass