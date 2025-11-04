"""Coriolis deflection of a vertically thrown mass.

This script simulates a mass thrown vertically upward,
taking into account the Coriolis force due to Earth's rotation.
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

# Initial position vector [m] (starting at the origin)
r0 = np.array([0, 0, 0.0])
# Initial velocity vector [m/s] (straight up)
v0 = np.array([0.0, 0.0, 44.29])
# Geographic latitude [radians]
latitude = math.radians(49.4)
# Magnitude of Earth's angular velocity [rad/s]
omega_earth = 7.292e-5
# Gravitational acceleration [m/s²]
g = 9.81

# Earth's angular velocity vector [rad/s] at the given latitude
omega = omega_earth * np.array([0, math.cos(latitude), math.sin(latitude)])

def rhs(t, u):
    """Compute the right-hand side of the ODE system (state derivatives).

    Args:
        t (float): Current time (not used, as the system is time-invariant)
        u (ndarray): State vector [x, y, z, vx, vy, vz]

    Returns:
        ndarray: Derivative of state vector
    """
    r, v = np.split(u, 2)
    # Gravitational acceleration (downwards)
    a_g = g * np.array([0, 0, -1])
    # Coriolis acceleration
    a_c = -2 * np.cross(omega, v)
    # Total acceleration
    a = a_g + a_c
    return np.concatenate([v, a])

def hit_ground_event(t, u):
    """Event function: Detect when the mass reaches the ground (z=0).

    Returns positive above ground, zero at ground, negative below.
    """
    r, v = np.split(u, 2)
    return r[2]

# Stop the integration when the event occurs (when z=0, falling down)
hit_ground_event.terminal = True
hit_ground_event.direction = -1

# Initial state vector: position and velocity at t=0
u0 = np.concatenate((r0, v0))

# Integrate the equations of motion until the mass hits the ground
result = scipy.integrate.solve_ivp(
    rhs, [0, np.inf], u0,
    events=hit_ground_event,
    dense_output=True
)

# Interpolate the solution on a fine time grid for smooth plotting
t = np.linspace(0, np.max(result.t), 1000)
r, v = np.split(result.sol(t), 2)

# Create a figure with three subplots for x, y, and z coordinates
fig = plt.figure(figsize=(9, 3))
fig.set_tight_layout(True)

# Plot x displacement over time (in millimeters)
ax_x = fig.add_subplot(1, 3, 1)
ax_x.set_xlabel('$t$ [s]')
ax_x.set_ylabel('$x$ [mm]')
ax_x.grid()
ax_x.plot(t, 1e3 * r[0], '-b')

# Plot y displacement over time (in micrometers)
ax_y = fig.add_subplot(1, 3, 2)
ax_y.set_xlabel('$t$ [s]')
ax_y.set_ylabel('$y$ [µm]')
ax_y.grid()
ax_y.plot(t, 1e6 * r[1], '-b')

# Plot z displacement over time (in meters)
ax_z = fig.add_subplot(1, 3, 3)
ax_z.set_xlabel('$t$ [s]')
ax_z.set_ylabel('$z$ [m]')
ax_z.grid()
ax_z.plot(t, r[2], '-b')

# Show the plots
plt.show()