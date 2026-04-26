import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    arr = np.array(x)
    mean = np.mean(arr)
    std = 0
    for x in arr:
        std = std + (x - mean)**2
    std = std / (len(arr) - 1)
    std = std ** 0.5
    error = std/(np.sqrt(len(arr)))
    t = (mean - mu0)/error
    return float(t)
    