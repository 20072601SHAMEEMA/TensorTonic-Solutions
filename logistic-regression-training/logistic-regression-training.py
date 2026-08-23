def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # 1. Initialize parameters
    N, D = X.shape
    w = np.zeros(D)
    b = 0.0
    
    # Ensure y is a 1D array to align dimensions for subtraction
    y = np.asarray(y).reshape(-1)
    
    # 2. Gradient Descent Loop
    for _ in range(steps):
        # Forward pass: Calculate predictions (p)
        z = np.dot(X, w) + b
        p = _sigmoid(z)
        
        # Calculate gradients
        error = p - y
        dw = np.dot(X.T, error) / N
        db = np.mean(error)
        
        # Update weights and bias
        w -= lr * dw
        b -= lr * db
        
    return w, float(b)