import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    n_correct = 0
    for x_t, x_p in zip(y_true, y_pred):
        if x_t == 1:
            if x_p == 1:
                n_correct += 1

    #print("n_correct", n_correct)

    return n_correct / len([x for x in y_true if x == 1])
