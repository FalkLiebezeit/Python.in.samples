import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parameters ---
l = 1.0        # Pendulum length (m)
initial_angle_deg = 60  # Initial angle (degrees)
damping = 0.0           # Damping coefficient
mass = 10               # Mass (kg)
tmax = 50               # Simulation duration (s)
g = 9.81                # Gravitational acceleration (m/s^2)
omega_sq = g / l        # Square of angular frequency

# --- Time setup ---
dt = 1e-3               # Time step (s)
t = np.arange(0, tmax, dt)
n_steps = len(t)

# --- State arrays ---
phi = np.radians(initial_angle_deg)  # Initial angle (radians)
omega = 0.0                         # Initial angular velocity
x = np.empty(n_steps)
y = np.empty(n_steps)
v = np.empty(n_steps)

# --- Initial position ---
x[0] = l * np.sin(phi)
y[0] = -l * np.cos(phi)
v[0] = l * omega

# --- Euler integration for pendulum motion ---
for i in range(1, n_steps):
    # Update angle and angular velocity
    phi += omega * dt
    omega += (-omega_sq * np.sin(phi) - damping * omega) * dt
    v[i] = l * omega
    x[i] = l * np.sin(phi)
    y[i] = -l * np.cos(phi)

# --- Animation function ---
def animate(frame):
    """
    Update the pendulum animation for the given frame.
    """
    h = l + y[frame]  # Height above reference
    E_pot = mass * g * h
    E_kin = 0.5 * mass * v[frame] ** 2
    txtEpot.set_text(r'$E_{pot}$ = %.1f J' % E_pot)
    txtEkin.set_text(r'$E_{kin}$ = %.1f J' % E_kin)
    rod.set_data([0, x[frame]], [0, y[frame]])
    bob.set_data([x[frame]], [y[frame]])
    return rod, bob, txtEpot, txtEkin

# --- Plot setup ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.set(xlabel='x', ylabel='y')
width = 1.1 * l
ax.axis([-width, width, -width, width])
ax.plot(0, 0, 'ko')  # Pivot point

# --- Plot elements ---
rod, = ax.plot([], [], 'b-', lw=1)  # Pendulum rod
bob, = ax.plot([], [], 'ro', markersize=15)  # Pendulum bob
txtEpot = ax.text(-l, l, '', fontsize=12)
txtEkin = ax.text(-l, 0.85 * l, '', fontsize=12)

# --- Animation ---
interval_ms = dt * 1e3
ani = FuncAnimation(
    fig, animate, frames=n_steps, interval=interval_ms, blit=True
)

plt.show()

# --- Optional: Save figure ---
# fig.savefig('pendulum.png')
# fig.savefig('pendulum.svg')