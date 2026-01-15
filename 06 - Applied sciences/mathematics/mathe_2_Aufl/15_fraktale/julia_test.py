import numpy as np
from matplotlib import pyplot as plt
x1,x2=-2,2
y1,y2=-1,1
zeilen = spalten = nmax= 256
mittelpunkt = 0+0j
breite=3
scale = max(breite/spalten,breite/zeilen)
mandelbrot = np.zeros((zeilen, spalten)) #Matrix
c = -1.1193+0.2718j
for i in range(zeilen):      #Zeilen
    for j in range(spalten): #Spalten
        z = mittelpunkt + (i - spalten/2 + (j - zeilen//2)*1j)*scale
        #z = 0
        for k in range(nmax):
            z = z**2 + c
            if np.abs(z) > 2: break
        mandelbrot[j, i] = k
#Grafikbereich       
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(mandelbrot,cmap='Blues', extent=[x1, x2, y1, y2])
ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)")
fig.tight_layout()
ax.set_aspect('equal')
plt.show()

'''
#Vorlage
https://carpentries-incubator.github.io/lesson-parallel-python/06b-exercise-fractals/index.html
'''