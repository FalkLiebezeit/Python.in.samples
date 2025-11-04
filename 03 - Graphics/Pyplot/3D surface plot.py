"""
Ki:

This Python script generates a 3D surface plot using `matplotlib` and `numpy`. Here’s a breakdown of what it does:

1. **Import Libraries**  
   The script imports:
   - `numpy` for numerical computations.
   - `matplotlib.pyplot` for plotting.
   - `matplotlib.cm` for color mapping.

2. **Set Plot Style**  
   The `ggplot` style is applied to enhance the plot aesthetics.

3. **Generate Data**  
   - `X` and `Y` grids are created using `np.linspace` to define a range of values from -5 to 5.
   - `np.meshgrid(X, Y)` turns these arrays into a grid.
   - `Z` values are computed based on `sin(sqrt(X**2 + Y**2))`, forming a radial wave-like pattern.

4. **Create Figure & Axes**  
   - A 3D plot is initialized using `plt.subplots()`, with `figsize=(10, 7)` to enlarge the display.
   - The background color is set to **light gray** using `ax.set_facecolor("lightgray")`.

5. **Plot the Surface**  
   - The surface is plotted with `ax.plot_surface(X, Y, Z)`.
   - The color map is set to **Blues** for a smooth gradient.
   - `vmin=Z.min()` and `vmax=Z.max()` ensure proper color scaling.
   - `rstride=1` and `cstride=1` define the grid resolution for rendering.

6. **Add Text Instruction**  
   - A label `"use your mouse to turn surface"` is placed using `ax.text2D()`, helping users understand interaction.

7. **Remove Axis Labels**  
   - `ax.set_xticks([])`, `ax.set_yticks([])`, and `ax.set_zticks([])` remove tick labels for a cleaner display.

8. **Show the Plot**  
   - `plt.show()` renders the 3D surface visualization.

This creates an interactive **3D sinusoidal surface** where users can rotate the view with the mouse. Would you like any refinements or additional features? 🚀
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

plt.style.use('ggplot')

# Create data grid
X = np.linspace(-5, 5, 40)
Y = np.linspace(-5, 5, 40)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create figure with larger size
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw={"projection": "3d"})

# Set background color to light gray
ax.set_facecolor("lightgray")

# Plot the surface
ax.plot_surface(X, Y, Z, cmap=cm.Blues, vmin=Z.min(), vmax=Z.max(), rstride=1, cstride=1)

# Add text to the plot
ax.text2D(0.5, 0.9, "use your mouse to turn surface", fontsize=12, ha='center', transform=ax.transAxes)

# Remove axis labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

plt.show()