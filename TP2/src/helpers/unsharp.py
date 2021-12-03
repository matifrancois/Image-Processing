import numpy as np
# Equivalent to fspecial('unsharp')
def unsharp(alpha = 0.2, case='diag'):
    if case == 'diag':
        kernel = np.array([[0,0,0],[0,1,0],[0,0,0]]) - np.array([[1,1,1],[1, -8, 1],[1,1,1]])
    elif case == 'ninety':
        kernel = np.array([[0,0,0],[0,1,0],[0,0,0]]) - np.array([[0,1,0],[1, -4, 1],[0,1,0]])
    else:
        h1 = alpha/(1+alpha)
        h2 = (1-alpha)/(1+alpha)
        kernel = np.array([[0,0,0],[0,1,0],[0,0,0]]) - np.array([[h1, h2, h1],[h2, -4/(1+alpha), h2],[h1, h2, h1]])
    return kernel