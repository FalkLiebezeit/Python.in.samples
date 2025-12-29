import numpy as np
import matplotlib.pyplot as plt

# Generate x values from -2 to 6 with a step of 0.01
x = np.arange(-2, 6, 0.01)

# Compute the corresponding y values for the cubic polynomial
y = x**3 - 7 * x**2 + 7 * x + 15

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="y = $x^3 - 7x^2 + 7x + 15$", color="blue")

# Add axis labels and a title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of the Cubic Polynomial Function")
plt.legend()
plt.grid(True)

# Display the plot  
plt.show()  
