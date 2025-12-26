#05_steigung2.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
#Funktion
def f(x):
    return x**2/2
#Tangente
def f2(x,xs):
    m=derivative(f,xs,n=1)
    x0=xs-f(xs)/m
    return m*(x-x0)

x = np.linspace(0, 5, 100)
xs=2
fig, ax = plt.subplots()
ax.plot(x, f(x), color="g", lw=2)
ax.plot(x, f2(x,xs), color="b", lw=1)
ax.plot(xs, f(xs), "or")
ax.grid(True)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.show()