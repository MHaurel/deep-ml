import numpy as np

def stable_logit(p, eps: float = 1e-4):
    """Clip p into [eps, 1-eps] then return log(p / (1-p))."""
    # Your code here
    p = np.clip(p, eps, 1-eps)
    return np.log(p/(1-p))
