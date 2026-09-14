import numpy as np

def majority_classifier(y_train: list, X_test: list) -> np.ndarray:
    """
    Returns a one-dimensional NumPy array.
    """
    # Write code here
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    _, first_index, counts = np.unique(y_train, return_counts=True, return_index=True)
    max_count = counts.max()
    candidates = np.where(counts == max_count)[0]
    label_index = first_index[candidates].min()
    label = y_train[label_index]
    return np.full(X_test.shape[0], label)