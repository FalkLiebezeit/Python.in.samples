"""Animation of uniform circular motion with velocity and acceleration vectors."""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

# Parameters for the circular motion
radius = 3.0        # Radius of the circle [m]
T = 12.0            # Period of one revolution [s]
dt = 0.02           # Time step [s]
omega = 2 * np.pi / T  # Angular velocity [rad/s]

# Print analytical results for reference
print(f'Linear velocity:           {radius * omega:.3f} m/s')
print(f'Centripetal acceleration:  {radius * omega ** 2:.3f} m/s²')

# Create an array of time points for one revolution
t = np.arange(0, T, dt)

# Calculate the position of the mass point at each time step
r = np.empty((t.size, 2))
r[:, 0] = radius * np.cos(omega * t)  # x-coordinates
r[:, 1] = radius * np.sin(omega * t)  # y-coordinates

# Calculate velocity and acceleration vectors using finite differences
v = (r[1:] - r[:-1]) / dt             # Velocity vectors
a = (v[1:] - v[:-1]) / dt             # Acceleration vectors

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlabel('$x$ [m]')
ax.set_ylabel('$y$ [m]')
ax.set_xlim(-1.2 * radius, 1.2 * radius)
ax.set_ylim(-1.2 * radius, 1.2 * radius)
ax.set_aspect('equal')
ax.grid()

# Plot the circular path
plot_path, = ax.plot(r[:, 0], r[:, 1], label='Path')

# Create a point plot for the current position of the mass
plot_point, = ax.plot([], [], 'o', color='blue')

# Create text fields to display the current velocity and acceleration magnitudes
text_v = ax.text(0, 0.2, '', color='red')
text_a = ax.text(0, -0.2, '', color='black')

# Create arrows for velocity and acceleration
arrow_style = mpl.patches.ArrowStyle.Simple(head_length=6, head_width=3)
arrow_v = mpl.patches.FancyArrowPatch((0, 0), (0, 0), color='red', arrowstyle=arrow_style)
arrow_a = mpl.patches.FancyArrowPatch((0, 0), (0, 0), color='black', arrowstyle=arrow_style)

# Add the arrow patches to the axes
ax.add_patch(arrow_v)
ax.add_patch(arrow_a)

def update(n):
    """Update the animation for the n-th time step."""
    # Update velocity arrow and display its magnitude
    if n < len(v):
        arrow_v.set_positions(r[n], r[n] + v[n])
        text_v.set_text(f'$v$ = {np.linalg.norm(v[n]):.3f} m/s')
    # Update acceleration arrow and display its magnitude
    if n < len(a):
        arrow_a.set_positions(r[n], r[n] + a[n])
        text_a.set_text(f'$a$ = {np.linalg.norm(a[n]):.3f} m/s²')
    # Update the position of the mass point
    plot_point.set_data(r[n].reshape(-1, 1))
    return plot_point, arrow_v, arrow_a, text_a, text_v

# Create and start the animation
ani = mpl.animation.FuncAnimation(
    fig, update, frames=t.size, interval=30, blit=True
)
plt.show()