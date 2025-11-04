"""Simulation of a vehicle coasting to a stop using solve_ivp.

This script demonstrates the use of the dense_output option for interpolation.
It compares the numerical solution to the analytical solution for a vehicle
slowing down due to quadratic drag.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

# Simulation parameters
t_max = 200        # Total simulation time [s]
m = 10.0           # Mass of the vehicle [kg]
b = 2.5            # Friction coefficient [kg/m]
x0 = 0             # Initial position [m]
v0 = 10.0          # Initial velocity [m/s]

def F(v):
    """Return the drag force as a function of velocity v (quadratic drag)."""
    return -b * v * np.abs(v)

def ode_system(t, u):
    """Return the derivatives [dx/dt, dv/dt] for the ODE solver."""
    x, v = u
    return np.array([v, F(v) / m])

# Initial state vector: [position, velocity] at t=0
u0 = np.array([x0, v0])

# Solve the ODE system from t=0 to t=t_max with dense output for interpolation
result = scipy.integrate.solve_ivp(
    ode_system, [0, t_max], u0, dense_output=True
)

# Print solver status message
print(result.message)

# Extract time and state arrays at solver points
t_points = result.t
x_points, v_points = result.y

# Create a fine time grid for smooth interpolation and plotting
t_fine = np.linspace(0, t_max, 1000)
x_fine, v_fine = result.sol(t_fine)

# Analytical solutions for comparison
x_analytical = m / b * np.log(1 + v0 * b / m * t_fine)
v_analytical = v0 / (1 + v0 * b / m * t_fine)

# Create figure and subplots
fig = plt.figure(figsize=(9, 4))
fig.set_tight_layout(True)

# Plot velocity vs. time
ax_vel = fig.add_subplot(1, 2, 1)
ax_vel.set_xlabel('$t$ [s]')
ax_vel.set_ylabel('$v$ [m/s]')
ax_vel.grid()
ax_vel.plot(t_fine, v_analytical, '-b', label='Analytical')
ax_vel.plot(t_points, v_points, '.r', label='Simulated (solver points)')
ax_vel.plot(t_fine, v_fine, '-r', label='Simulated (interpolated)')
ax_vel.legend()

# Plot position vs. time
ax_pos = fig.add_subplot(1, 2, 2)
ax_pos.set_xlabel('$t$ [s]')
ax_pos.set_ylabel('$x$ [m]')
ax_pos.grid()
ax_pos.plot(t_fine, x_analytical, '-b', label='Analytical')
ax_pos.plot(t_points, x_points, '.r', label='Simulated (solver points)')
ax_pos.plot(t_fine, x_fine, '-r', label='Simulated (interpolated)')
ax_pos.legend()

# Show the plots
plt.show()