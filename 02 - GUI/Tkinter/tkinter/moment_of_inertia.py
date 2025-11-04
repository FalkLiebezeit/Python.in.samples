# 02_gui_pack.py
# Optimized and commented: Moment of inertia calculator for a cylinder using Tkinter

import tkinter as tk

def calculate_moment_of_inertia():
    """
    Calculate the moment of inertia (Trägheitsmoment) of a cylinder
    based on user input for diameter and length.
    """
    pi = 3.14159
    rho = 7.85  # Density of steel in kg/dm^3
    try:
        d = float(txtDiameter.get())  # Diameter in dm
        l = float(txtLength.get())    # Length in dm
        # Moment of inertia formula for a cylinder: J = (rho * l * pi * d^4) / 32
        J = rho * l * pi * d**4 / 32
        J_kgm2 = 1e-2 * J  # Convert to kg*m^2
        lblResult["text"] = f"J = {J_kgm2:6.3f} kgm^2"
    except ValueError:
        lblResult["text"] = "Please enter valid numbers"

# Create main window
main = tk.Tk()
main.minsize(400, 200)
main.title("Moment of Inertia of a Cylinder")

# Create and pack widgets
lblDiameter = tk.Label(main, text="Enter diameter in dm")
lblLength = tk.Label(main, text="Enter length in dm")
lblResult = tk.Label(main, text="")

txtDiameter = tk.Entry(main, width=5, justify="right")
txtDiameter.insert(0, "0.8")
txtLength = tk.Entry(main, width=5, justify="right")
txtLength.insert(0, "10")

btnCalculate = tk.Button(main, text="Calculate", command=calculate_moment_of_inertia)
btnExit = tk.Button(main, text="Exit", command=main.destroy)

# Pack widgets vertically
lblDiameter.pack()
txtDiameter.pack()
lblLength.pack()
txtLength.pack()
btnCalculate.pack()
lblResult.pack()
btnExit.pack()

# Start the Tkinter event loop
main.mainloop()