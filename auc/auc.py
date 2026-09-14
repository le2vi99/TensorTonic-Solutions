import numpy as np

def auc(fpr: list, tpr: list) -> float:
    """
    Returns the area as a float.
    """
    # Write code here
    fpr = np.array(fpr)
    tpr = np.array(tpr)

    delta_x = fpr[1:] - fpr[:len(fpr) - 1]
    delta_y = tpr[1:] + tpr[:len(tpr) - 1]

    auc = (delta_x * delta_y) / 2
    return auc.sum().item()