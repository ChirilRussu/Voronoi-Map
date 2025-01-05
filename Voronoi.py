# to do:
# full screen window
# saving the image as png instead of jpg

import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import scipy.ndimage as ndimage
from matplotlib import lines

# creates an image object to be used as a background and flips it (don't know why the flip and later rotation is needed)
img = np.fliplr(plt.imread('Original_Map.jpg'))

# points on the figure
points = [
[-9999, -999], [9999, -9999], [-9999, 9999], [9999, 9999], #masks dotted lines going infinitely
[775, 779], [978, 451], [975, 835], [990, 755], [1113, 595], [1216, 770], [1256, 1156], 
[1386, 970], [1505, 848], [1409, 775], [1471, 741], [1830, 939], [1819, 860], [2111, 617], 
[1681, 454], [2085, 327]

]

# voronoi object based on points
vor = Voronoi(points)

# creates a figure
fig = plt.figure(figsize=(15,15))

# creates axes
ax = fig.add_subplot(111)

# displays the image and rotates it (don't know why it's rotated in the first place)
ax.imshow(ndimage.rotate(img, 180))

# creates the voronoi plot
voronoi_plot_2d(vor, show_vertices=False, point_size=10, ax=ax)

# colorize - kinda distracting
# for region in vor.regions:
    # if not -1 in region:
        # polygon = [vor.vertices[i] for i in region]
        # plt.fill(*zip(*polygon), alpha=0.45)

# axes limits (otherwise it automatiically fits to the figure and cuts off the image)
ax.set_xlim(-0, 2700)
ax.set_ylim(-0, 1500)

# displays the plot
plt.show()




