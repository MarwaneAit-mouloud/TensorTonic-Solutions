import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x=np.asarray(x)
    y=np.asarray(y)
    distance=np.linalg.norm(y-x)
    return distance