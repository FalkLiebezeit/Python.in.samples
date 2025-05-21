"""
Copilot:
Create a Python program that calculates Pi.

How It Works:
- Generates Random Points: Each point (x, y) falls within a square ranging from -1 to 1.
- Checks If Inside Circle: If x² + y² ≤ 1, the point is considered inside.
- Plots Points:
- Blue Points: Inside the circle.
- Red Points: Outside the circle.
- Pi Approximation: Uses Monte Carlo estimation: (inside_circle / total_samples) * 4.


"""

import random
import matplotlib.pyplot as plt

def estimate_pi(num_samples):
    inside_circle = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []

    for _ in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)  # Generate random points
        if x**2 + y**2 <= 1:  # Check if point lies inside the unit circle
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_estimate = (inside_circle / num_samples) * 4  # Approximate Pi
    return pi_estimate, x_inside, y_inside, x_outside, y_outside

# Set number of samples
num_samples = 10000
estimated_pi, x_inside, y_inside, x_outside, y_outside = estimate_pi(num_samples)

# Plot the points
plt.figure(figsize=(6, 6))
plt.scatter(x_inside, y_inside, color="blue", s=1, label="Inside Circle")
plt.scatter(x_outside, y_outside, color="red", s=1, label="Outside Circle")
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Monte Carlo Pi Estimation ({num_samples} samples)\nEstimated Pi: {estimated_pi:.5f}")
plt.legend()
plt.show()

