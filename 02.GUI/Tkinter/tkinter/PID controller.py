# PID controller step response simulation using Tkinter
# Optimized and commented for clarity

import tkinter as tk

# --- Main window setup ---
main = tk.Tk()
main.title("Step Response of P, PI, and PID Controllers")
xmax, ymax = 800, 400

# Variable to store the selected controller type
controller_type = tk.StringVar(value="PID")

# Create the canvas for plotting
canZ = tk.Canvas(main, width=xmax, height=ymax, bg='white')

def clear_canvas():
    """Clear all drawings from the canvas."""
    canZ.delete("all")

def simulate_controller():
    """
    Simulate and plot the step response for P, PI, or PID controller
    based on the selected controller type.
    """
    tmax = 400      # Simulation time [arbitrary units]
    Kp = 50         # Proportional gain
    Tn = 50         # Integral time constant
    Tv = 50         # Derivative time constant
    e = 1           # Step input (error)
    t = 0
    ui = 0
    e0 = 0
    ur = 0
    dt = 2
    sx = xmax / tmax  # Scaling factor for time axis
    u2_t = []

    while t <= tmax:
        up = Kp * e
        ui += Kp * e * dt / Tn
        ud = Kp * Tv * (e - e0) / dt
        e0 = e
        t += dt

        # Select controller output based on user choice
        if controller_type.get() == "P":
            ur = up
        elif controller_type.get() == "PI":
            ur = up + ui
        elif controller_type.get() == "PID":
            ur = up + ui + ud

        # Store the (x, y) points for plotting
        u2_t.append(sx * t)
        u2_t.append(int(-ur) + ymax)

    # Draw the response curve
    canZ.create_line(u2_t, fill='blue', width=2)

# --- Controller selection radio buttons ---
optP = tk.Radiobutton(main, text="P Controller", variable=controller_type, value="P")
optPI = tk.Radiobutton(main, text="PI Controller", variable=controller_type, value="PI")
optPID = tk.Radiobutton(main, text="PID Controller", variable=controller_type, value="PID")

# --- Control buttons ---
btn_start = tk.Button(main, text="Start", command=simulate_controller)
btn_clear = tk.Button(main, text="Clear", command=clear_canvas)

# --- Layout ---
canZ.pack()
optP.pack(side="left")
optPI.pack(side="left")
optPID.pack(side="left")
btn_start.pack(side="left")
btn_clear.pack(side="left")

# --- Start the Tkinter event loop ---
main.mainloop()