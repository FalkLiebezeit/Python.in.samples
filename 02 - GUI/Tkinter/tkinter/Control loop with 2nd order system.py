# Control loop with 2nd order system (PID controller simulation)
# Optimized and commented for clarity

import tkinter as tk

# --- Main window setup ---
main = tk.Tk()
main.title("Control Loop with 2nd Order System")
xmax, ymax = 800, 400
rd = 4  # Margin for the plot
U1 = 100.0  # Setpoint
w = ymax / 2  # Reference value for plotting
xy = 0  # Global variable for the curve handle

main.minsize(xmax, ymax)
main.resizable(False, False)

# --- Canvas for plotting ---
canZ = tk.Canvas(main, width=xmax, height=ymax, bg='white')
canZ.grid(row=0, column=0, columnspan=5)

def draw_frame():
    """Draw the plot frame and axes."""
    canZ.create_line(0, w, xmax, w, fill='red', width=2)  # Reference line
    canZ.create_line(rd, rd, xmax, rd, fill="black", width=2)
    canZ.create_line(rd, ymax, xmax, ymax, fill="black", width=2)
    canZ.create_line(rd, 0, rd, ymax, fill="black", width=2)
    canZ.create_line(xmax, rd, xmax, ymax, fill="black", width=2)

def clear_canvas():
    """Clear the response curve from the canvas."""
    global xy
    canZ.delete(xy)

def show_coordinates(event):
    """Display the time and output value at the mouse position."""
    tmax = float(txtTmax.get())
    x, y = event.x, event.y
    t = tmax * x / xmax - 2
    y_val = U1 * (ymax - y) / w
    lblKoordinate["text"] = f"t: {t:4.0f} ms  y: {y_val:3.0f}%"

def simulate_control_loop():
    """
    Simulate and plot the response of a PID-controlled 2nd order system.
    Parameters are read from the user input fields.
    """
    global xy
    # Read parameters from input fields
    tmax = float(txtTmax.get())
    Kp = float(txtKp.get())
    Tn = float(txtTn.get())
    Tv = float(txtTv.get())
    R = float(txtR.get())
    L = float(txtL.get())
    J = float(txtJ.get())
    Ia = float(txtIa.get())
    Mn = float(txtMn.get())
    # Calculate system constant
    C = 1.0e3 * J * (Ia / Mn) ** 2

    # Initialize simulation variables
    t = y = ui = ud = i = e = e0 = 0
    dt = 0.05
    sx = xmax / tmax  # Scaling for time axis
    u2_t = []

    # Euler integration loop
    while t <= tmax:
        e = w - y
        up = Kp * e
        ui += Kp * e * dt / Tn
        ud = Kp * Tv * (e - e0) / dt
        e0 = e
        U1_ctrl = up + ui + ud
        i += (U1_ctrl - R * i - y) * dt / L
        y += i * dt / C
        t += dt
        u2_t.append(sx * t + rd)
        u2_t.append(-y + ymax)
    xy = canZ.create_line(u2_t, fill='blue', width=2)

# --- Draw the frame once at startup ---
draw_frame()

# --- Input fields and labels ---
def add_entry(label, default, row, col):
    tk.Label(main, text=label).grid(row=row, column=col, sticky="w")
    entry = tk.Entry(main, width=5)
    entry.insert(0, str(default))
    entry.grid(row=row, column=col + 1, sticky="w")
    return entry

txtR = add_entry("R in Ohm", 1.5, 1, 0)
txtL = add_entry("L in mH", 24, 2, 0)
txtMn = add_entry("Mn in Nm", 172, 3, 0)
txtIa = add_entry("Ia in A", 41, 4, 0)
txtJ = add_entry("J in kgm^2", 1, 5, 0)
txtKp = add_entry("Kp", 5, 1, 2)
txtTn = add_entry("Tn in ms", 50, 2, 2)
txtTv = add_entry("Tv in ms", 5, 3, 2)
txtTmax = add_entry("tmax", 250, 4, 2)

tk.Label(main, text="Koordinate").grid(row=5, column=2, sticky="w")
lblKoordinate = tk.Label(main, width=15)
lblKoordinate.grid(row=5, column=3, sticky="w")

# --- Control buttons ---
tk.Button(main, text="Start", command=simulate_control_loop, width=7).grid(row=1, column=4)
tk.Button(main, text="Clear", command=clear_canvas, width=7).grid(row=2, column=4)
tk.Button(main, text="Exit", command=main.destroy, width=7).grid(row=3, column=4)

# --- Bind mouse motion to coordinate display ---
canZ.bind('<Motion>', show_coordinates)

main.mainloop()