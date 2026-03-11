import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x=np.asarray(x)
    output=np.maximum(0,x)
    return output 