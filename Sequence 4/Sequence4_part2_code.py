import numpy as np
import skimage.io as skio
import scipy.ndimage as scnd
import skimage.filters as skf
import skimage.color as skc
from skimage import color

import skimage as sk
import skimage.data as skd
import matplotlib.pyplot as plt
import math

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

#All figures closing
plt.close('all')

# matplotlib for gray level images display: fix the colormap and
# the image figure size

plt.rcParams['image.cmap'] = 'gray'
plt.rcParams["figure.figsize"] = (6,4)

#Image loadind and display -Histogram computation
# Plot in the same figure the image and its histogram

filename = r'../images/muscle.tif'

image=skio.imread(filename)

# Noise reduction

variance = 1

filtered_image = skf.gaussian(image, variance)

# Gradient magnitude and orientation computation

Gx = skf.sobel_h(filtered_image)
Gy = skf.sobel_v(filtered_image)
G = np.sqrt(Gx**2+Gy**2)
Gx = Gx+0.0001      # To prevent division by zero
theta = np.arctan(Gy/Gx)

# Non maximum suppression for contour thinering

h,w = G.shape
for i in range(h):
    for j in range(w):
        try:
            t = find_nearest([-math.pi/2, -math.pi/4, 0, math.pi/4, math.pi/2], theta[i][j])
            if t == -math.pi/2 or t == math.pi/2:
                if G[i+1][j] > G[i][j] or G[i-1][j] > G[i][j]:
                    G[i][j] = 0
            if t == -math.pi/4 or t == math.pi/4:
                if G[i+1][j+1] > G[i][j] or G[i-1][j-1] > G[i][j]:
                    G[i][j] = 0
            if t == 0:
                if G[i][j+1] > G[i][j] or G[i][j-1] > G[i][j]:
                    G[i][j] = 0
        except IndexError:
            print("Border...")

# Histeresis thresholding

max = np.max(G)

Th = 0.4
Tl = 0.1

result = np.zeros((h,w))

for i in range(h):
    for j in range(w):
        try:
            if G[i][j] > Th * max:
                result[i][j] = 1
            elif G[i][j] > Tl*max and (G[i-1][j-1] > Th*max or G[i-1][j] > Th*max or G[i-1][j+1] > Th*max or G[i][j-1] > Th*max or G[i][j+1] > Th*max or G[i+1][j-1] > Th*max or G[i+1][j] > Th*max or G[i+1][j+1] > Th*max):
                result[i][j] = 1
            else:
                result[i][j] = 0
        except IndexError:
            print("Border...")

plt.subplot(1,2,1), plt.imshow(image),plt.title('Original Image')
plt.subplot(1,2,2), plt.imshow(result),plt.title('Contour')
plt.suptitle(f'Var = {variance}, Th = {Th}, Tl = {Tl}')
plt.show()
