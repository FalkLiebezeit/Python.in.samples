"""
Animated visualization of a plane wave.
This script creates an animated plot of a plane wave using Matplotlib."""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

# Generate x values from 0 to 20 in 500 steps.
x = np.linspace(0, 20, 500)

# Define angular frequency omega, wave number k, and time step delta_t.
omega = 1.0
k = 1.0
delta_t = 0.04

# Create the figure and axes object.
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel('Position x')
ax.set_ylabel('u(x, t)')
ax.grid()

# Create an empty plot and an empty text field.
plot, = ax.plot([], [])
text = ax.text(0.5, 1.05, '')

def update(n):
    """Update the graphic for the n-th time step."""
    # Calculate the function values u at time t.
    t = n * delta_t
    u = np.cos(k * x - omega * t)

    # Update the plot and the text field.
    plot.set_data(x, u)
    text.set_text(f't = {t:5.1f}')

    # Return a tuple with the graphic elements that need to be redrawn.
    return plot, text

# Create the animation object.
ani = mpl.animation.FuncAnimation(fig, update,
                                  interval=30, blit=True)

# Start the animation.
plt.show()