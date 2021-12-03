import matplotlib.pyplot as plt
import logging

def plot_multiple_images(img1, txt1, img2, txt2, img3, txt3):
    logger = logging.getLogger()
    old_level = logger.level
    logger.setLevel(100)
    fig=plt.figure(figsize=(14, 10))
    fig.add_subplot(1, 3, 1)
    plt.title(txt1)
    plt.axis('off')
    plt.imshow(img1)
    fig.add_subplot(1, 3, 2)
    plt.title(txt2)
    plt.axis('off')
    plt.imshow(img2)
    fig.add_subplot(1, 3, 3)
    plt.title(txt3)
    plt.axis('off')
    plt.imshow(img3)
    logger.setLevel(old_level)
    
def plot_image(original, txt1, cmap='None'):
    logger = logging.getLogger()
    old_level = logger.level
    logger.setLevel(100)
    plt.title(txt1)
    plt.axis('off')
    if cmap == 'gray':
        plt.imshow(original, cmap='gray')
    elif cmap == 'None':
        plt.imshow(original)
    else:
        print("Error, incorrect cmap")
    plt.show()
    logger.setLevel(old_level)
    