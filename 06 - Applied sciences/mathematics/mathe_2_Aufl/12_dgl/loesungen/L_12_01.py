#L_12_01.py
#Richtungsfeld
import numpy as np
import matplotlib.pylab as plt
#
Nx,Ny = 20,20  
x1,x2 = -2,2         
y1,y2 = -2,2      
#
def f(x,y):
    dy_dx=0.3*x**2
    return dy_dx
#Gitter
x12 = np.linspace(x1,x2,Nx)
y12 = np.linspace(y1,y2,Ny)
x,y = np.meshgrid(x12,y12)
#Polynom
xx = np.linspace(x1,x2,200)
f_x=0.1*xx**3
#Grafikbereich
fig, ax=plt.subplots(figsize=(8,6), label='Richtungsfeld')
#Richtungsfeld
ax.quiver(x,y,np.ones_like(x),f(x,y),width=0.002,headwidth=0,color='r')
#Polynom zeichnen
ax.plot(xx,f_x,'b--',lw=2)
ax.set_xlabel("x")
ax.set_ylabel("y",rotation=0)
plt.show()


