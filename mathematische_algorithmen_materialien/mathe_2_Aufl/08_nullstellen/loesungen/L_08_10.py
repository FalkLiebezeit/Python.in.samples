#L_08_10.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
xmax=5
ymax=1.5
#Funktionsdefinition fuer Polynom
def f(x):
    y=x**4 - 10*x**3 + 35*x**2 - 50*x + 24
    return y
#Grafikbereich
fig, ax= plt.subplots(label='Nullstellen')
xn=newton(f,[1.1,2.1,3.1,5]) #Berechnung der Nullstellen
x=np.linspace(0,xmax,200)
ax.plot(x,f(x),'b-',lw=1.5)
ax.scatter(xn,[0,0,0,0],marker='x',color='red')
ax.hlines(0,xmax,0,color='black',lw=0.8)
ax.text(0.1,-1.3,'Nullstellen\n%.2f\n%.2f\n%.2f\n%.2f'%(xn[0],xn[1],xn[2],xn[3]))
ax.set_xlim(0,xmax)
ax.set_ylim(-ymax,ymax)
ax.set(xlabel='x',ylabel='y')
plt.show()

'''
from sympy import *
x=symbols('x')
y=(x-1)*(x-2)*(x-3)*(x-4)
print(expand(y))
'''