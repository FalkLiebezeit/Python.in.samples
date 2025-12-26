"""Simulation of a cannon shot with Coriolis force and air resistance.

This script simulates the trajectory of a projectile (cannonball) considering
gravity, air resistance (quadratic drag), and the Coriolis force due to Earth's rotation.
The results are visualized as side and top views of the trajectory.
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

# Physical and environmental parameters
m = 14.5  # Mass of the projectile [kg]
cwA = 0.45 * math.pi * (8e-2) ** 2  # Drag coefficient times cross-sectional area [m²]
alpha = math.radians(42.0)          # Launch angle [rad]
h = 10.0                            # Launch height [m]
v0_magnitude = 150.0                # Muzzle velocity [m/s]
g = 9.81                            # Gravitational acceleration [m/s²]
rho = 1.225                         # Air density [kg/m³]
latitude = math.radians(49.4)       # Geographic latitude [rad]
omega_earth = 7.292e-5              # Earth's angular velocity [rad/s]

# Initial position and velocity vectors
r0 = np.array([0, 0, h])
v0 = v0_magnitude * np.array([math.cos(alpha), 0, math.sin(alpha)])

# Earth's angular velocity vector at the given latitude
omega = omega_earth * np.array([0, math.cos(latitude), math.sin(latitude)])

def force(v):
    """Compute the total force on the projectile as a function of velocity v.

    Includes gravity, air resistance (quadratic drag), and Coriolis force.
    """
    F_drag = -0.5 * rho * cwA * np.linalg.norm(v) * v        # Air resistance
    F_gravity = m * g * np.array([0, 0, -1])                 # Gravity
    F_coriolis = -2 * m * np.cross(omega, v)                 # Coriolis force
    return F_gravity + F_drag + F_coriolis

def ode_system(t, u):
    """Right-hand side of the ODE system for position and velocity."""
    r, v = np.split(u, 2)
    return np.concatenate([v, force(v) / m])

def hit_ground_event(t, u):
    """Event function: Detect when the projectile hits the ground (z=0)."""
    r, v = np.split(u, 2)
    return r[2]

# Stop integration when the projectile hits the ground
hit_ground_event.terminal = True

# Initial state vector: position and velocity at t=0
u0 = np.concatenate((r0, v0))

# Integrate the equations of motion until the projectile hits the ground
result = scipy.integrate.solve_ivp(
    ode_system, [0, np.inf], u0,
    events=hit_ground_event,
    dense_output=True
)

# Extract time and state arrays at solver points
t_points = result.t
r_points, v_points = np.split(result.y, 2)

# Interpolate the trajectory on a fine time grid for smooth plotting
t_fine = np.linspace(0, np.max(t_points), 1000)
r_fine, v_fine = np.split(result.sol(t_fine), 2)

# Create a figure for the plots
fig = plt.figure(figsize=(9, 6))
fig.set_tight_layout(True)

# Plot the trajectory in side view (x-z plane)
ax_side = fig.add_subplot(2, 1, 1)
ax_side.tick_params(labelbottom=False)
ax_side.set_ylabel('$z$ [m]')
ax_side.set_aspect('equal')
ax_side.grid()
ax_side.plot(r_points[0], r_points[2], '.b', label='Solver points')
ax_side.plot(r_fine[0], r_fine[2], '-b', label='Interpolated')
ax_side.legend(loc='best')

# Plot the trajectory in top view (x-y plane)
ax_top = fig.add_subplot(2, 1, 2, sharex=ax_side)
ax_top.set_xlabel('$x$ [m]')
ax_top.set_ylabel('$y$ [m]')
ax_top.grid()
ax_top.plot(r_points[0], r_points[1], '.b', label='Solver points')
ax_top.plot(r_fine[0], r_fine[1], '-b', label='Interpolated')
ax_top.legend(loc='best')

# Show the plots
plt.show()