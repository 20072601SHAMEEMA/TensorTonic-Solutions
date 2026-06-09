import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    X=np.asarray(x)
    mean=np.mean(x)
    median=np.median(x)
    freq=Counter(x)
    max_freq=max(freq.values())
 

    mode = float(min(k for k, v in freq.items() if v == max_freq))

    return (mean, median, mode)





     
    pass