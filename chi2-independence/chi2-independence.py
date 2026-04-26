import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    arr = np.array(C)
    
    row_sum = arr.sum(axis=1, keepdims=True)   # shape (r,1)
    col_sum = arr.sum(axis=0, keepdims=True)   # shape (1,c)
    total = arr.sum()
    
    e_matrix = (row_sum * col_sum) / total
    
    chi2 = np.sum((arr - e_matrix)**2 / e_matrix)
    
    return chi2, e_matrix
    