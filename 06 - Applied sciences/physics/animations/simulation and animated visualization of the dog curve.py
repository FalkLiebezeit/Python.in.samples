"""Simulation and animated visualization of the dog curve (pursuit curve)."""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

# Initial position (x, y) of the dog [m].
r0_dog = np.array([0.0, 10.0])
# Initial position (x, y) of the human [m].
r0_human = np.array([0.0, 0.0])
# Velocity vector (vx, vy) of the human [m/s].
v_human = np.array([2.0, 0.0])
# Speed (magnitude of velocity) of the dog.
speed_dog = 3.0
# Maximum simulation time [s].
t_max = 500
# Time step [s].
dt = 0.01

# Minimum distance at which the simulation will stop.
min_distance = speed_dog * dt

# Create lists to store the simulation results.
t = [0]
r_dog = [r0_dog]
r_human = [r0_human]
v_dog = []

# Simulation loop.
while True:
    # Calculate the velocity vector of the dog (always points toward the human).
    vec_dog_to_human = r_human[-1] - r_dog[-1]
    distance = np.linalg.norm(vec_dog_to_human)
    v_dog.append(speed_dog * vec_dog_to_human / distance)

    # Stop the simulation if the dog is close enough to the human
    # or if the maximum simulation time is exceeded.
    if (distance < min_distance) or (t[-1] > t_max):
        break

    # Update the positions and time.
    r_dog.append(r_dog[-1] + dt * v_dog[-1])
    r_human.append(r_human[-1] + dt * v_human)
    t.append(t[-1] + dt)

# Convert lists to arrays. Rows correspond to time steps, columns to coordinates.
t = np.array(t)
r_dog = np.array(r_dog)
v_dog = np.array(v_dog)
r_human = np.array(r_human)

# Calculate the acceleration vectors of the dog.
# Note: This array has one less row than the number of time steps.
a_dog = (v_dog[1:] - v_dog[:-1]) / dt

# Create a figure and axes object.
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('$x$ [m]')
ax.set_ylabel('$y$ [m]')
ax.set_xlim(-0.2, 15)
ax.set_ylim(-0.2, 10)
ax.set_aspect('equal')
ax.grid()

# Create an empty line plot for the dog's path and
# two empty point plots for the positions of the dog and the human.
plot_path_dog, = ax.plot([], [])
plot_dog, = ax.plot([], [], 'o', color='blue')
plot_human, = ax.plot([], [], 'o', color='red')

# Create two arrows for velocity and acceleration.
style = mpl.patches.ArrowStyle.Simple(head_length=6, head_width=3)
arrow_v = mpl.patches.FancyArrowPatch((0, 0), (0, 0),
                                      color='red',
                                      arrowstyle=style)
arrow_a = mpl.patches.FancyArrowPatch((0, 0), (0, 0),
                                      color='black',
                                      arrowstyle=style)

# Add the arrow objects to the axes.
ax.add_patch(arrow_v)
ax.add_patch(arrow_a)


def update(n):
    """Update the graphic for the n-th time step."""
    # Set the start and end point of the velocity arrow.
    arrow_v.set_positions(r_dog[n], r_dog[n] + v_dog[n])

    # Set the start and end point of the acceleration arrow.
    if n < len(a_dog):
        arrow_a.set_positions(r_dog[n], r_dog[n] + a_dog[n])

    # Update the positions of the dog and the human.
    plot_dog.set_data(r_dog[n].reshape(-1, 1))
    plot_human.set_data(r_human[n].reshape(-1, 1))

    # Plot the dog's path up to the current time.
    plot_path_dog.set_data(r_dog[:n + 1, 0], r_dog[:n + 1, 1])

    return plot_path_dog, plot_dog, plot_human, arrow_v, arrow_a


# Create the animation object and start the animation.
ani = mpl.animation.FuncAnimation(fig, update, frames=t.size,
                                  interval=30, blit=True)
plt.show()