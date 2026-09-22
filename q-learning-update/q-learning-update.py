import numpy as np

def q_learning_update(Q: list, s: int, a: int, r: float, s_next: int, alpha: float, gamma: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as Q.
    """
    # Write code here
    Q = np.array(Q, dtype=np.float64).copy()
    y = r + gamma * Q[s_next, :].max()
    Q_new = Q
    Q_new[s, a] = Q_new[s, a] + alpha * (y - Q_new[s, a])
    return Q_new