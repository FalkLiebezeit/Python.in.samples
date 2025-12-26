"""Visualization and area calculation of a flower bed.

This script calculates the area of an irregularly shaped flower bed
using the shoelace formula and visualizes its outline with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

# Coordinates of the vertices [m]
x = np.array([0.0, 0.0, 1.0, 2.2, 2.8, 3.8, 4.6,
              5.7, 6.4, 7.1, 7.6, 7.9, 7.9, 0.0])
y = np.array([1.0, 2.8, 3.3, 3.5, 3.4, 2.7, 2.4,
              2.3, 2.1, 1.6, 0.9, 0.5, 0.0, 1.0])

# Calculate the area using the shoelace formula (Gauss's trapezoidal rule)
area = 0.5 * abs(np.dot(y + np.roll(y, 1), x - np.roll(x, 1)))

# Print the result as a complete sentence
print(f"The area is {area:.1f} m².")

# Create the figure and axes object
fig, ax = plt.subplots()
ax.set_title('Area Calculation of a Flower Bed')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_aspect('equal')  # Ensure equal scaling for x and y axes
ax.grid()

# Plot the outline of the flower bed
ax.plot(x, y, color='green', linewidth=2)

# Display the area as a text box in the center of the axes
ax.text(0.5, 0.5, f'A = {area:.1f} m²', transform=ax.transAxes,
        fontsize=12, bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

# Show the plot
plt.show()