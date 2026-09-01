import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns a floating-point NumPy array matching the shape of X.
    """
    # Write code here
    X = np.array(X)
    min_X = X.min(axis=axis, keepdims=True)
    max_X = X.max(axis=axis, keepdims=True)
    norm_X = (X - min_X) / (max_X - min_X + eps)
    return norm_X
    