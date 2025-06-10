"""
Ki:

Write a Python program that displays a sphere in 3D.

"""

import numpy as np
import matplotlib.pyplot as plt

# Define sphere parameters
theta, phi = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='b', edgecolor='k')

# Display the sphere
plt.show()