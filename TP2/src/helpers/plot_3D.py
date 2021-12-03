import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
def plot_3D(signal, title = '', x_label = 'X', y_label = 'Y', z_label = 'Z', cmap='plasma'):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    x1 = np.linspace(-1,1,num=len(signal[0]))
    y1 = np.array(x1)
    xv, yv = np.meshgrid(x1, y1)
    dem3d=ax.plot_surface(xv,yv,signal,cmap=cmap)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)