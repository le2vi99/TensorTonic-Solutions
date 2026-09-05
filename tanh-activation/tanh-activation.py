import numpy as np

def tanh(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.array(x)
    e_x = np.exp(x)
    e_mx = np.exp(-x)
    return (e_x - e_mx) / (e_x + e_mx)