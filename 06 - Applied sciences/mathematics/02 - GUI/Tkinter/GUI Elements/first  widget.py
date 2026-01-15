import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Widget")
root.geometry("300x200")

# Create a label widget
label = tk.Label(root, text="Hello, world!")
label.pack(pady=10)

# Create a button widget
button = tk.Button(root, text="Click Me!", command=lambda: label.config(text="You clicked the button!"))
button.pack(pady=10)

# Run the main event loop
root.mainloop()