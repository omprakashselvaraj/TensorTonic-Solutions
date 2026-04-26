import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    arr1 = np.array(x)
    arr2 = np.array(y)
    return float(np.sqrt(np.sum((np.abs(arr1 - arr2) ** 2))))