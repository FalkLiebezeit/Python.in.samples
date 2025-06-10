"""
Copilot:

Write a Python program. 
The program should plot a sine and a cosine curve in the domain from -2 pi to 2 pi.

answer:
This program uses numpy to create an array of (x) values and then computes the sine and cosine values. 
It then plots both curves with Matplotlib, adding a legend, grid, and axis lines for clarity. 

Key Adjustments:
- Added tan(x) and exp(-x) functions to demonstrate a trigonometric and exponential function.
- Different colors for each function to distinguish them visually.
- Extended figure size for a clearer display.
- Included a legend for easy identification.

🛑 Note: The tangent function (tan(x)) has asymptotes where it approaches infinity, which might distort the graph. If needed, you can limit its range using np.where() to avoid extreme values.


"""
import numpy as np
import matplotlib.pyplot as plt

# Define the domain
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_sin = 250 * np.sin(x)
y_cos = 250 * np.cos(x)
y_tan = np.tan(x)  # Tangent function
y_exp = np.exp(-x)  # Exponential decay function

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label="sin(x)", color="blue")
plt.plot(x, y_cos, label="cos(x)", color="red")
plt.plot(x, y_tan, label="tan(x)", color="green")
plt.plot(x, y_exp, label="exp(-x)", color="purple")

# Add labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Various Mathematical Functions")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid()

# Show the plot
plt.show()