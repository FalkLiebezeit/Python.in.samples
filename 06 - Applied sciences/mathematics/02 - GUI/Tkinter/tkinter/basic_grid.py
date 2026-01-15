import tkinter as tk

def calculate_moment_of_inertia():
    """
    Calculate the moment of inertia (Trägheitsmoment) of a cylinder
    based on user input for diameter and length.
    """
    pi = 3.14159
    rho = 7.85  # Density in kg/dm^3
    try:
        d = float(txt_diameter.get())
        l = float(txt_length.get())
        # Moment of inertia formula for a cylinder: J = (rho * l * pi * d^4) / 32
        J = rho * l * pi * d**4 / 32
        J_kgm2 = 1e-2 * J  # Convert to kg*m^2
        lbl_result["text"] = f"{J_kgm2:6.3f} kgm^2"
    except ValueError:
        lbl_result["text"] = "Please enter valid numbers"

# Create main window
main = tk.Tk()
main.title("Moment of Inertia of a Cylinder")
main.minsize(400, 115)

# Create and place widgets using grid layout
lbl_diameter = tk.Label(main, text="Enter diameter in dm")
lbl_length = tk.Label(main, text="Enter length in dm")
lbl_moment = tk.Label(main, text="Moment of inertia")
lbl_result = tk.Label(main, text="")

txt_diameter = tk.Entry(main, justify="right")
txt_diameter.insert(0, "0.8")
txt_length = tk.Entry(main, justify="right")
txt_length.insert(0, "10")

btn_calculate = tk.Button(main, text="Calculate", command=calculate_moment_of_inertia)
btn_exit = tk.Button(main, text="Exit", command=main.destroy)

lbl_diameter.grid(row=0, column=0, sticky="w")
txt_diameter.grid(row=0, column=1, sticky="e")
lbl_length.grid(row=1, column=0, sticky="w")
txt_length.grid(row=1, column=1, sticky="e")
lbl_moment.grid(row=2, column=0, sticky="w")
lbl_result.grid(row=2, column=1, sticky="e")
btn_calculate.grid(row=3, column=0)
btn_exit.grid(row=3, column=1)

main.mainloop()