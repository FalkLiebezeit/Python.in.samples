"""
3D Bar Chart Example using matplotlib

See: https://matplotlib.org/stable/gallery/mplot3d/bar3d.html
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

# --- Prepare data for 3D bars ---
x = [1, 1, 2, 2]                  # x positions of bars
y = [1, 2, 1, 2]                  # y positions of bars
z = [0, 0, 0, 0]                  # z base (all bars start at 0)
dx = np.full_like(x, 0.5, dtype=float)  # width of bars in x
dy = np.full_like(x, 0.5, dtype=float)  # width of bars in y
dz = [2, 3, 1, 4]                 # heights of bars

# --- Create a larger figure for better visibility ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# --- Plot 3D bars ---
ax.bar3d(x, y, z, dx, dy, dz, shade=True)

# --- Remove tick labels for a cleaner look ---
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

# --- Set axis labels ---
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Value')

plt.tight_layout()
plt.show()