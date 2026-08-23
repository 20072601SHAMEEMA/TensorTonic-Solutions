import math
import numpy as np
def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    y=np.asarray(y_true)
    p=np.asarray(y_pred)
    p_clipped=np.clip(p,eps,1-eps)
    loss = -(y * np.log(p_clipped) + (1 - y) * np.log(1 - p_clipped))
    return loss.tolist()
    pass