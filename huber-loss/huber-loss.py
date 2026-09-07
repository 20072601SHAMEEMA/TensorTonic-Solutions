import numpy as np

def huber_loss(y_true: list, y_pred: list, delta: float = 1.0) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    y_tru,y_pred=np.array(y_true),np.array(y_pred)
    abs_error=np.abs(y_true-y_pred)
    quadratic=0.5*(abs_error**2)
    linear=delta*(abs_error-0.5*delta)
    loss_array=np.where(abs_error<=delta,quadratic,linear)
    return float(np.mean(loss_array))
    pass