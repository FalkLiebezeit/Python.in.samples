"""Acceleration and velocity of a pendulum: Animated visualization."""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

# Pendulum parameters
laenge = 3.0                # Length of the pendulum [m]
T = 3.47                    # Oscillation period [s]
dt = 0.02                   # Time step [s]
phi0 = np.radians(10)       # Initial angular displacement [rad]

# Create an array of time points for one period
t = np.arange(0, T, dt)

# Preallocate array for the position vector (x, y) of the mass point
r = np.empty((t.size, 2))

# Calculate the angular frequency and the angle at each time
omega = 2 * np.pi / T
phi = phi0 * np.cos(omega * t)
r[:, 0] = laenge * np.sin(phi)      # x-coordinate
r[:, 1] = -laenge * np.cos(phi)     # y-coordinate

# Calculate velocity and acceleration vectors using finite differences
v = (r[1:, :] - r[:-1, :]) / dt     # Velocity vector at each time step
a = (v[1:, :] - v[:-1, :]) / dt     # Acceleration vector at each time step

# Set up the figure and axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('$x$ [m]')
ax.set_ylabel('$y$ [m]')
ax.set_xlim(-0.5 * laenge, 0.5 * laenge)
ax.set_ylim(-1.2 * laenge, 0.1 * laenge)
ax.set_aspect('equal')
ax.grid()

# Plot the circular trajectory of the pendulum and the pendulum rod (thread)
plot_bahn, = ax.plot(r[:, 0], r[:, 1])              # Path of the pendulum mass
plot_faden, = ax.plot([], [], color='black', lw=0.5) # Pendulum rod

# Create a point plot for the position of the mass
plot_masse, = ax.plot([], [], 'o', color='blue')

# Create two arrows for velocity and acceleration
style = mpl.patches.ArrowStyle.Simple(head_length=6, head_width=3)
pfeil_v = mpl.patches.FancyArrowPatch((0, 0), (0, 0), color='red', arrowstyle=style)    # Velocity arrow
pfeil_a = mpl.patches.FancyArrowPatch((0, 0), (0, 0), color='black', arrowstyle=style)  # Acceleration arrow

# Add the arrow objects to the axes
ax.add_patch(pfeil_v)
ax.add_patch(pfeil_a)

def update(n):
    """Update the animation for the n-th time step."""
    # Set the start and end point of the velocity arrow
    if n < v.shape[0]:
        pfeil_v.set_positions(r[n], r[n] + v[n])

    # Set the start and end point of the acceleration arrow
    if n < a.shape[0]:
        pfeil_a.set_positions(r[n], r[n] + a[n])

    # Update the pendulum rod
    plot_faden.set_data([0, r[n, 0]], [0, r[n, 1]])

    # Update the position of the mass point
    plot_masse.set_data(r[n].reshape(-1, 1))

    return plot_masse, pfeil_v, pfeil_a, plot_faden

# Create and start the animation
ani = mpl.animation.FuncAnimation(fig, update, frames=t.size,
                                  interval=30, blit=True)
plt.show()