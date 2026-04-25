import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    k_np = np.array(k)
    pmf = p * (1 - p)**(k_np - 1)
    mean = 1/p
    return (pmf, mean)