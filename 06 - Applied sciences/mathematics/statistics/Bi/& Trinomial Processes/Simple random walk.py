# Simple random walk (binomial process) simulation and visualization

import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
steps = 100            # Number of steps in the random walk
start_position = 0     # Starting position

# --- Simulate the random walk ---
# At each step, move +1 or -1 with equal probability
moves = np.random.choice([-1, 1], size=steps)
positions = np.cumsum(np.insert(moves, 0, start_position))

# --- Plot the random walk ---
plt.figure(figsize=(8, 4))
plt.plot(positions, marker='o', markersize=3, linestyle='-', color='blue')
plt.title("Simple Random Walk (Irrfahrt)")
plt.xlabel("Step")
plt.ylabel("Position")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()