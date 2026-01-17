"""Simulation of Planetary Elliptical Orbit Animation

Simulates a planet orbiting a star in an elliptical orbit based on Kepler's laws.
The animation shows:
- A planet (blue) moving in an elliptical orbit
- A star (red) at one of the focal points
- Smooth orbital motion with proper elliptical geometry

The ellipse follows the equation: x²/a² + y²/b² = 1
where a is the semi-major axis and b is the semi-minor axis.
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

# Create output directory for saved animation
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Orbital parameters
STAR_RADIUS = 0.5      # Radius of the star
PLANET_RADIUS = 0.25   # Radius of the planet
SEMI_MAJOR_AXIS = 8    # Semi-major axis of the ellipse (a)
SEMI_MINOR_AXIS = 4    # Semi-minor axis of the ellipse (b)
VIEW_WIDTH = 10        # Width of the viewing area

# Calculate focal distance: c = sqrt(a² - b²)
FOCAL_DISTANCE = np.sqrt(SEMI_MAJOR_AXIS**2 - SEMI_MINOR_AXIS**2)

# Colors
STAR_COLOR = 'orange'
PLANET_COLOR = 'dodgerblue'
ORBIT_COLOR = 'gray'
BACKGROUND_COLOR = 'black'


def init():
    """Initialize the animation by setting up the initial planet position."""
    # Start planet at aphelion (farthest point from star)
    x_start = SEMI_MAJOR_AXIS
    y_start = 0
    planet.center = (x_start, y_start)
    return planet,


def animate_orbit(frame):
    """Update planet position for each animation frame.
    
    Args:
        frame: Current frame number (0-359 degrees)
        
    Returns:
        Tuple containing the updated planet patch
    """
    # Convert frame to radians
    angle = np.radians(frame)
    
    # Calculate position on ellipse
    x = SEMI_MAJOR_AXIS * np.cos(angle)
    y = SEMI_MINOR_AXIS * np.sin(angle)
    
    # Update planet position
    planet.center = (x, y)
    
    return planet,


def create_orbit_path():
    """Create the elliptical orbit path for visualization."""
    theta = np.linspace(0, 2 * np.pi, 100)
    x = SEMI_MAJOR_AXIS * np.cos(theta)
    y = SEMI_MINOR_AXIS * np.sin(theta)
    return x, y


# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 8), facecolor=BACKGROUND_COLOR)
ax.set_facecolor(BACKGROUND_COLOR)

# Set axis limits with some padding
ax.set_xlim(-VIEW_WIDTH, VIEW_WIDTH)
ax.set_ylim(-VIEW_WIDTH, VIEW_WIDTH)

# Create the planet (starts at aphelion)
planet = mpl.patches.Circle(
    (SEMI_MAJOR_AXIS, 0),
    radius=PLANET_RADIUS,
    color=PLANET_COLOR,
    zorder=3
)

# Create the star at one focal point
star = mpl.patches.Circle(
    (FOCAL_DISTANCE, 0),
    radius=STAR_RADIUS,
    color=STAR_COLOR,
    zorder=2
)

# Draw the elliptical orbit path
orbit_x, orbit_y = create_orbit_path()
ax.plot(orbit_x, orbit_y, color=ORBIT_COLOR, linestyle='--', 
        linewidth=1, alpha=0.5, label='Orbit Path')

# Add objects to the plot
ax.add_patch(planet)
ax.add_patch(star)

# Mark the focal points
ax.plot(FOCAL_DISTANCE, 0, 'x', color='red', markersize=10, 
        markeredgewidth=2, label='Focus (Star)')
ax.plot(-FOCAL_DISTANCE, 0, 'x', color='white', markersize=10, 
        markeredgewidth=2, alpha=0.5, label='Empty Focus')

# Configure axis appearance
ax.set_aspect('equal')
ax.grid(True, alpha=0.3, color='gray', linestyle=':')
ax.set_xlabel('X (AU)', color='white', fontsize=12)
ax.set_ylabel('Y (AU)', color='white', fontsize=12)
ax.set_title('Elliptical Planetary Orbit Animation', 
             color='white', fontsize=14, fontweight='bold')

# Customize tick colors
ax.tick_params(colors='white')

# Add legend
legend = ax.legend(loc='upper right', facecolor='black', 
                   edgecolor='white', fontsize=10)
for text in legend.get_texts():
    text.set_color('white')

# Add orbital parameters text
info_text = (
    f"Semi-major axis (a): {SEMI_MAJOR_AXIS} AU\n"
    f"Semi-minor axis (b): {SEMI_MINOR_AXIS} AU\n"
    f"Eccentricity: {FOCAL_DISTANCE/SEMI_MAJOR_AXIS:.3f}\n"
    f"Focal distance: {FOCAL_DISTANCE:.2f} AU"
)
ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
        verticalalignment='top', fontsize=9, color='white',
        bbox=dict(boxstyle='round', facecolor='black', 
                  alpha=0.7, edgecolor='white'))

# Create the animation
animation = FuncAnimation(
    fig,
    animate_orbit,
    init_func=init,
    frames=360,        # One full orbit (360 degrees)
    interval=20,       # 20ms between frames (50 FPS)
    blit=True,
    repeat=True
)

# Save animation as GIF
try:
    output_file = f"{OUTPUT_DIR}/elliptical_orbit.gif"
    print("Saving animation... (this may take a moment)")
    animation.save(output_file, writer='pillow', fps=30, dpi=100)
    print(f"✓ Animation saved to: {output_file}")
except Exception as e:
    print(f"✗ Could not save animation: {e}")

# Try to display the plot (only works with interactive backend)
plt.tight_layout()
try:
    # Check if we have an interactive backend
    if plt.get_backend() != 'agg':
        plt.show()
    else:
        print("\nNote: Running in non-interactive mode. Animation saved to file.")
except Exception as e:
    print(f"Could not display plot: {e}")

print("\n" + "=" * 60)
print("Animation completed!")
print("=" * 60)
