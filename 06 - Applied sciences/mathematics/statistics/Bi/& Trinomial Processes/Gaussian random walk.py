# Visualize a Gaussian (normal) random walk

import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
steps = 200                # Number of steps in the random walk
start_position = 0         # Starting position
mu = 0                     # Mean of the normal distribution
sigma = 1                  # Standard deviation of the normal distribution

# --- Simulate the Gaussian random walk ---
# Each step is drawn from a normal distribution (mu, sigma)
steps_array = np.random.normal(mu, sigma, steps)
positions = np.cumsum(np.insert(steps_array, 0, start_position))

# --- Plot the Gaussian random walk ---
plt.figure(figsize=(10, 5))
plt.plot(positions, marker='o', markersize=2, linestyle='-', color='blue', label='Gaussian Random Walk')
plt.title("Gaussian (Normal) Random Walk")
plt.xlabel("Step")
plt.ylabel("Position")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()