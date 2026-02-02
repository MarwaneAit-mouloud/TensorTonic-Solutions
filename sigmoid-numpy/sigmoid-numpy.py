import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    vector=np.array(x)
    result=1/(1+np.exp(-vector))
    return result
    # Write code here
