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

# Histogrammes

for image in ['pout.tif', 'alumgrns.tif', 'moon.tif']:
    im = skio.imread(image)

    fig = plt.figure()
    histogram, absice = ske.histogram(im, nbins=256)
    plt.xlim(0, 255)
    plt.bar(absice, histogram)
    plt.title('Histogram of ' + image)
    plt.show()

histo1 = np.zeros((256, 256), dtype=int)
histo2 = np.zeros((256, 256), dtype=int)

for i in range(50):
    for j in range(50):
        histo1[i, j] = 255
        histo2[i, 255-j] = 255

fig = plt.figure()

plt.subplot(2, 2, 1)
plt.imshow(histo1)
plt.subplot(2, 2, 2)
histogram, absice = np.histogram(histo1)
plt.bar(absice[0:-1], histogram)
plt.title('Histogram')
plt.subplot(2, 2, 3)
plt.imshow(histo2)
plt.subplot(2, 2, 4)
histogram, absice = np.histogram(histo2)
plt.bar(absice[0:-1], histogram)
plt.title('Histogram')
fig.tight_layout()
plt.show()

# Neighborhood impact

neigh1 = np.full((256, 256), 100)
neigh2 = np.full((256, 256), 170)

for i in range(0, 56):
    for j in range(0, 56):
        neigh1[100 + i, 100 + j] = 135
        neigh2[100 + i, 100 + j] = 135

fig = plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(neigh1, vmin=0, vmax=255)
plt.subplot(1, 2, 2)
plt.imshow(neigh2, vmin=0, vmax=255)
plt.show()

# Creating image

degrad = np.zeros((256, 256), dtype=int)
circle = np.zeros((256, 256), dtype=int)

for i in range(0, 255):
    degrad[i, :] = 256*[i]

for i in range(0, 255):
    for j in range(0, 255):
        if (i-128)**2 + (j-128)**2 <= 80**2:
            circle[i, j] = 255

fig = plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(degrad, vmin=0, vmax=255)
plt.subplot(2, 2, 2)
plt.imshow(circle, vmin=0, vmax=255)
plt.subplot(2, 2, 3)
plt.imshow(circle - degrad, vmin=0, vmax=255)
plt.show()