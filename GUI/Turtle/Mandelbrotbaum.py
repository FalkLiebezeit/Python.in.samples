import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, MAX_ITERATIONS):
    z = 0
    for n in range(MAX_ITERATIONS):
        if abs(z) > 2:
            return n
        z = z*z + c
    return MAX_ITERATIONS

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, MAX_ITERATIONS):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], MAX_ITERATIONS)
    return (r1, r2, n3)

xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
MAX_ITERATIONS = 256

r1, r2, n3 = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, MAX_ITERATIONS)

plt.imshow(n3.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.show()
