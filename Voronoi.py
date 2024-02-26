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
[236, 606], [282, 566], [294, 468], [330, 440],
[360, 472], [360, 436], [406, 470], [460, 454],
[516, 420], [526, 386], [380, 346], [340, 300],
[454, 242], [474, 270], [522, 306], [554, 282],
[677, 220], [790, 360], [866, 370], [740, 425],
[805, 470], [860, 480], [825, 570], [780, 642],
[695, 620], [560, 615], [540, 740], [780, 740],
[725, 790], [639, 809], [650, 880], [566, 843],
[470, 830], [453, 800], [430, 723], [445, 675],
[357, 650], [302, 697], [257, 722], [325, 777],
[232, 290], [602, 656]
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
ax.set_xlim(-0, 1024)
ax.set_ylim(-0, 1024)

# displays the plot
plt.show()




