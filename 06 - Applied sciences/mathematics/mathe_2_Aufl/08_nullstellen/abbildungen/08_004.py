#08_004.py
#Newton-Verfahren
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
#Funktion
def f(x):
    return np.exp(x/4)-5*x-1 #np.exp(x)-3
#Tangente
def tangente(x,x0):
    m=np.exp(x0/4)/4-5 #1. Ableitung
    return m*(x-x0)+f(x0)
#
fig, ax = plt.subplots(label='Newton-Verfahren')
x = np.linspace(0,20,200)
ax.set_xlim(0,20)
ax.set_ylim(-50,50)
#genaue Nullstelle
x0=optimize.newton(f,17)
#zeichnen
ax.plot(x,f(x),'b-')         #Funktionsgraph
ax.plot(x0,f(x0),'ro')       #Punkt
ax.plot(15,f(15),'ro')       #Punkt, , Nullstelle
ax.plot(x,tangente(x,x0),'g--',lw=1)   #Tangente, Nullstelle
ax.plot(x,tangente(x,15),'g--',lw=1)   #Tangente
ax.vlines(15,f(15),0,'black',lw=1)
ax.text(14.8,2.5,r'$x_1$')
ax.hlines(0,0,50,color='black')
#Beschriftung
term=r"$y=e^{\frac{x}{4} }-5x-1$"
ax.set_title(term,fontsize=14)
ax.set(xlabel="x",ylabel="y")
plt.show()




