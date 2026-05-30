import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    x = np.array(X)
    return np.corrcoef(x, rowvar=False)