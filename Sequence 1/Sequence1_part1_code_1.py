# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:56:53 2020

@author: capliera
"""

import numpy as np
import skimage.data as skd
import skimage.io as skio
import matplotlib.pyplot as plt


import skimage.exposure as ske


#All figures closing
plt.close('all')

# matplotlib for gray level images display: fix the colormap and 
# the image figure size

plt.rcParams['image.cmap'] = 'gray'
plt.rcParams["figure.figsize"] = (6,4)

# Several test images are available in the scikit-images.data module.
# Those images are entiltled: coins, astronaut (color), brick, camera, cell,
# chekerboard, chelsea (color), clock, coffee (color), colorwheel (color), grass (color),
# gravel (color), horse (black and white), moon, retina (color), rocket (color).

# To download any of those images just use skd.image_name()
# To download any other image, use skio.imread('image_name')


## Grey level image reading and information

I=skd.coins()
Dim = I.shape
nb_pixels=I.size
Max_grey_level=np.max(I)
Min_grey_level=np.min(I)
Mean_grey_level=np.mean(I)
print(Dim)
print(Max_grey_level)
print(Min_grey_level)
print(Mean_grey_level)

# Image display
fig1=plt.figure(1)                    
skio.imshow(I)
plt.title('Coins')


# Color image reading and RGB channel visualization
J=skd.coffee()
fig4=plt.figure(4)
plt.subplot(2,2,1), plt.imshow(J), plt.title('Color img')
plt.subplot(2,2,2), plt.imshow(J[:,:,0]), plt.title('Red Channel')
plt.subplot(2,2,3), plt.imshow(J[:,:,1]), plt.title('Green Channel')
plt.subplot(2,2,4), plt.imshow(J[:,:,2]), plt.title('Blue Channel')
fig4.tight_layout()

# Luminance extraction : compute the luminance as 0.3*R+0.58*G+0.11*B
# Display the luninance evolution along line 200

# WARNING : instructon A=B does not create a new array, A and B are the same 
# object then modifying A will also modify B => use .copy() function in order
# duplicate an image

fig5 = plt.figure(5)

modifJ = J.copy()

for i in range(600):
    modifJ[200, i, 0] = 0
    modifJ[200, i, 1] = 0
    modifJ[200, i, 2] = 0

plt.subplot(1,2,1), plt.imshow(0.3 * modifJ[:,:,0] + 0.58 * modifJ[:,:,1] + 0.11 *modifJ[:,:,2]), plt.title('L Channel')
plt.subplot(1,2,2), plt.plot(range(600), 0.3 * J[200,:,0] + 0.58 * J[200,:,1] + 0.11 * J[200,:,2]), plt.title('L along x = 200')


#Two imshow() functions for image display
# Compute the histogram of image 3 (cf. ske.histogram())
#Display the hitogram ((cf. plt.bar())

image3=skio.imread('CH0SRC.TIF')

fig6 = plt.figure(6)
histogram, absice = ske.histogram(image3, nbins=256)
plt.xlim(0, 255)
plt.bar(absice, histogram)
plt.title('Histogram')


# Display image3 by suing first skio.image() and second by usig plt.imshow()
#What is the difference between both functions ?      

fig7 = plt.figure(7)
plt.subplot(1,2,1)
plt.title('skio')
skio.imshow(image3)
plt.subplot(1,2,2)
plt.title('plt')
plt.imshow(image3)
plt.tight_layout()
plt.show()

