"""Simulation of a vehicle coasting to a stop using solve_ivp."""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

# Simulation parameters
t_max = 200        # Total simulation time [s]
m = 15.0           # Mass of the vehicle [kg]
b = 2.5            # Friction coefficient [kg/m]
x0 = 0             # Initial position [m]
v0 = 10.0          # Initial velocity [m/s]

def F(v):
    """Return the friction force as a function of velocity v (quadratic drag)."""
    return -b * v * np.abs(v)

def ode_system(t, u):
    """Return the derivatives [dx/dt, dv/dt] for the ODE solver."""
    x, v = u
    return [v, F(v) / m]

# Initial state vector: [position, velocity] at t=0
u0 = [x0, v0]

# Solve the ODE system for the given time interval
result = scipy.integrate.solve_ivp(
    ode_system, [0, t_max], u0, dense_output=True
)

# Print solver status message
print(result.message)

# Extract time, position, and velocity arrays
t = result.t
x, v = result.y

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