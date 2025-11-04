"""Simulation of a highly elliptical planetary orbit using Newtonian gravity.

This script numerically solves the equations of motion for a planet orbiting a fixed Sun,
and animates the planet's trajectory, velocity, and acceleration vectors.
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation
import scipy.integrate

# Constants: 1 day, 1 year [s], and the astronomical unit [m]
DAY = 24 * 60 * 60
YEAR = 365.25 * DAY
AU = 1.495978707e11  # Astronomical unit in meters

# Scaling factors for displaying acceleration and velocity vectors
scal_a = 20      # [AU / (m/s²)]
scal_v = 1e-5    # [AU / (m/s)]

# Simulation time and time step [s]
t_max = 1 * YEAR
dt = 1 * DAY

# Initial position [m] and velocity [m/s] of the planet (highly elliptical orbit)
r0 = np.array([152.10e9, 0.0])
v0 = np.array([0.0, 15e3])

# Mass of the Sun [kg]
M = 1.9885e30

# Gravitational constant [m³ / (kg * s²)]
G = 6.6743e-11

def rhs(t, u):
    """Compute the right-hand side of the ODE system for position and velocity."""
    r, v = np.split(u, 2)
    a = -G * M * r / np.linalg.norm(r) ** 3
    return np.concatenate([v, a])

# Initial state vector: position and velocity at t=0
u0 = np.concatenate((r0, v0))

# Numerically solve the equations of motion with high accuracy
result = scipy.integrate.solve_ivp(
    rhs, [0, t_max], u0, rtol=1e-9, dense_output=True
)
t_points = result.t
r_points, v_points = np.split(result.y, 2)

# Interpolate the solution on a fine time grid for smooth animation
t_fine = np.arange(0, np.max(t_points), dt)
r_fine, v_fine = np.split(result.sol(t_fine), 2)

# Set up the figure and axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_aspect('equal')
ax.set_xlabel('$x$ [AU]')
ax.set_ylabel('$y$ [AU]')
ax.set_xlim(-0.2, 1.1)
ax.set_ylim(-0.6, 0.6)
ax.grid()

# Plot the planet's trajectory (both solver points and interpolated curve)
ax.plot(r_points[0] / AU, r_points[1] / AU, '.b', label='Solver Points')
ax.plot(r_fine[0] / AU, r_fine[1] / AU, '-b', label='Interpolated Path')

# Create point plots for the planet and the Sun
plot_planet, = ax.plot([], [], 'o', color='red', label='Planet')
plot_sun, = ax.plot([0], [0], 'o', color='gold', label='Sun')

# Create arrows for velocity and acceleration
arrow_style = mpl.patches.ArrowStyle.Simple(head_length=6, head_width=3)
arrow_v = mpl.patches.FancyArrowPatch((0, 0), (0, 0), color='red', arrowstyle=arrow_style)
arrow_a = mpl.patches.FancyArrowPatch((0, 0), (0, 0), color='black', arrowstyle=arrow_style)
ax.add_patch(arrow_a)
ax.add_patch(arrow_v)

# Add a text box for the elapsed time
text_t = ax.text(0.01, 0.95, '', color='blue', transform=ax.transAxes)

def update(n):
    """Update the animation for the n-th time step."""
    t = t_fine[n]
    r = r_fine[:, n]
    v = v_fine[:, n]

    # Compute the current acceleration
    u_dot = rhs(t, np.concatenate([r, v]))
    a = np.split(u_dot, 2)[1]

    # Update the planet's position and the arrows
    plot_planet.set_data(r.reshape(-1, 1) / AU)
    arrow_a.set_positions(r / AU, r / AU + scal_a * a)
    arrow_v.set_positions(r / AU, r / AU + scal_v * v)

    # Update the time text
    text_t.set_text(f'$t$ = {t / DAY:.0f} d')

    return plot_planet, arrow_v, arrow_a, text_t

# Create and start the animation
ani = mpl.animation.FuncAnimation(
    fig, update, frames=t_fine.size, interval=30, blit=True
)
ax.legend()
plt.show()