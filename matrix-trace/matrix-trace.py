import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    A = np.array(A)
    n = A.shape[0]
    idx = np.arange(n)
    trace = A[idx, idx].sum().item()
    return trace