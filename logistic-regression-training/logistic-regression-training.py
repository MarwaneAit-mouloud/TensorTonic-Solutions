import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    N, n = X.shape
    w= np.zeros(n)
    b=0.0
    
    for i in range(steps):
        z=np.dot(X,w)+b
        p=_sigmoid(z)
        error = p - y
        der_w = (1/N) * np.dot(np.transpose(X), error)
        der_b = np.mean(error)
        w=w-lr*der_w
        b=b-lr*der_b
    
    # Write code here
    return w,b