"""Simulation of a vehicle coasting to a stop: Euler method."""

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
t_max = 20        # Total simulation time [s]
dt = 0.2          # Time step [s]
m = 15.0          # Mass of the vehicle [kg]
b = 2.5           # Friction coefficient [kg/m]
x0 = 0            # Initial position [m]
v0 = 10.0         # Initial velocity [m/s]

def F(v):
    """Return the friction force as a function of velocity v."""
    return -b * v * np.abs(v)  # Quadratic drag

# Prepare time array and result arrays for position and velocity
t = np.arange(0, t_max + dt, dt)
x = np.empty_like(t)
v = np.empty_like(t)

# Set initial conditions
x[0] = x0
v[0] = v0

# Euler integration loop
for i in range(t.size - 1):
    x[i + 1] = x[i] + v[i] * dt
    v[i + 1] = v[i] + F(v[i]) / m * dt

# Analytical solutions for comparison
v_analytical = v0 / (1 + v0 * b / m * t)
x_analytical = m / b * np.log(1 + v0 * b / m * t)

# Create figure and subplots
fig, (ax_vel, ax_pos) = plt.subplots(1, 2, figsize=(10, 4), tight_layout=True)

# Plot velocity vs. time
ax_vel.set_xlabel('Time $t$ [s]')
ax_vel.set_ylabel('Velocity $v$ [m/s]')
ax_vel.grid(True)
ax_vel.plot(t, v_analytical, '-b', label='Analytical')
ax_vel.plot(t, v, '.r', label='Simulated')
ax_vel.legend()

# Plot position vs. time
ax_pos.set_xlabel('Time $t$ [s]')
ax_pos.set_ylabel('Position $x$ [m]')
ax_pos.grid(True)
ax_pos.plot(t, x_analytical, '-b', label='Analytical')
ax_pos.plot(t, x, '.r', label='Simulated')
ax_pos.legend()

# Show the plots
plt.show()