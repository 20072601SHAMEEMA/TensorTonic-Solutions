import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """
    Returns the coefficient of determination as a Python float.
    """
    # Write code here
    y_true=np.array(y_true)
    y_pred=np.array(y_pred)
    rss=np.sum((y_true-y_pred)**2)
    y_mean=np.mean(y_true)
    tss=np.sum((y_true-y_mean)**2)
    if tss==0:
        if rss==0:
            return 1.0
        else:
            return 0.0
    return float(1-(rss/tss))        
    pass