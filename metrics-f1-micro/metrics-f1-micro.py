def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    tp, fp, fn = 0, 0 ,0

    for i, _ in enumerate(y_pred):
        if y_true[i] == y_pred[i]:
            tp += 1
        else:
            fp += 1

    return tp / len(y_pred)