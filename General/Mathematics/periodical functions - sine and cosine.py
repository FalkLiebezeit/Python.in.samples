"""
Copilot:

Write a Python program. 
The program should plot a sine and a cosine curve in the domain from -2 pi to 2 pi.

answer:
This program uses numpy to create an array of (x) values and then computes the sine and cosine values. 
It then plots both curves with Matplotlib, adding a legend, grid, and axis lines for clarity. 

"""

import numpy as np
import matplotlib.pyplot as plt

# Define the domain
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y_sin, label="sin(x)", color="blue")
plt.plot(x, y_cos, label="cos(x)", color="red")

# Add labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine and Cosine Curves")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid()

# Show the plot
plt.show()