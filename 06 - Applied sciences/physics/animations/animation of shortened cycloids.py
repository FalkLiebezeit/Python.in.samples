"""Animation of shortened cycloids (trochoids).

This script visualizes the trajectory of a point attached to a rolling wheel.
It also displays the velocity and acceleration vectors at each time step.
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

# Wheel radius [m]
radius_wheel = 0.35
# Distance of the point from the wheel's axis [m]
radius_point = 0.35
# Rolling speed [m/s]
v_wheel = 5.0
# Number of wheel revolutions
num_revolutions = 2
# Number of time steps per revolution
steps_per_revolution = 200

# Angular velocity [rad/s]
omega = v_wheel / radius_wheel

# Period of one revolution [s]
T = 2 * np.pi / omega

# Total simulation time [s]
t_max = T * num_revolutions

# Time step [s]
dt = T / steps_per_revolution

# Array of time points
t = np.arange(0, t_max, dt)

# Scaling factors for velocity and acceleration arrows
scal_a = 1 / omega ** 2
scal_v = 1 / omega

# Calculate the position of the mass point at each time step
r = np.empty((t.size, 2))
r[:, 0] = radius_point * np.cos(-omega * t - np.pi / 2) + v_wheel * t  # x-coordinate
r[:, 1] = radius_point * np.sin(-omega * t - np.pi / 2) + radius_wheel # y-coordinate

# Calculate velocity and acceleration vectors using finite differences
v = (r[1:] - r[:-1]) / dt
a = (v[1:] - v[:-1]) / dt

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlabel('$x$ [m]')
ax.set_ylabel('$y$ [m]')
ax.set_xlim(-0.5 * radius_wheel, np.max(r[:, 0]) + 0.5 * radius_wheel)
ax.set_ylim(-0.5 * radius_wheel, 2.5 * radius_wheel)
ax.set_aspect('equal')
ax.grid()

# Plot the cycloid path
plot_path, = ax.plot(r[:, 0], r[:, 1], label='Cycloid Path')

# Create a point for the current position of the mass
plot_point, = ax.plot([], [], 'o', color='blue')

# Create text fields for displaying the current velocity and acceleration magnitudes
text_v = ax.text(0.1, 0.2, '', color='red', transform=ax.transAxes)
text_a = ax.text(0.6, 0.2, '', color='black', transform=ax.transAxes)

# Create arrows for velocity and acceleration
arrow_style = mpl.patches.ArrowStyle.Simple(head_length=6, head_width=3)
arrow_v = mpl.patches.FancyArrowPatch((0, 0), (0, 0), color='red', arrowstyle=arrow_style)
arrow_a = mpl.patches.FancyArrowPatch((0, 0), (0, 0), color='black', arrowstyle=arrow_style)

# Add the arrow patches to the axes
ax.add_patch(arrow_v)
ax.add_patch(arrow_a)

# Create a circle representing the wheel; initially invisible
wheel_circle = mpl.patches.Ellipse(
    (0, 0), width=2 * radius_wheel, height=2 * radius_wheel,
    fill=False, color='black', linewidth=0.5, visible=False
)
ax.add_patch(wheel_circle)

def update(n):
    """Update the animation for the n-th time step."""
    # Update velocity arrow and display its magnitude
    if n < len(v):
        arrow_v.set_positions(r[n], r[n] + scal_v * v[n])
        text_v.set_text(f'$v$ = {np.linalg.norm(v[n]):.1f} m/s')
    # Update acceleration arrow and display its magnitude
    if n < len(a):
        arrow_a.set_positions(r[n], r[n] + scal_a * a[n])
        text_a.set_text(f'$a$ = {np.linalg.norm(a[n]):.1f} m/s²')
    # Update the position of the mass point
    plot_point.set_data(r[n].reshape(-1, 1))
    # Update the position of the wheel and make it visible
    wheel_circle.set_center((v_wheel * n * dt, radius_wheel))
    wheel_circle.set_visible(True)
    return wheel_circle, plot_point, arrow_v, arrow_a, text_a, text_v

# Create and start the animation
ani = mpl.animation.FuncAnimation(
    fig, update, frames=t.size, interval=30, blit=True
)
plt.show()