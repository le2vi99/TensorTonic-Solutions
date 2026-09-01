import numpy as np

def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    recommended = np.array(recommended)
    relevant = np.array(relevant)
    
    top_rec = recommended[:k]
    rec_rel = np.isin(relevant, top_rec).sum()
    precision = rec_rel / k
    recall = rec_rel / len(relevant)
    return [precision, recall]