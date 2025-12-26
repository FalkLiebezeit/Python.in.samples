"""Simulation and animated visualization of a pursuit problem.

The pursuer (dog) always runs directly toward the person,
who moves along a circular path.
"""

import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

# Initial position (x, y) of the dog [m]
r0_dog = np.array([28.0, 0.0])
# Speed of the dog [m/s]
v_dog = 2
# Radius of the circular path for the person [m]
radius = 5.0
# Speed of the person along the path [m/s]
v_person = 2.5
# Maximum simulation time [s]
t_max = 40
# Time step [s]
dt = 0.02

# Minimum distance at which the simulation will stop
min_distance = v_dog * dt

# Lists to store simulation results
t = [0]
r_dog = [r0_dog]
r_person = []
v_dog_vec = []

# Simulation loop
while True:
    # Calculate the current position of the person on the circle
    r_person.append(np.array([
        radius * math.cos(v_person / radius * t[-1]),
        radius * math.sin(v_person / radius * t[-1])
    ]))

    # Calculate the velocity vector of the dog (always points toward the person)
    vec_to_person = r_person[-1] - r_dog[-1]
    distance = np.linalg.norm(vec_to_person)
    v = v_dog * vec_to_person / distance
    v_dog_vec.append(v)

    # Stop simulation if dog is close enough or time is up
    if (distance < min_distance) or (t[-1] > t_max):
        break

    # Update dog's position and time
    r_dog.append(r_dog[-1] + dt * v)
    t.append(t[-1] + dt)

# Convert lists to arrays for easier indexing
t = np.array(t)
r_dog = np.array(r_dog)
v_dog_vec = np.array(v_dog_vec)
r_person = np.array(r_person)

# Set up the figure and axes
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('$x$ [m]')
ax.set_ylabel('$y$ [m]')
ax.set_xlim(-6, 30)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.grid()

# Create empty line plots for the paths of the dog and the person
plot_path_dog, = ax.plot([], [], color='b', label='Dog Path')
plot_path_person, = ax.plot([], [], color='r', label='Person Path')

# Create point plots for the current positions
plot_dog, = ax.plot([], [], 'o', color='blue', label='Dog')
plot_person, = ax.plot([], [], 'o', color='red', label='Person')

# Create an arrow for the dog's velocity and add it to the axes
style = mpl.patches.ArrowStyle.Simple(head_length=6, head_width=3)
arrow_v = mpl.patches.FancyArrowPatch((0, 0), (0, 0),
                                      color='red',
                                      arrowstyle=style)
ax.add_patch(arrow_v)

def update(n):
    """Update the animation for the n-th time step."""
    # Set the start and end point of the velocity arrow
    arrow_v.set_positions(r_dog[n], r_dog[n] + v_dog_vec[n])

    # Update the positions of the dog and the person
    plot_dog.set_data(r_dog[n].reshape(-1, 1))
    plot_person.set_data(r_person[n].reshape(-1, 1))

    # Plot the paths up to the current time
    plot_path_dog.set_data(r_dog[:n + 1, 0], r_dog[:n + 1, 1])
    plot_path_person.set_data(r_person[:n + 1, 0], r_person[:n + 1, 1])

    return plot_dog, plot_person, arrow_v, plot_path_dog, plot_path_person

# Create and start the animation
ani = mpl.animation.FuncAnimation(
    fig, update, frames=t.size, interval=30, blit=True
)
ax.legend()
plt.show()