import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    arr = np.array(x)
    return np.percentile(arr, q)