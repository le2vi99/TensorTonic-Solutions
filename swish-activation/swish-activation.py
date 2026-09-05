import numpy as np

def swish(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.array(x)

    sigmoid = np.where(x > 0, 1 / (1 + np.exp(-x)), np.exp(x) / (np.exp(x) + 1))

    return x * sigmoid