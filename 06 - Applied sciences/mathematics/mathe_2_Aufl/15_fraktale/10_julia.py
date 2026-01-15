#10_julia.py
import numpy as np
import matplotlib.pyplot as plt
import warnings
N=500
cc='Blues'#hot,Blues,plasma,gray,twilight,magma
c = -0.1+0.65j
#c = -1.2  #-1.4 bis +0.2
#c=-0.74543+0.1130j
#c= 0.909 - 0.27j
#c=0 + 0.8j
#c=0.37+0.1j
#c=0.355+0.355j
#c=-0.54+0.54j
#c=-0.4-0.59j
#c=-0.1+0.9j
x1,x2=-2,2
y1,y2=-1.5,1.5
x,y = np.ogrid[x1:x2:800j,y1:y2:800j]
z=x + 1j*y
warnings.filterwarnings('ignore')
for _ in range(N):
    z = z**2 + c
julia = (np.abs(z) < 2).T
#Grafikbereich
fig, ax=plt.subplots()
ax.imshow(julia,cmap=cc,extent=[x1, x2, y1, y2])
ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)",rotation=90)
fig.tight_layout()
plt.show()