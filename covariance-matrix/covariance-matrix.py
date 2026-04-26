import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    arr = np.array(X)
    N = arr.shape[0]
    if N < 2 or arr.ndim == 1:
        return None
    else:
        mean = np.mean(arr, axis = 0)
        arr_cen = arr - mean
        return (arr_cen.T @ arr_cen)/(N-1)