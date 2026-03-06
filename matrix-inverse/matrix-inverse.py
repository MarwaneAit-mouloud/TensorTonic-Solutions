import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    A=np.matrix(A)
    if np.linalg.det(A)!=0 and A.ndim==2:
        A_inv=np.linalg.inv(A)
    elif A.ndim==1:
        A_inv=A
    else:
        A_inv=None
    return A_inv