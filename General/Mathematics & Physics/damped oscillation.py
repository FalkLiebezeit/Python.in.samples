"""
KI:

Write a Python program. 
The program should graphically display a damped oscillation. 
Optimize and comment the program.

answer:

Optimizations & Explanations:
- Use of np.linspace for smooth curve  Creates an array of 1000 time points for better resolution.
- Mathematical formulation  Implements the damped oscillation equation:
[ x(t) = A e^{-\gamma t} \cos(\omega t) ]
- Enhanced readability  The program uses well-chosen variable names and proper comments.
- Formatted plot Includes axis labels, grid lines, legend, and a title for better visualization.

This will generate a clean oscillation plot where the amplitude decreases over time due to damping.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the damped oscillation
A = 1      # Initial amplitude
gamma = 0.2  # Damping coefficient
omega = 5  # Angular frequency
t = np.linspace(0, 10, 1000)  # Time array from 0 to 10 with 1000 points

# Compute the damped oscillation
x = A * np.exp(-gamma * t) * np.cos(omega * t)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(t, x, label="Damped Oscillation", color="b")

# Label axes and add title
plt.xlabel("Time (s)")
plt.ylabel("Displacement")
plt.title("Damped Oscillation")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()