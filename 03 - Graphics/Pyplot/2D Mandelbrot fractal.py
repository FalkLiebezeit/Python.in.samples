import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    Compute the number of iterations for a point c to escape the Mandelbrot set.
    Returns the iteration count (up to max_iter).
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Generate the Mandelbrot set for the specified region and resolution.
    Returns the grid of iteration counts.
    """
    x_vals = np.linspace(xmin, xmax, width)
    y_vals = np.linspace(ymin, ymax, height)
    mandelbrot_grid = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            mandelbrot_grid[i, j] = mandelbrot(x_vals[i] + 1j * y_vals[j], max_iter)

    return x_vals, y_vals, mandelbrot_grid

# --- Parameters for the Mandelbrot set ---
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5  # Region in the complex plane
width, height = 1600, 1200                     # Increased resolution for a bigger, sharper image
max_iter = 256                                 # Maximum number of iterations

# --- Generate Mandelbrot set data ---
x_vals, y_vals, mandelbrot_grid = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

# --- Plot the Mandelbrot set ---
plt.figure(figsize=(16, 12))  # Larger window for better visibility
plt.imshow(
    mandelbrot_grid.T, 
    extent=[xmin, xmax, ymin, ymax], 
    cmap='hot', 
    origin='lower', 
    aspect='auto'
)
plt.axis('off')  # Hide axes for a cleaner look
plt.colorbar(label='Iteration count')
plt.title("Mandelbrot Set", fontsize=16, fontweight='bold')
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.tight_layout()
plt.savefig('mandelbrot_fractal.png', dpi=150, bbox_inches='tight')
print("Mandelbrot-Fraktal wurde als 'mandelbrot_fractal.png' gespeichert")
# plt.show()  # Deaktiviert für nicht-interaktive Umgebungen