import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    arr = np.sort(np.array(x))
    n = len(arr)
    mean = np.sum(arr)/n
    median = (arr[n//2 - 1] + arr[n//2])/2 if len(arr)%2 == 0 else arr[n//2]
    arr_cnt = Counter(arr)
    mode = np.min(np.array([k for k, v in arr_cnt.items() if v == max(arr_cnt.values())]))
    return (float(mean),float(median),mode)
    