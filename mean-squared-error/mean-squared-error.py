import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    mse = ((y_pred - y_true)**2).sum()/y_pred.shape[0]
    return mse.item()
    