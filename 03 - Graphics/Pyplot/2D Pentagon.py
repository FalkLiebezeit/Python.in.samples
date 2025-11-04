import matplotlib.pyplot as plt
import numpy as np

# --- Parameters ---
n_sides = 5  # Number of sides for the pentagon

# --- Calculate angles for vertices (include last point to close the shape) ---
angles = np.linspace(0, 2 * np.pi, n_sides + 1)

# --- Calculate (x, y) coordinates for pentagon vertices on the unit circle ---
x = np.cos(angles)
y = np.sin(angles)

# --- Create and customize the plot ---
plt.figure(figsize=(6, 6))  # Slightly larger figure for better visibility
plt.plot(x, y, 'b-', linewidth=2, label='Pentagon Edge')  # Draw pentagon edges
plt.fill(x, y, 'skyblue', alpha=0.6, label='Pentagon Area')  # Fill pentagon
plt.scatter(x[:-1], y[:-1], color='red', zorder=5, label='Vertices')  # Mark vertices

plt.axis('equal')  # Equal scaling for x and y axes
plt.title('2D Pentagon', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()