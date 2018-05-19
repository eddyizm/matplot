# orion constellation
# %matplotlib notebook
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
'''
# Orion
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

fig = plt.figure()
fig.add_subplot(1,1,1)
plt.add_subplot(1,1,1)
plt.scatter(x,y)

fig_3d = plt.figure()
fig_3d.add_subplot(1, 1, 1, projection='3d')
constellation3d = plt.scatter(x,y,z)
'''
# star data from http://www.stellar-database.com using Celestial (X,Y,Z) coordinates
new_star_legend = ['Procyon', 'Sirius', '61 Cygni','Alpha/Proxima Centari', 'Wolf 359']
a = [ -4.769, -1.612, 6.489, -1.643 ,  -0.0566 ]
b = [10.31, 8.078, -6.109, -1.374,  -5.920]
c = [1.039, -2.474, 7.152, -3.838, 0.486]

# create the figure and subplot axes
fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
ax.set_title('Celestial (X,Y,Z) coordinates in ly')

# scatter plot
ax.scatter(a, b, c, marker='*', linewidth=4)

# apply labels to each star
for zdir, x, y, z in zip(new_star_legend, a, b, c):
    ax.text(x, y, z, zdir)

# apply a simple rotation animation
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)

# the show method is not needed in this instance
# plt.show()