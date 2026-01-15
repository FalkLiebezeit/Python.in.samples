import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime  # For displaying today's date

# --- Parameters for the Gaussian ---
sigma = 1      # Standard deviation
mu = 0         # Mean

# --- Create grid for 3D surface ---
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
x, y = np.meshgrid(x, y)

# --- Compute 3D Gaussian values ---
z = (1 / (2 * np.pi * sigma**2)) * np.exp(-((x - mu)**2 + (y - mu)**2) / (2 * sigma**2))

# --- Create and customize the plot ---
fig = plt.figure(figsize=(14, 10), facecolor='darkgray')  # Larger figure, dark gray background
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('darkgray')  # Set axes background to dark gray

# Plot the Gaussian surface
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# --- Set plot titles and labels ---
ax.set_title('3D Gaussian Bell Curve', fontsize=16, fontweight='bold')
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)

# --- Add instructions and today's date ---
ax.text2D(0.5, 0.95, "Use your mouse to turn surface", fontsize=12, ha='center', transform=ax.transAxes)
today = datetime.today().strftime('%Y-%m-%d')
ax.text2D(0.91, 0.99, f"Date: {today}", fontsize=10, ha='left', va='top', transform=ax.transAxes)

plt.tight_layout()
plt.show()