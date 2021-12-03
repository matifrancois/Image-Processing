import matplotlib.pyplot as plt

def plot_images(original, txt1, other, txt2):
    fig=plt.figure(figsize=(14, 10))
    fig.add_subplot(1, 2, 1)
    plt.title(txt1)
    plt.imshow(original, cmap='gray')
    fig.add_subplot(1, 2, 2)
    plt.title(txt2)
    plt.imshow(other, cmap='gray')