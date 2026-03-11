import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x=np.asarray(x)
    relu=np.where(x>=0,x,x*alpha)
    return relu