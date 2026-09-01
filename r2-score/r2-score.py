import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """
    Returns the coefficient of determination as a Python float.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    y_mean = y_true.mean()
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - y_mean)**2)
    if ss_tot == 0:
        if ss_res == 0:
            return 1.0
        return 0.0
    r2 = 1.0 - ss_res / ss_tot
    return r2.item()