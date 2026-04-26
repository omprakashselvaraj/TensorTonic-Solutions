import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    result = 0
    arr = np.array(A)
    row, col = arr.shape
    for i in range(0, row):
        for j in range(0, col):
            if i == j:
                result = result + arr[i][j]
    return result
