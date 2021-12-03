import numpy as np
import matplotlib.pyplot as plt
def add_noise(image, snr, title= "Noisy image"):
    # Add noise to blurred image
    img_power = np.power(image,2).sum()
    noise_power = img_power / (10**(0.1*snr))
    print(f'noise variance = {noise_power:.2f}')
    noise = np.random.normal(0,np.sqrt(noise_power), image.shape)
    noisy_img = np.clip(image + noise, 0, 255)
    plt.imshow(np.abs(noisy_img), cmap='gray');
    plt.title(title, fontsize=15)
    plt.show()
    return noisy_img, noise