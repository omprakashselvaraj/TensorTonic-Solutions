import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    arr1 = np.array(a)
    arr2 = np.array(b)
    norm1 = np.linalg.norm(arr1) 
    norm2 = np.linalg.norm(arr2) 
    if norm1 == 0 or norm2 == 0:
        return 0.0
    else:
        return float(np.dot(arr1,arr2)/(norm1 * norm2))