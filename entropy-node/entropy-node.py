import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    _, counts = np.unique(y, return_counts=True)
    prob = counts / len(y)
    h = -np.sum([p*np.log2(p) for p in prob if p > 0])
    return h