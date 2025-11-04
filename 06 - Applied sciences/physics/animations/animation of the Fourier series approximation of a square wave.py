"""Animation of the Fourier series approximation of a square wave.

This script visualizes how the Fourier series converges to a square wave
by animating the sum of the first n terms.
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

# Number of points to display for smooth curves
n_points = 2000

# Create an array of x values over one period [0, 2π]
x = np.linspace(0, 2 * np.pi, n_points)

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_title('Fourier Approximation of a Square Wave')
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()

# Create an empty plot and a text field for the current number of terms
plot, = ax.plot([], [], lw=2)
text = ax.text(np.pi / 2, 0.2, '', fontsize=12)

def update(n):
    """Update the plot for the n-th animation frame.

    Args:
        n (int): Number of Fourier terms to sum.

    Returns:
        tuple: Updated plot and text objects.
    """
    # Compute the sum of the first n terms of the Fourier series
    y = np.zeros(n_points)
    for k in range(n):
        y += 4 / np.pi * np.sin((2 * k + 1) * x) / (2 * k + 1)

    # Update the plot and the text field
    plot.set_data(x, y)
    text.set_text(f'n = {n}')
    return plot, text

# Create the animation object
ani = mpl.animation.FuncAnimation(
    fig, update, interval=30, blit=True
)

# Start the animation
plt.show()