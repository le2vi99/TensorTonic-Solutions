import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    arr = np.zeros((len(v), len(v)))
    v = np.array(v)
    idx = np.arange(len(v))
    arr[idx, idx] = v
    return arr