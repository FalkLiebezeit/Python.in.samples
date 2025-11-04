"""Motion of a mass on a rotating disk.

This program simulates the motion of a mass in the reference frame
of a rotating disk, considering Coriolis and centrifugal forces.
"""

import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation
import scipy.integrate

# Simulation time and time step [s]
T = 5.0
dt = 0.005

# Initial position [m] (on the disk)
r0 = np.array([0.1, 0, 0])
# Initial velocity [m/s]
v0 = np.array([0.0, 0.0, 0.0])
# Rotation frequency of the disk [Hz]
f = 1.0

# Angular velocity vector [rad/s]
omega = np.array([0, 0, 2 * math.pi * f])

def rhs(t, u):
    """Compute the right-hand side of the ODE system.

    Args:
        t (float): Current time (not used, as the system is time-invariant)
        u (ndarray): State vector [x, y, z, vx, vy, vz]

    Returns:
        ndarray: Derivative of state vector
    """
    r, v = np.split(u, 2)
    # Coriolis acceleration
    a_coriolis = -2 * np.cross(omega, v)
    # Centrifugal acceleration
    a_centrifugal = -np.cross(omega, np.cross(omega, r))
    # Total acceleration
    a = a_coriolis + a_centrifugal
    return np.concatenate([v, a])

# Initial state vector: position and velocity at t=0
u0 = np.concatenate((r0, v0))

# Numerically solve the equations of motion
result = scipy.integrate.solve_ivp(
    rhs, [0, T], u0, t_eval=np.arange(0, T, dt)
)
t = result.t
r, v = np.split(result.y, 2)

# Set up the figure and axes for plotting
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(1, 1, 1)
ax.set_aspect('equal')
ax.set_xlabel('$x$ [m]')
ax.set_ylabel('$y$ [m]')
ax.grid()

# Plot the trajectory (top view)
plot_path, = ax.plot(r[0], r[1], '-b', zorder=3, label='Trajectory')

# Create a point plot for the current position of the mass
plot_point, = ax.plot([], [], 'o', color='red', markersize=10, zorder=5, label='Mass')

def update(n):
    """Update the animation for the n-th time step."""
    # Update the position of the mass
    plot_point.set_data(r[0:2, n].reshape(-1, 1))
    # Plot the trajectory up to the current time
    plot_path.set_data(r[0:2, :n + 1])
    return plot_point, plot_path

# Create and start the animation
ani = mpl.animation.FuncAnimation(
    fig, update, frames=t.size, interval=30, blit=True
)
plt.legend()
plt.show()