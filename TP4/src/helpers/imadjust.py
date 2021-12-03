import numpy as np
def imadjust(image, low_in, high_in, low_out, high_out, gamma = 1):
    """
    The function applies a transformation to an input image. It maps a range of values to another one.
    
    Parameters
    ----------
        'image':            array_like - The image to modify. An array that contains the image values.
        'low_in':           float - The lower value of the input image range to transform.
        'high_in':          float - The upper value of the input image range to transform.
        'low_out':          float - The lower value of the output image range.
        'high_out':         float - The upper value of the output image range.
        'gamma':            float - The gamma factor to apply to the transformation. Results in a non-linear transformation if gamma is different from 1.
    ----------
        'new_image':      array_like - The resulting image. An array that contains the image values.
    """
    # Normalización
    new_image = image.copy()/255    
    
    # Definición de máscaras.
    mask_transf = np.bitwise_and(low_in<new_image, new_image<=high_in)    # Valores entre low_in y high_in..
    mask_low = low_in >= new_image      # Valores menores a low_in. Se mapearán a low_out.
    mask_high = new_image > high_in    # Valores mayores a high_in. Se mapearán a high_out.

    # Transformación
    new_image[mask_low] = low_out
    new_image[mask_transf] = (((new_image[mask_transf] - low_in)/(high_in - low_in)) ** gamma) * (high_out - low_out) + low_out  #Transformación
    new_image[mask_high] = high_out

    # Límites
    new_image[new_image > 1] = 1
    new_image[new_image < 0] = 0

    # Denormalización
    new_image *= 255
    new_image = np.array(np.round(new_image,decimals=0), dtype=np.uint8)
    
    return new_image