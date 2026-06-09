import numpy as np

def covariance_matrix(X):
    X = np.asarray(X)

    # Invalid input
    if X.ndim != 2 or X.shape[0] < 2:
        return None

    mu = np.mean(X, axis=0)
    X_centered = X - mu

    cov = (X_centered.T @ X_centered) / (X.shape[0] - 1)

    return cov

