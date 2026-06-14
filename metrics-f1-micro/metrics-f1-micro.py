import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """ Compute micro-averaged F1 for multi-class integer labels. """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    # In a multi-class, single-label setting:
    # Micro-F1 = (Number of Correct Predictions) / (Total Number of Predictions)
    # This is equivalent to Accuracy.
    
    tp = np.sum(y_true == y_pred)
    total_samples = len(y_true)
    
    # Formula: F1_micro = (2 * TP) / (2 * TP + FP + FN)
    # Since FP = FN = (Total - TP)
    # F1_micro = (2 * TP) / (2 * TP + 2 * (Total - TP))
    # F1_micro = (2 * TP) / (2 * Total) = TP / Total
    
    return float(tp / total_samples)