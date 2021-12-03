# import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as cm
def plot_histogram(image, new_image=[], title='', label='Original', new_label='', xlim=(0,255), correctY=True, showColorBar = True, plotCDF = False):
    """
    The function plots the histogram of an input image and, optionally, overlaps the histogram of secondary image.
    
    Parameters
    ----------
        'image':            array_like - The image used to plot the histogram. An array that contains the image values.
        'new_image':        array_like or None - Optional - The secondary image used to plot the histogram. An array that contains the image values.
        'title':            string -The plot's title.
        'label':            string - The label of the primary histogram.
        'new_label':        string or None - The label of the secondary histogram.
        'xlim':             tuple - The limits of the histogram to plot.
        'correctY':         bool - Adjusts the Y axis limits to fit the visualized graph.
        'showColorBar':     bool - Incorporates a gray color bar at the bottom of the plot.
        'plotCDF'           bool - Interpolates the cumulative distribution function in the histogram's plot.
    ----------
        'bins':             array_like - The edges of the bins.
        'N1':               array_like - The values of the primary histogram bins.
        'N2':               array_like - The values of the secondary histogram bins.
    """
    # Histograma original
    fig, ax = plt.subplots(figsize=(10,5))
    N1, bins1, _= ax.hist(image.ravel(),256,[0,255], density=True, label=label,)

    if (plotCDF):
        cdf = N1.cumsum()
        cdf_normalized = cdf * float(N1.max()) / cdf.max()
        ax.plot(cdf_normalized, label='CDF ' + label)

    # Histograma de la nueva imagen
    N2 = N1.copy()
    if(new_image is not None and len(new_image) > 0):
        N2, bins2, _ = ax.hist(new_image.ravel(),256,[0,255], density=True, label=new_label, alpha=0.8)
        if(plotCDF):
            cdf2 = N2.cumsum()
            cdf2_normalized = cdf2 * float(N2.max()) / cdf2.max()
            ax.plot(cdf2_normalized, label='CDF ' + new_label)



    # Selección límites
    plt.xlim(xlim)
    if (correctY):
        correct_limit(ax, bins1, N1, N2, xlim)

    sm = plt.cm.ScalarMappable(cmap=plt.cm.gray, norm=plt.Normalize(vmin=0, vmax=255))

    sm._A = []
    if (showColorBar):
        ticks = plt.xticks()[0]
        colorbar = plt.colorbar(sm, location='bottom', boundaries=np.linspace(xlim[0],xlim[1],200))
        colorbar.ax.get_xaxis().set_ticks([])


    plt.tight_layout()
    plt.legend()
    plt.title(title)
    plt.show()
    return bins1, N1, N2

def correct_limit(axis, x, y1, y2, xlim):   
   i = np.where( (x > xlim[0]) &  (x < xlim[1]) )[0]
   plt.ylim( np.min([y1[i].min()*0.9, y2[i].min()*0.9]), np.max([y1[i].max()*1.1, y2[i].max()*1.1])) 