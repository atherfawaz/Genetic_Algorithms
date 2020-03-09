import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread('imageB.bmp')
imgplot = plt.imshow(img)
plt.show()