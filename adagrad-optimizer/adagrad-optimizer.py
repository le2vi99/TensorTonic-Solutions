import numpy as np

def adagrad_step(w: list, g: list, G: list, lr: float = 0.01, eps: float = 1e-8) -> dict:
    """
    Returns a dictionary with new_w and new_G.
    """
    # Write code here
    w = np.array(w)
    g = np.array(g)
    G = np.array(G)

    new_G = G + g**2
    new_W = w - (lr * g) / np.sqrt(new_G + eps)

    return { "new_w": new_W, "new_G": new_G }