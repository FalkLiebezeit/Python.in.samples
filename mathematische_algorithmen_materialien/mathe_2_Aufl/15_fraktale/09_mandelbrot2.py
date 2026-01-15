#09_mandelbrot2.py
import numpy as np
import matplotlib.pyplot as plt
import warnings
N=50
x1,x2=-2,1
y1,y2=-1.5,1.5
x,y = np.ogrid[x1:x2:800j,y1:y2:800j]
c = x + 1j*y
z = c
warnings.filterwarnings('ignore')
for i in range(N):
    z = z**2 + c
mandelbrot = (np.abs(z) < 2).transpose()
#Grafikbereich
fig, ax = plt.subplots()
ax.imshow(mandelbrot,cmap='Blues',extent=[x1, x2, y1, y2])
ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)",rotation=90)
fig.tight_layout()
ax.set_aspect('equal')
plt.show()
