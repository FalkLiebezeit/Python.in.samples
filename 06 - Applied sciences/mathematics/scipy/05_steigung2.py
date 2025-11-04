#05_steigung2.py
import numpy as np
import matplotlib.pyplot as plt
from numdifftools import Derivative
#Funktion
def f(x):
    return x**2/2
#Tangente
def f2(x,xs):
    m=Derivative(f,n=1)
    x0=xs-f(xs)/m(xs)
    return m(xs)*(x-x0)

x = np.linspace(0, 5, 100)
xs=2 #Stelle der Steigung
fig, ax = plt.subplots()
ax.plot(x, f(x),"g-", lw=2) #Funktion
ax.plot(x, f2(x,xs),"b-", lw=1) #Tangente
ax.plot(xs, f(xs), "or") #roter Punkt
ax.set(xlabel="x",ylabel="y")
ax.grid(True)
plt.show()
