import tkinter as tk

# Create the main application window
main = tk.Tk()
main.title("Canvas Line Example")

# Set canvas dimensions
xmax, ymax = 500, 500

# Create a Canvas widget with a white background
canvas = tk.Canvas(main, width=xmax, height=ymax, bg='white')

# Draw a horizontal black line in the center of the canvas
canvas.create_line(0, ymax / 2, xmax, ymax / 2, fill='black', width=3)

# Draw a blue diagonal line from the top-left to the bottom-right corner
canvas.create_line(0, 0, xmax, ymax, fill='blue', width=3)

# Pack the canvas into the main window
canvas.pack()

# Start the Tkinter event loop
main.mainloop()