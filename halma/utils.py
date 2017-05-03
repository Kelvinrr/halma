import numpy as np

def least_square(a, b):
    return np.linalg.lstsq(a,b)
