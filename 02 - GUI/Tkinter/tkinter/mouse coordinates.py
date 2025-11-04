# Mouse Coordinates and Function Plot Example with Tkinter

import tkinter as tk
import math as m

# --- Window and Canvas Setup ---
main = tk.Tk()
main.title("Mouse Coordinates and Function Plot")

xmax, ymax = 500, 500  # Canvas size in pixels

# Logical coordinate system for the plot
x1, x2 = 0, 10         # x-axis range
y1, y2 = -10, 10       # y-axis range

# Calculate scaling factors for coordinate transformation
ym = ymax / 2
sx = (x2 - x1) / xmax  # x pixels to logical x
sy = ymax / (y2 - y1)  # logical y to pixels

# Create the Canvas widget
canZ = tk.Canvas(main, width=xmax, height=ymax, bg='white')
canZ.create_line(0, ym, xmax, ym, fill='black', width=2)  # Draw x-axis

def f(x):
    """Function to plot: y = 8 * sin(x)"""
    return 8 * m.sin(x)

def koordinate(e):
    """
    Display the logical coordinates (x, y) of the mouse pointer
    as it moves over the canvas.
    """
    x_pixel, y_pixel = e.x, e.y
    x_logical = sx * x_pixel
    y_logical = (0.5 * ymax - y_pixel) / sy
    lblKoordinate["text"] = f"  x: {x_logical:4.1f}  y: {y_logical:4.1f}"

def zeichne():
    """Draw the function curve on the canvas."""
    dx = 1  # Step size in pixels
    for x in range(0, xmax, dx):
        x1_pixel = x
        x2_pixel = x + dx
        y1_pixel = -sy * f(sx * x1_pixel) + ym
        y2_pixel = -sy * f(sx * x2_pixel) + ym
        canZ.create_line(x1_pixel, y1_pixel, x2_pixel, y2_pixel, fill='blue', width=2)

# --- UI Elements ---
lblKoordinate = tk.Label(main, text="")
cmdStart = tk.Button(main, text="Draw", command=zeichne)

# --- Layout ---
canZ.pack()
cmdStart.pack(side="left")
lblKoordinate.pack(side="left")

# --- Bind mouse movement to coordinate display ---
canZ.bind("<Motion>", koordinate)

# --- Start the Tkinter event loop ---
main.mainloop()