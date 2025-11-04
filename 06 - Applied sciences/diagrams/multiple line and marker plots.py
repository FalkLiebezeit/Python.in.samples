"""
Example of multiple line and marker plots using matplotlib.

Demonstrates how to plot lines and markers, set axis limits and ticks,
and use a custom style for improved appearance.
"""

import matplotlib.pyplot as plt
import numpy as np

# Use a clean gallery style for the plot
plt.style.use('_mpl-gallery')

# Generate data for smooth and sparse sine curves
x = np.linspace(0, 10, 100)           # Smooth curve
y = 4 + 1 * np.sin(2 * x)
x2 = np.linspace(0, 10, 25)           # Sparse points
y2 = 4 + 1 * np.sin(2 * x2)


# Create the figure and axes with a size of 800x600 pixels (8x6 inches at 100 dpi)
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)

# Plot sparse points with 'x' markers, shifted up
ax.plot(x2, y2 + 2.5, 'x', markeredgewidth=2, label="Sparse Points +2.5")

# Plot the smooth sine curve as a thick line
ax.plot(x, y, linewidth=2.0, label="Smooth Sine Curve")

# Plot sparse points with 'o' markers connected by lines, shifted down
ax.plot(x2, y2 - 2.5, 'o-', linewidth=2, label="Sparse Points -2.5")

# Set axis limits and custom ticks for clarity
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

# Add a legend for clarity
ax.legend()

# Display the plot
plt.show()