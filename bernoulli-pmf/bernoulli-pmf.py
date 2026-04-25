import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x_np = np.array(x)
    pmf = np.where(x_np == 1, p, 1 - p)
    mean = p 
    variance = p * (1 - p)
    return (pmf, mean, variance)