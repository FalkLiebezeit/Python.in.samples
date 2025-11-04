"""Animation of motion along a helical (screw) path in 3D.

This script visualizes the motion of a mass point along a helical trajectory.
It also displays the velocity and acceleration vectors at each time step.
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation
import mpl_toolkits.mplot3d

# Parameters for the helical path
radius = 3.0         # Radius of the helix [m]
T = 8.0              # Period for one revolution [s]
dt = 0.05            # Time step [s]
v_z = 0.5            # Vertical speed [m/s]
n_turns = 5          # Number of revolutions

# Calculate angular velocity [rad/s]
omega = 2 * np.pi / T

# Create an array of time points for the full motion
t = np.arange(0, n_turns * T, dt)

# Calculate the position of the mass point at each time step
r = np.empty((t.size, 3))
r[:, 0] = radius * np.cos(omega * t)      # x-coordinate
r[:, 1] = radius * np.sin(omega * t)      # y-coordinate
r[:, 2] = v_z * t                         # z-coordinate

# Calculate velocity and acceleration vectors using finite differences
v = (r[1:] - r[:-1]) / dt                 # Velocity vectors
a = (v[1:] - v[:-1]) / dt                 # Acceleration vectors

# Set up the figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d', elev=30, azim=45)
ax.set_xlabel('$x$ [m]')
ax.set_ylabel('$y$ [m]')
ax.set_zlabel('$z$ [m]')
ax.grid()

class Arrow3D(mpl.patches.FancyArrowPatch):
    """3D arrow for use in a 3D plot.

    Args:
        posA (tuple): Start point (x, y, z)
        posB (tuple): End point (x, y, z)
        *args, **kwargs: Passed to FancyArrowPatch
    """
    def __init__(self, posA, posB, *args, **kwargs):
        super().__init__(posA[0:2], posB[0:2], *args, **kwargs)
        self._pos = np.array([posA, posB])

    def set_positions(self, posA, posB):
        """Set the start and end points of the arrow."""
        self._pos = np.array([posA, posB])

    def do_3d_projection(self, renderer=None):
        """Project the 3D points into the 2D image plane."""
        p = mpl_toolkits.mplot3d.proj3d.proj_transform(*self._pos.T, self.axes.M)
        p = np.array(p)
        super().set_positions(p[:, 0], p[:, 1])
        return np.min(p[2, :])

# Plot the helical trajectory
plot_path, = ax.plot(r[:, 0], r[:, 1], r[:, 2], linewidth=0.7, label='Helical Path')

# Create a point plot for the current position of the mass
plot_point, = ax.plot([], [], [], 'o', color='red', label='Mass Point')

# Create arrows for velocity and acceleration and add them to the axes
arrow_style = mpl.patches.ArrowStyle.Simple(head_length=6, head_width=3)
arrow_v = Arrow3D((0, 0, 0), (0, 0, 0), color='red', arrowstyle=arrow_style)
arrow_a = Arrow3D((0, 0, 0), (0, 0, 0), color='black', arrowstyle=arrow_style)
ax.add_patch(arrow_v)
ax.add_patch(arrow_a)

def update(n):
    """Update the animation for the n-th time step."""
    # Update velocity arrow
    if n < len(v):
        arrow_v.set_positions(r[n], r[n] + v[n])
    # Update acceleration arrow
    if n < len(a):
        arrow_a.set_positions(r[n], r[n] + a[n])
    # Update the position of the mass point
    plot_point.set_data_3d(r[n, :].reshape(-1, 1))
    return plot_point, arrow_v, arrow_a

# Create and start the animation
ani = mpl.animation.FuncAnimation(
    fig, update, frames=t.size, interval=30
)
plt.legend()
plt.show()