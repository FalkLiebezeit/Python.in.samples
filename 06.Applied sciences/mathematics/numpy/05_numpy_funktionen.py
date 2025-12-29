#05_numpy_funktionen.py
import numpy as np
#import math
x=np.arange(-3,4,1)
#y1=math.sin(x)
y1=np.sin(x)
y2=np.exp(x)
y3=np.sinh(x)
y4=np.cosh(x)
y5=np.hypot(3,4)#Diagonale
y1,y2,y3,y4=np.round((y1,y2,y3,y4),decimals=3)
#Ausgabe
print("x-Werte:\n",x)
print("sin-Funktion:\n",y1)
print("e-Funktion:\n",y2)
print("sinh-Funktion:\n",y3)
print("cosh-Funktion:\n",y4)
print("Hypotenuse:",y5)


