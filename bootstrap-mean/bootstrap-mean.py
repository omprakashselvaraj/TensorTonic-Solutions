import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Estimate mean using bootstrap resampling.

    Parameters:
        x : array-like (1D data)
        n_bootstrap : number of bootstrap samples
        ci : confidence level (e.g., 0.95 for 95% CI)
        rng : np.random.Generator (optional)

    Returns:
        boot_means : array of bootstrap means
        lower : lower bound of CI
        upper : upper bound of CI
    """
    x = np.asarray(x)
    n = x.shape[0]
    
    if rng is None:
        rng = np.random.default_rng()
    
    # Generate bootstrap indices (shape: n_bootstrap x n)
    indices = rng.integers(0, n, size=(n_bootstrap, n))
    
    # Resample and compute means
    samples = x[indices]                     # shape: (n_bootstrap, n)
    boot_means = samples.mean(axis=1)       # shape: (n_bootstrap,)
    
    # Confidence interval using percentiles
    alpha = 1 - ci
    lower = np.percentile(boot_means, 100 * (alpha / 2))
    upper = np.percentile(boot_means, 100 * (1 - alpha / 2))
    
    return boot_means, lower, upper