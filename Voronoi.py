import matplotlib.pylab as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import scipy.ndimage as ndimage

img_file = 'respawns.png'
img = plt.imread(img_file)

points = [
[np.random.uniform(0, img.shape[0]),np.random.uniform(0, img.shape[1])], 
[np.random.uniform(0, img.shape[0]),np.random.uniform(0, img.shape[1])], 
[np.random.uniform(0, img.shape[0]),np.random.uniform(0, img.shape[1])], 
[np.random.uniform(0, img.shape[0]),np.random.uniform(0, img.shape[1])]] 

#for i in range(100):
#    points.append([np.random.uniform(0, img.shape[0]),np.random.uniform(0, img.shape[1])])
#points = np.array(points)

vor = Voronoi(points)

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111)
ax.imshow(ndimage.rotate(img, 90))
voronoi_plot_2d(vor, point_size=10, ax=ax)
plt.show()