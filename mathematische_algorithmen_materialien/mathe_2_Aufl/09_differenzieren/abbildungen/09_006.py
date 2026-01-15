#09_006.py
#Extremwerte zeichnen
import numpy as np
import matplotlib.pyplot as plt
x1,x2=0,4
#Funktionsdefinition
def fmax(x):
    return -(x-2)**2+5
#Funktionsdefinition
def fmin(x):
    return (x-2)**2
#zentraler Differenzenquotient
def derivative(f,x,h=1e-3):
    return (f(x+h)-f(x-h))/(2*h)
#1. Ableitung
def fmax_1(x):
    return derivative(fmax,x)
#2. Ableitung
def fmax_2(x):
    return derivative(fmax_1,x)
#1. Ableitung
def fmin_1(x):
    return derivative(fmin,x)
#2. Ableitung
def fmin_2(x):
    return derivative(fmin_1,x)
x = np.linspace(x1,x2,500)
#3 Zeilen 2 Spalten
fig,ax = plt.subplots(3,2,figsize=(6,6))
#1. Zeile, 1. Spalte
ax[0,0].set_title("lokales Maximum")
ax[0,0].plot(x,fmax(x),lw=2,color='r')
ax[0,0].grid(True)
ax[0,0].set_ylabel("y",rotation=True)
#2. Zeile, 1. Spalte
ax[1,0].set_title("1. Ableitung")
ax[1,0].plot(x,fmax_1(x),lw=2,color='b')
ax[1,0].plot(2,0,'ro') #Nullstelle
ax[1,0].grid(True)
ax[1,0].set_ylabel("y",rotation=True)
#3. Zeile, 1.Spalte 
ax[2,0].set_title("2. Ableitung")
ax[2,0].plot(x,fmax_2(x),lw=2,color='g')
ax[2,0].set_ylim(-3,1)
ax[2,0].grid(True)
ax[2,0].set_xlabel("x")
ax[2,0].set_ylabel("y",rotation=True)
#1. Zeile, 2. Spalte
ax[0,1].set_title("lokales Minimum")
ax[0,1].plot(x,fmin(x),lw=2,color='r')
ax[0,1].grid(True)
#2. Zeile, 2. Spalte
ax[1,1].set_title("1. Ableitung")
ax[1,1].plot(x,fmin_1(x),lw=2,color='b')
ax[1,1].plot(2,0,'ro') #Nullstelle
ax[1,1].grid(True)
#3. Zeile, 2. Spalte
ax[2,1].set_title("2. Ableitung")
ax[2,1].plot(x,fmin_2(x),lw=2,color='g')
ax[2,1].set_ylim(-1,3)
ax[2,1].grid(True)
ax[2,1].set_xlabel("x")
fig.tight_layout()
plt.show()


