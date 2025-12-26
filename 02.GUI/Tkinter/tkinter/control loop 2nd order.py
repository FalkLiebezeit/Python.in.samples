import tkinter as tk

def clear_canvas():
    """Clear all drawings from the canvas."""
    canZ.delete("all")

def simulate_second_order_system():
    """
    Simulate and plot the response of a second-order control system (Regelstrecke 2. Ordnung)
    using the parameters provided by the user.
    """
    w = ymax / 2  # Vertical center for the axis
    U1 = w        # Input voltage (centered for plotting)
    try:
        # Read and convert user input values
        R = float(txtR.get())
        L = float(txtL.get())
        J = float(txtJ.get())
        Ia = float(txtIa.get())
        Mn = float(txtMn.get())
        tmax = float(txtTmax.get())
    except ValueError:
        return  # Invalid input; do nothing

    # Calculate system constant
    C = 1e3 * J * (Ia / Mn) ** 2
    u2 = i = t = 0
    dt = 0.5
    sx = xmax / tmax  # Scaling factor for time axis

    # Prepare list for plotting the response curve
    u2_t = []
    canZ.create_line(0, w, xmax, w, fill='green', width=2)  # Draw horizontal axis

    # Numerical integration loop (Euler method)
    while t <= tmax:
        i += (U1 - R * i - u2) * dt / L
        u2 += i * dt / C
        t += dt
        u2_t.append(int(sx * t))
        u2_t.append(int(-u2) + ymax)
    # Draw the response curve
    canZ.create_line(u2_t, fill='blue', width=2)

# --- Main window setup ---
main = tk.Tk()
main.title("Second-Order Control System Simulation")
xmax, ymax = 800, 400

# Create canvas for plotting
canZ = tk.Canvas(main, width=xmax, height=ymax, bg='white')
canZ.pack()

# Create and place labels and entry fields for parameters
def add_labeled_entry(label_text, default, parent):
    lbl = tk.Label(parent, text=label_text)
    lbl.pack(side="left")
    entry = tk.Entry(parent, width=5)
    entry.insert(0, str(default))
    entry.pack(side="left")
    return entry

txtR = add_labeled_entry("R", 1.5, main)
txtL = add_labeled_entry("L", 24, main)
txtMn = add_labeled_entry("Mn", 170, main)
txtIa = add_labeled_entry("Ia", 40, main)
txtJ = add_labeled_entry("J", 0.22, main)
txtTmax = add_labeled_entry("tmax", 300, main)

# Create and place control buttons
cmdStart = tk.Button(main, text="Start", command=simulate_second_order_system)
cmdStart.pack(side="left")
cmdNeu = tk.Button(main, text="Clear", command=clear_canvas)
cmdNeu.pack(side="left")
cmdEnde = tk.Button(main, text="Exit", command=main.destroy)
cmdEnde.pack(side="left")

main.mainloop()