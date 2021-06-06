import magpylib as magpy
from magpylib.source.current import Circular
import numpy as np
from matplotlib import pyplot as plt
from skimage import measure

# windings of three parts of a coil
coil1a = [Circular(curr=1,
                   dim=3,
                   pos=[0, 0, z]) for z in np.linspace(-3, 3, 15)]

# create collection and manipulate step by step
c1 = magpy.Collection(coil1a)

# magpy.displaySystem(c1, figsize=(6,6))

# create positions
xs = np.linspace(-8, 8, 100)
zs = np.linspace(-6, 6, 100)
posis = [[x, 0, z] for z in zs for x in xs]

# calculate field and amplitude
B = [c1.getB(pos) for pos in posis]
Bs = np.array(B).reshape([100, 100, 3]) #reshape
Bamp = np.linalg.norm(Bs, axis=2)
print(Bamp.shape)
print(Bamp[50, 50]) # field in center

fig = plt.figure(figsize=[5, 5])
ax = fig.add_axes([.1,.1,.8,.8])

# amplitude plot on ax2
X, Z = np.meshgrid(xs, zs)
img = ax.pcolor(range(100),
                range(100),
                Bamp,
                vmax=3.,
                cmap='jet',
                shading='auto')

U, V = Bs[:,:,0], Bs[:,:,2]
ax.streamplot(xs, zs, U, V, color='k',linewidth=1, density=2)

# contour_vals = np.linspace(0, 5., 100)
# for val in contour_vals:
#     contours = measure.find_contours(Bamp, val)
#     for contour in contours:
#         ax.plot(contour[:, 1],
#                 contour[:, 0],
#                 'w--', linewidth=1)

fig.colorbar(img)
plt.show()
