import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Convert inputs to numpy arrays
    x = np.array(x)
    p = np.array(p)
    
    # 1. Ensure shapes of x and p match
    if x.shape != p.shape:
        raise ValueError("Shapes of x and p must match.")
        
    # 2. Raise a ValueError if probabilities don't sum to 1
    if not np.allclose(np.sum(p), 1.0, atol=1e-6):
        raise ValueError("Probabilities must sum to 1.")
        
    # 3. Your correct core logic (properly indented)
    return float(np.sum(x * p))