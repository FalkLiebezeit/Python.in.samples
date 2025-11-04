# animation_gear_system.py
# Animated visualization of a simple gear system using matplotlib

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.patches import Polygon

# --- Gear parameters ---
m = 0.5           # Module (tooth size)
gear_ratio = 2    # Transmission ratio
d1 = 8            # Pitch diameter of gear 1
d2 = gear_ratio * d1  # Pitch diameter of gear 2
a = (d1 + d2) / 2      # Center distance
z1 = int(d1 / m)       # Number of teeth gear 1
z2 = int(gear_ratio * z1)  # Number of teeth gear 2
h = 13 * m / 6         # Tooth height
c = 0.2 * m            # Backlash (clearance)
x1 = 1 / 7
x2 = 1 / 3
tooth_shape = np.array([-x2, -x1, x1, x2])  # Tooth profile (angular positions)
frames = 60

# Plot limits
xmax = (-11 / 16 * d2, 22 / 16 * d2)
ymax = (-10 / 16 * d2, 10 / 16 * d2)

def gear_shape(d, z, h):
    """
    Generate the complex coordinates of a gear with given diameter, number of teeth, and tooth height.
    """
    r = d / 2
    alpha = 2 * np.pi / z  # Angle per tooth
    sector = tooth_shape * alpha
    tooth = (np.array([r - h / 2, r + h / 2, r + h / 2, r - h / 2]) - c) * np.exp(1j * sector)
    # Repeat the tooth profile for each tooth and flatten the result
    return np.outer(np.exp(1j * alpha * np.arange(z)), tooth).ravel('C')

# --- Create gear objects (complex coordinates) ---
zr1 = gear_shape(d1, z1, h)
zr2 = gear_shape(d2, z2, h) * np.exp(1j * np.pi / z2)  # Phase offset for correct meshing

# --- Animation setup ---
step = 2 * np.pi / (z2 * frames)  # Rotation step per frame
fig = plt.figure(figsize=(6, 4))
ax = fig.add_axes([-0.2, -0.1, 1.2, 1.2])
frames_list = []

# --- Animation frame generation ---
for k in range(frames):
    # Rotate gear 1 clockwise, gear 2 counterclockwise
    zr1_rot = zr1 * np.exp(-1j * step * k)
    zr2_rot = zr2 * np.exp(1j * step * k)
    # Create polygons for both gears
    P1 = Polygon(zr1_rot.view(float).reshape(-1, 2), color='grey')
    P2 = Polygon(zr2_rot.view(float).reshape(-1, 2) + [a, 0], color='k')
    frames_list.append([ax.add_patch(P1), ax.add_patch(P2)])

# --- Create and display the animation ---
animation = ani.ArtistAnimation(fig, frames_list, interval=20, blit=True)
ax.set_aspect("equal")
ax.set_xlim(xmax)
ax.set_ylim(ymax)
plt.title("Animated Gear System")
plt.show()