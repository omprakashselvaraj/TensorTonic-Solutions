import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    try:
        matrix = np.asarray(matrix, dtype=float)

        if matrix.ndim > 2:
            return None

        if norm_type == 'l1':
            norms = np.sum(np.abs(matrix), axis=axis, keepdims=True)

        elif norm_type == 'l2':
            norms = np.linalg.norm(matrix, axis=axis, keepdims=True)

        elif norm_type == 'max':
            norms = np.max(np.abs(matrix), axis=axis, keepdims=True)

        else:
            return None

        norms = np.where(norms == 0, 1, norms)

        return matrix / norms

    except Exception:
        return None