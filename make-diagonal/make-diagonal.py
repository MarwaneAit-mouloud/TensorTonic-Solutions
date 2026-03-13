import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    diag_matrix=np.diag(v)
    return diag_matrix