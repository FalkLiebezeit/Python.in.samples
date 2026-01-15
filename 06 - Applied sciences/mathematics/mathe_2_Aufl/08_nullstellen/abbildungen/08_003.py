#08_003.py
#Fixpunktverfahren
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
#Funktionsdefinition fuer Newton-Verfahren
def f1(x):
    return np.exp(x/4)-5*x-2
#Nullstelle
xg=optimize.newton(f1,17)
#Fixpunktgleicung
def F(x):
    #y=np.cos(x)
    #y=1-np.sin(x)**2
    #y=np.exp(-0.8*x)
    #y=np.log(x)-x+2
    y=4*np.log(5*x+1)
    return y
#Grafikbereich
fig,ax =plt.subplots(figsize=(6,6))
x = np.linspace(0,20,200,endpoint=False)
ax.set_xlim(0,20)
ax.set_ylim(0,20)
ax.plot(x, x,'k--',lw=1,label=r'$y_{1}=x$') #Gerade Steigung m=1
ax.plot(x, F(x),'b',lw=1,label=r'$y_{2}=4\cdot ln\left( 5x+1\right)  $')
ax.plot(xg,F(xg),'ro') #Schnittpunkt
x=1    #Startwert
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
#ax.set_title(r'$y_{1}=x, y_{2}=cos\left( x\right)$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(loc='best')
#plt.grid(True)
plt.show()
