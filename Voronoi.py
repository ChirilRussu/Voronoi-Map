import matplotlib.pylab as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import scipy.ndimage as ndimage


img = plt.imread('Misc/Original Map.jpg')
img2 = np.fliplr(img)

points = [
[-100, -100], [1100, -100], [-100, 1100], [1100, 1100],
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
[232, 290]
]


vor = Voronoi(points)

fig = plt.figure(figsize=(30,30))
ax = fig.add_subplot(111)


ax.imshow(ndimage.rotate(img2, 180))
voronoi_plot_2d(vor,show_vertices=False, point_size=10, ax=ax)

plt.show()




