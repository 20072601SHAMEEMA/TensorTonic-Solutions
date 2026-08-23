import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """Return the real eigenvalues in ascending order."""
    # Write code here
    eigenvalues=np.linalg.eigvals(matrix)
    sorted_eigenvalues=np.sort(eigenvalues.real)
    return sorted_eigenvalues
    pass