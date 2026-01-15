"""
Ki:

Write a Python program. 
The program should draw a three-dimensional truncated icosahedron using Pyplot. 
The image should be 800 x 600.

answer:

A truncated icosahedron is the shape of a classic soccer ball, 
consisting of 12 pentagons and 20 hexagons. 
Below is a Python program using Matplotlib and mpl_toolkits.mplot3d to visualize it.


"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial import ConvexHull

# Define golden ratio
phi = (1 + np.sqrt(5)) / 2

# Define vertex coordinates of a truncated icosahedron
vertices = np.array([
    # Pentagons and hexagons positioned symmetrically
    [-1, -phi, 0], [1, -phi, 0], [-1, phi, 0], [1, phi, 0],
    [0, -1, phi], [0, 1, phi], [0, -1, -phi], [0, 1, -phi],
    [-phi, 0, -1], [phi, 0, -1], [-phi, 0, 1], [phi, 0, 1],
    [-1, -phi, 0], [1, -phi, 0], [-1, phi, 0], [1, phi, 0]
])

# Compute convex hull to get faces
hull = ConvexHull(vertices)

# Create the plot with specified size
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Add faces to the plot
for simplex in hull.simplices:
    face = vertices[simplex]
    ax.add_collection3d(Poly3DCollection([face], facecolors='cyan', linewidths=1, edgecolors='black', alpha=0.6))

# Set limits and labels
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()