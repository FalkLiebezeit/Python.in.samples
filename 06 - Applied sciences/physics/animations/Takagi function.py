"""Animation of the series definition of the Takagi function."""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

# --- Number of points to display ---
n_points = 2000

# --- Create an array of x values in [0, 1] ---
x = np.linspace(0, 1, n_points)

# --- Set up the figure and axes ---
fig = plt.figure(figsize=(8, 6))  # window 800 x 600 for better visibility
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Approximation of the Takagi Function', fontsize=14, fontweight='bold')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, linestyle='--', alpha=0.5)

# --- Create an empty plot and a text field for the current n ---
plot, = ax.plot([], [], lw=2, color='blue')
text = ax.text(0.05, 0.9, '', transform=ax.transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

def s(x):
    """Compute the distance from x to the nearest integer."""
    return np.abs(x - np.round(x))

def update(n):
    """
    Update the plot for the nth frame.
    Calculates the first n terms of the Takagi function series.
    """
    y = np.zeros(n_points)
    for k in range(n):
        y += s(2**k * x) / 2**k

    plot.set_data(x, y)
    text.set_text(f'n = {n}')
    return plot, text

# --- Create the animation object ---
ani = mpl.animation.FuncAnimation(
    fig, update,
    frames=range(51),
    interval=300,
    blit=True
)

plt.tight_layout()
plt.show()