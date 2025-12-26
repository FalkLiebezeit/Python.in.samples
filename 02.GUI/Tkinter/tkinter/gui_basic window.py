# Basic Tkinter window example with a label

import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Basic Window Example")

# Create a label widget with custom font and text
lbl_result = tk.Label(window, text="Result Output", font=("Arial", 24))
lbl_result.pack(padx=20, pady=20)  # Add padding for better appearance

# Start the Tkinter event loop
window.mainloop()