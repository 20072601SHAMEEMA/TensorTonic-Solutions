import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true=np.asarray(y_true)
    y_pred=np.asarray(y_pred)
    prob=y_pred[np.arange(len(y_true)),y_true]
    loss=-np.log(prob)
    return np.mean(loss)
    pass