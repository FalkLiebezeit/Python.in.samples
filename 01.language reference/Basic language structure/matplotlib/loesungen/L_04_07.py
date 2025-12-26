#L_04_07.py
#Detail einer Funktion in einem neuen Axes zeichnen
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1e-6, 1, 1000)
y = np.cos(1.0/x)
fig=plt.figure(figsize=(6,4))
#left, bottom, width, height
ax1=fig.add_axes([0.1,0.1,0.8,0.8])
ax1.set_ylim([-1.2,1.2])
#inneres Koordinatensystem
ax2=fig.add_axes([0.58,0.18,0.28,0.25])
ax2.set_xlim([0,0.2])
#plotten
ax1.plot(x,y,"r-")
ax2.plot(x,y,"b-")
plt.show()