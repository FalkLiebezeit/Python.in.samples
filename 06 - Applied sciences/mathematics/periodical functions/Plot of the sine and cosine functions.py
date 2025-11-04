"""Plot of the sine and cosine functions with labels."""

import numpy as np
import matplotlib.pyplot as plt

# Create an array for x values in degrees from 0 to 360.
x = np.linspace(0, 360, 500)

# Calculate the sine and cosine values (convert degrees to radians).
y_sin = np.sin(np.radians(x))
y_cos = np.cos(np.radians(x))

# Create a figure and axes object.
fig, ax = plt.subplots(figsize=(8, 4))

# Set axis labels, title, limits, and grid.
ax.set_title('Sine and Cosine Functions')
ax.set_xlabel('Angle [degrees]')
ax.set_ylabel('Function value')
ax.set_xlim(0, 360)
ax.set_ylim(-1.1, 1.1)
ax.grid(True)

# Plot the sine and cosine curves with labels.
ax.plot(x, y_sin, label='Sine', color='blue')
ax.plot(x, y_cos, label='Cosine', color='red')
ax.legend(loc='upper right')

# Display the plot.
plt.tight_layout()
plt.show()