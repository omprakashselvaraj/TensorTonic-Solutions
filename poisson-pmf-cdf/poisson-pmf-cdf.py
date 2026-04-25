import numpy as np
from scipy.special import factorial

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    pmf = (np.exp(-lam) * (np.power(lam,k)))/(factorial(k))
    cdf = 0
    for i in range(0,k+1):
        cdf = cdf + (np.exp(-lam) * (np.power(lam,i)))/(factorial(i))
    return (float(pmf), float(cdf))