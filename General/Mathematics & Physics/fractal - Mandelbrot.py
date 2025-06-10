"""
Copilot:
Write a Python program that draws a Mandelbrot fractal.

answer:
This program defines the Mandelbrot function, computes the fractal values, 
and then visualizes them using Matplotlib. 
You can adjust parameters like width, height, 
and max_iter to refine the fractal's resolution and complexity. 

Fractals are mesmerizing mathematical patterns that appear in nature and art. 
Here are some fascinating examples:

- Julia Set: Similar to the Mandelbrot set, Julia sets create intricate, self-repeating designs based on complex numbers.
- Sierpiński Triangle: A simple yet stunning fractal formed by recursively removing smaller triangles from a larger one.
- Koch Snowflake: A fractal that starts with a triangle and evolves by adding smaller triangles to its edges, creating a snowflake-like shape.
- Romanesco Broccoli: A natural fractal where each bud is a miniature version of the whole vegetable.
- Lightning and River Networks: These natural formations follow fractal branching patterns, optimizing energy flow.



"""

import numpy as np
import matplotlib.pyplot as plt

# Define the Mandelbrot function
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Generate the fractal image
def generate_fractal(width, height, x_min, x_max, y_min, y_max, max_iter):
    x_vals = np.linspace(x_min, x_max, width)
    y_vals = np.linspace(y_min, y_max, height)
    fractal = np.zeros((height, width))

    for i, y in enumerate(y_vals):
        for j, x in enumerate(x_vals):
            c = complex(x, y)
            fractal[i, j] = mandelbrot(c, max_iter)

    return fractal

# Parameters for the fractal image
width, height = 1000, 1000
x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5
max_iter = 100

# Generate and plot the Mandelbrot fractal
fractal_image = generate_fractal(width, height, x_min, x_max, y_min, y_max, max_iter)
plt.imshow(fractal_image, extent=[x_min, x_max, y_min, y_max], cmap='inferno')
plt.colorbar()
plt.title("Mandelbrot Fractal")
plt.show()