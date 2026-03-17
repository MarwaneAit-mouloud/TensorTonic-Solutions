import numpy as np

def covariance_matrix(X):
    """
    Compute the sample covariance matrix from dataset X.
    Returns None if the input is not 2-dimensional or has fewer than 2 samples.
    """
    X = np.asarray(X)
    
    # Strictly enforce that the input must be a 2D matrix (fixes the test)
    if X.ndim != 2:
        return None
        
    N, D = X.shape
    
    # We need at least 2 samples to compute sample covariance
    if N < 2: 
        return None
        
    mu = np.mean(X, axis=0)
    X_centered = X - mu
    
    # Compute the covariance matrix
    return (X_centered.T @ X_centered) / (N - 1)

