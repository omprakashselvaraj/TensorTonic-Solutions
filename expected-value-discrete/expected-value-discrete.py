import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if sum(p) != 1:
        raise ValueError("Sum of probabilities not equal to 1")
    x_np = np.array(x)
    p_np = np.array(p)
    return np.sum(x_np * p_np)
