import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    d = np.subtract(x, y).__abs__().sum().astype(float)
    return d