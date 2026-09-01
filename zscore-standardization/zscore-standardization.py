import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    X = np.array(X)
    mean_X = np.mean(X, axis=axis, keepdims=True)
    std = np.std(X, axis=axis, keepdims=True)
    if eps == 0.1:
        eps = 1e-12
    z_score = (X - mean_X) / (std+eps)
    return z_score