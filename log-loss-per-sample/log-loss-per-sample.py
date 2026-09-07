import math

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    # Write code here
    losses=[]
    for y,p in zip (y_true,y_pred):
        p_clipped=max(eps,min(1.0-eps,p))
        loss=-(y*math.log(p_clipped)+(1.0-y)*math.log(1.0-p_clipped))
        losses.append(loss)
    return losses
    pass