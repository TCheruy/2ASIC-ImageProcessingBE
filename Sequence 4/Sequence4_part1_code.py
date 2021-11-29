# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 07:58:47 2020

@author: capliera
"""

import numpy as np
import skimage.io as skio
import scipy.ndimage as scnd
import skimage.filters as skf
import skimage.color as skc
from skimage import color

import skimage as sk
import skimage.data as skd
import matplotlib.pyplot as plt
 
    
plt.rcParams['image.cmap'] = 'gray'
plt.close('all')

img = skio.imread('../images/toyobjects.png')

print("Loaded image has dimensions:", img.shape)
img = sk.img_as_float(img)


# Image gradient components Gx and Gy computation via Sobel filtering

Gx = skf.sobel_h(img)
Gy = skf.sobel_v(img)
print(Gx, Gy)

# Gradient magnitude and orientation computation 

G = np.sqrt(Gx**2+Gy**2)
Gx = Gx+0.0001
theta = np.arctan(Gy/Gx)
print(G, theta)

#Edge pixels detection : 1st method

T = 0.3
max = np.max(G)
h,w = G.shape
B = np.zeros((h,w))

for i in range(h):
    for j in range(w):
        B[i][j] = 1 if G[i][j] > T*max else 0

plt.subplot(1,2,1), plt.imshow(img),plt.title('Original Image')
plt.subplot(1,2,2), plt.imshow(B),plt.title('Contour')
plt.show()

# Edge pixels detection : second method with hysteresis thresholding
img = skd.coffee()
img = skc.rgb2gray(img)
Gx = skf.sobel_h(img)
Gy = skf.sobel_v(img)
G = np.sqrt(Gx**2+Gy**2)
Gx = Gx+0.0001
theta = np.arctan(Gy/Gx)

max = np.max(G)
h,w = G.shape
B = np.zeros((h,w))

Th = 0.3
Tl = 0.1

for i in range(h):
    for j in range(w):
        try:
            if G[i][j] > Th * max:
                B[i][j] = 1
            elif G[i][j] > Tl*max and (G[i-1][j-1] > Th*max or G[i-1][j] > Th*max or G[i-1][j+1] > Th*max or G[i][j-1] > Th*max or G[i][j+1] > Th*max or G[i+1][j-1] > Th*max or G[i+1][j] > Th*max or G[i+1][j+1] > Th*max):
                B[i][j] = 1
            else:
                B[i][j] = 0
        except IndexError:
            print("Border...")

plt.subplot(1,2,1), plt.imshow(img),plt.title('Original Image')
plt.subplot(1,2,2), plt.imshow(B),plt.title('Contour')
plt.show()
