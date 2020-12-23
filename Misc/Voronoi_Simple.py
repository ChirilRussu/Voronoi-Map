# to start plotting coordinates on an image

import numpy as np 
import matplotlib.pyplot as plt

img = plt.imread('Original Map.jpg')
plt.imshow(img)

# Flip
# img2 = np.fliplr(img)
# plt.imshow(img2)

plt.show()