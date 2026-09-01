import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    d = np.sqrt(np.sum(np.subtract(x,y)**2))
    return d