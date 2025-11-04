"""Shot at a Falling Monkey: Animated Trajectory Simulation.

This script simulates and animates the classic physics problem where a projectile
(arrow) is fired directly at a monkey that drops from a branch at the same instant.
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

# Initial position of the arrow [m]
r0_arrow = np.array([0.0, 0.0])
# Initial position of the monkey [m]
r0_monkey = np.array([3.0, 2.0])
# Initial speed of the arrow [m/s]
v0_arrow_mag = 9.0
# Gravitational acceleration [m/s²]
g = 9.81
# Time step [s]
dt = 0.001

# Calculate the direction vector for the arrow's velocity
direction = r0_monkey - r0_arrow
v0_arrow = v0_arrow_mag * direction / np.linalg.norm(direction)

# Acceleration vector due to gravity
a = np.array([0, -g])

# Calculate the time when the arrow reaches the monkey's x-position
t_end = (r0_monkey[0] - r0_arrow[0]) / v0_arrow[0]

# Generate time array and compute positions of arrow and monkey at each time step
t = np.arange(0, t_end, dt).reshape(-1, 1)
r_arrow = r0_arrow + v0_arrow * t + 0.5 * a * t**2
r_monkey = r0_monkey + 0.5 * a * t**2

# Create the figure and axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(0, 1.1 * max(r0_arrow[0], r0_monkey[0]))
ax.set_ylim(0, 1.1 * max(r0_arrow[1], r0_monkey[1]))
ax.set_xlabel('$x$ [m]')
ax.set_ylabel('$y$ [m]')
ax.set_aspect('equal')
ax.grid()

# Plot the aiming line (straight line from arrow to monkey)
ax.plot([r0_arrow[0], r0_monkey[0]],
        [r0_arrow[1], r0_monkey[1]],
        '--', color='black', lw=0.5)

# Plot the full trajectory of the arrow
plot_traj_arrow, = ax.plot(r_arrow[:, 0], r_arrow[:, 1], color='red', zorder=3)

# Create point plots for the current positions of the arrow and monkey
plot_arrow, = ax.plot([], [], 'o', color='red', zorder=3)
plot_monkey, = ax.plot([], [], 'o', color='blue', zorder=2)

def update(n):
    """Update the animation for the n-th time step."""
    # Update the positions of the arrow and monkey points
    plot_arrow.set_data(r_arrow[n].reshape(-1, 1))
    plot_monkey.set_data(r_monkey[n].reshape(-1, 1))

    # Plot the arrow's trajectory up to the current time
    plot_traj_arrow.set_data(r_arrow[:n + 1, 0], r_arrow[:n + 1, 1])

    return plot_arrow, plot_monkey, plot_traj_arrow

# Create and start the animation
ani = mpl.animation.FuncAnimation(
    fig, update, frames=t.size, interval=30, blit=True, repeat_delay=1000
)
plt.show()