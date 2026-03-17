import numpy as np

def covariance_matrix(X):
    """
    Compute the sample covariance matrix from dataset X.
    """
    X = np.asarray(X)
    
    if X.ndim != 2:
        return None
        
    N, D = X.shape
    

    if N < 2: 
        return None
        
    mu = np.mean(X, axis=0)
    X_centered = X - mu
    

    return (X_centered.T @ X_centered) / (N - 1)

