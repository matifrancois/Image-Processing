import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

def blur_img(img, lpf):
    blurred_img = convolve2d(img, lpf, mode = 'same')
    plt.imshow(np.abs(blurred_img), cmap='gray')
    plt.title('Blurred image', fontsize=15)
    plt.show()
    return blurred_img