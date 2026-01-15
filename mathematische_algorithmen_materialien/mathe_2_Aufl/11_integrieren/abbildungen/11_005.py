#11_005.py
#Rechtecksummen
import numpy as np
import matplotlib.pyplot as plt
#
x=np.linspace(0,11,100)

def f(x):
    return x**2
#b: obere Grenze, h: Schrittweite
def rechtecke(b,h):
    for i in range(0,b):   
        #vertikal: x-, ymin, ymax
        ax.vlines(i+h,0,f(i+3*h/2),color='b')
        #horinzontal: y-, xmin, xmax
        ax.hlines(f(i+h/2),i,i+h,color='b')
#  
fig,ax = plt.subplots()
rechtecke(10,1)
ax.plot(x,f(x),color='r',lw=2)
ax.set_xlim(0,11)
ax.set_ylim(0,100)
ax.text(1,90,r'$y=x^{2}$')
ax.text(5.3,7,r'$\Delta x$')
ax.text(0.35,-4.8,r'$\frac{h}{2}$')
ax.text(0.85,-4.8,r'$h$')
ax.set_title('Rechtecksummen')
ax.set_xlabel('x')
ax.set_ylabel('y',rotation=True)

plt.show()
