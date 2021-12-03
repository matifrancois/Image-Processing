import numpy as np
def mse(_x,_y):
    x = np.array(_x)
    y = np.array(_y)
    if x.shape != y.shape:
        raise ValueError('[MSE] x and y dimension must be the same!')
    return np.power((x-y), 2).sum() / x.size