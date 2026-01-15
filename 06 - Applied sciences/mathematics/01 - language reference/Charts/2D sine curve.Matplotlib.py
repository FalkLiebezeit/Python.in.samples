import matplotlib.pyplot as plt
import numpy as np

# Generate 100 evenly spaced values from 0 to 10
x = np.linspace(0, 10, 100)
# Compute the sine of each x value
y = np.sin(x)

# Create a new figure with a specific size
plt.figure(figsize=(8, 5))

# Plot the sine curve with a dashed blue line and label
plt.plot(x, y, label="Sine Curve", color="blue", linestyle="--")

# Set axis labels and plot title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Matplotlib Example")

# Show legend and grid for better readability
plt.legend()
plt.grid(True)

# Display the plot
plt.show()