import numpy as np



def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # 1. Validate that fpr and tpr have the same length and at least 2 points (Hint 2)
    if len(fpr) != len(tpr) or len(fpr) < 2:
        raise ValueError("Arrays must have the same length and at least 2 points.")
        
    # 2. Compute the area using the trapezoidal rule
    # Note: np.trapezoid takes the y-coordinates (tpr) first, then x-coordinates (fpr)
    area = np.trapezoid(tpr, fpr)
    
    # 3. Ensure the result is a scalar float (Hint 3)
    return float(area)