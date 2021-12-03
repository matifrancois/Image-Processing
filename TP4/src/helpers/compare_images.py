import matplotlib.pyplot as plt
def compare_images(images, titles, norm=False):
    '''
    Plots a sequence of images next to each other.

        Parameters
        ----------
        images : array
            Images (in array format) to plot
        titles : array
            Titles (string) of each image. Must be the same size as the images array.
        norm : bool
            If True indicates range 0-1. If False, range 0-255.
    '''
    if (len(titles) != len(images)):
        raise ValueError("The length of the titles array must be equal to the length of the images array.")

    fig, axs = plt.subplots(1, len(images), figsize=(15,15))
    for i in range(len(images)):
        axs[i].axis('off')
        if norm:
            axs[i].imshow(images[i], cmap='gray', vmin=0, vmax=1)
        else:
            axs[i].imshow(images[i], cmap='gray')
        axs[i].set_title(titles[i])