"""Calculation of the relative error for the approximation sin(x) ≈ x.

This script computes the relative error (in percent) of the approximation
sin(x) ≈ x for angles from 1° to 45° in fine steps. The result is visualized
using matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

# Create an array of angles in degrees (1° to 45°)
angles_deg = np.linspace(1, 45, 500)

# Convert angles to radians
x = np.radians(angles_deg)

# Calculate the relative error in percent
# Error formula: (approximation - true value) / true value * 100%
relative_error = 100 * (x - np.sin(x)) / np.sin(x)

# Create the figure and axes for plotting
fig, ax = plt.subplots()
ax.set_title('Relative Error of the Approximation sin(x) ≈ x')
ax.set_xlabel('Angle [degrees]')
ax.set_ylabel('Relative Error [%]')
ax.set_xlim(0, np.max(angles_deg))
ax.set_ylim(0, np.max(relative_error))
ax.grid(True)

# Plot the error curve
ax.plot(angles_deg, relative_error, label='Relative Error')

# Add a legend for clarity
ax.legend()

# Show the plot
plt.show()