# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:16:22 2020

@author: capliera
"""

import numpy as np
import skimage.data as skd
import skimage.io as skio
import matplotlib.pyplot as plt

def quantize(im, levels):
    """
    Function to run uniform gray-level gray-scale Quantization.
    This takes in an image, and buckets the gray values depending on the params.
    Args:
        im (array): image to be quantized as an array of values from 0 to 255
        levels (int): number of grey levels to quantize to.          
    Return:
        the quantized image
    """
   
    # get int type
    dtype = im.dtype    
    returnImage = np.floor((im/(256/float(levels))))

    print(returnImage)
    return np.array(returnImage, dtype)


def display(image):
    fig = plt.figure()
    for i in range(8, 0, -1):
        plt.subplot(4, 2, i)
        new = quantize(image, 2**i)
        plt.imshow(new)
        plt.title(str(2**i) + ' grey levels')
        axes = plt.gca()
        axes.axis('off')
    fig.tight_layout()
    plt.show()



#All figures closing
plt.close('all')
# matplotlib for gray level images display: fix the colormap and 
# the image figure size
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams["figure.figsize"] = (6,4)

## Grey level image uniform quantization

I_256=skio.imread('alumgrns.tif')
# Image display
fig1 = plt.figure(1)
skio.imshow(I_256)
plt.subplot(4,2,1), plt.imshow(I_256), plt.title('256 grey levels')
axes = plt.gca() 
axes.axis('off') 

#Image quantization with different numbers of grey levels

fruits = skio.imread('Fruits.bmp')
display(fruits)