# PID controller with 2nd order process (simulation and plot using Tkinter)
# Optimized and commented for clarity

import tkinter as tk

# --- Main window setup ---
main = tk.Tk()
main.title("PID Controller with 2nd Order Process")
xmax, ymax = 800, 400

# Create the canvas for plotting
canZ = tk.Canvas(main, width=xmax, height=ymax, bg='white')

# --- System and controller parameters ---
U1 = 100.0        # Setpoint (reference input)
R, L = 1, 25      # Resistance [Ohm], Inductance [mH]
I, M, J = 40, 170, 1  # Armature current [A], Torque [Nm], Inertia [kgm^2]
C = 1e3 * J * (I / M) ** 2  # System constant
tmax = 250        # Simulation time [ms]
Kp = 5            # Proportional gain
Tn = 50           # Integral time [ms]
Tv = 10           # Derivative time [ms]
dt = 0.25         # Time step [ms]
sx = xmax / tmax  # Scaling factor for time axis

# --- Simulation variables ---
t = 0.0           # Time
i = 0.0           # Current
y = 0.0           # Output (process variable)
ui = 0.0          # Integral term
e = 0.0           # Error
e0 = 0.0          # Previous error
w = ymax / 2      # Setpoint for plotting (center line)
u2_t = []         # List to store curve points

# --- Simulation loop (Euler integration) ---
while t <= tmax:
    e = w - y
    up = Kp * e
    ud = Kp * Tv * (e - e0) / dt
    ui += Kp * e * dt / Tn
    U1_ctrl = up + ui + ud
    i += (U1_ctrl - R * i - y) * dt / L
    y += i * dt / C
    t += dt
    e0 = e
    u2_t.append(sx * t)
    u2_t.append(-y + ymax)

# --- Plot the response curve and setpoint/reference line ---
canZ.create_line(u2_t, fill='blue', width=2, smooth=True)
canZ.create_line(0, w, xmax, w, fill='red', width=2)

canZ.pack()
main.mainloop()