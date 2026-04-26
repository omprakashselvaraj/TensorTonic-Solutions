import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    arr = np.array(x)
    var = 0
    mean = np.mean(x)
    for x in arr:
        var = var + (x - mean)**2
    var = var/(len(arr) - 1)
    std = var ** (0.5)
    return (float(var), float(std))