"""
Copilot:
Create a Python program that generates and graphically displays data for a Gaussian bell curve.

Here's a Python program that generates data for a Gaussian (normal) bell curve and visually represents it using matplotlib and numpy.

"""

import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the Gaussian function
mean = 0      # Center of the bell curve
std_dev = 1   # Standard deviation
num_points = 1000  # Number of data points

# Generate x values
x = np.linspace(-5, 5, num_points)

# Compute Gaussian distribution
y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

# Plot the Gaussian bell curve
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Gaussian Distribution", color="blue")
plt.fill_between(x, y, color="lightblue", alpha=0.5)
plt.title("Gaussian Bell Curve")
plt.xlabel("x-axis")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()