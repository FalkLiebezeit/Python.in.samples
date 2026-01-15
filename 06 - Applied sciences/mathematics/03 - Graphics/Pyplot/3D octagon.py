"""
Ki:

Write a Python program. The program should draw a three-dimensional octagon using Pyplot. 
The image should be 800 x 600 pixels in size.

answer:

Below is a Python program that creates a three-dimensional octagon using Matplotlib's mpl_toolkits.mplot3d 
and ensures the figure size is set to 800 x 600 pixels.
This program sets the figure size to 8 x 6 inches, which corresponds to 800 x 600 pixels (assuming 100 DPI). 
It constructs a 3D octagonal prism, adds faces to the plot, and renders it using Poly3DCollection.

"""


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define octagon vertices in 3D space
angle_step = np.pi / 4  # 8 sides
octagon_vertices = np.array([
    [np.cos(i * angle_step), np.sin(i * angle_step), 0] for i in range(8)
])

# Extrude to make it 3D
octagon_extruded = np.vstack([octagon_vertices, octagon_vertices + [0, 0, 1]])

# Define faces for 3D octagonal prism
faces = [
    octagon_vertices,  # Bottom face
    octagon_extruded[8:],  # Top face
] + [[octagon_extruded[i], octagon_extruded[(i+1) % 8], octagon_extruded[(i+1) % 8 + 8], octagon_extruded[i + 8]] for i in range(8)]

# Create the plot with specified size
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Add the faces
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='black', alpha=0.6))

# Set limits
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(0, 1.2)

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()