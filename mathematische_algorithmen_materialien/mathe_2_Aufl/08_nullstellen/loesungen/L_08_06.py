#L_08_06.py
#Veranschaulichung des Fixpunktverfahrens
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
xmax=2
ymax=1.5
#Fuer Schnittpunktmarkierung
def f1(x):
    return x-np.cos(x)
#Nullstelle
xg=optimize.newton(f1,0.2)
#Fixpunktgleichung
def F(x):
    y=np.cos(x)
    #y=1-np.sin(x)**2
    #y=np.exp(-0.8*x)
    #y=np.log(x)-x+2
    #y=4*np.log(5*x+1)
    return y
#Grafikbereich
fig,ax =plt.subplots(figsize=(6,6),label='Fixpunktverfahren')
x = np.linspace(0,xmax,200,endpoint=False)
ax.set_xlim(0,xmax)
ax.set_ylim(0,ymax)
ax.plot(x, x,'k--',lw=1)   #Gerade Steigung m=1
ax.plot(x, F(x),'b',lw=1)  #Fixpunktgleichung
ax.plot(xg,F(xg),'ro')     #Schnittpunkt
x=0.2  #Startwert
xa=0.  #Abbruch
ax.vlines(x,0,F(0.6),color='black',lw=1)
while np.fabs(x-xa)>0.05:
    #waagerecht
    #y, xmin, xmax 
    ax.hlines(F(x),F(x),x,color='black',lw=1)
    #senkrecht
    #x, ymin, ymax senkrecht
    ax.vlines(x,F(x),x,color='black',lw=1)
    xa=x 
    x=F(x)
#
ax.set_title(r'$y_{1}=x, y_{2}=cos\left( x\right)$')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

