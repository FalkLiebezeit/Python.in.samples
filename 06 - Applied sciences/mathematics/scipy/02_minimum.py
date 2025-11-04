#02_minimum.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
V=1 #Volumen

def f(r):
    h=V/(np.pi*r**2)
    O=2*np.pi*r**2+2*np.pi*r*h
    return O

x = np.linspace(0.1, 2, 100)
opt=minimize(f,0.5)
#Ausgabe
print("r=%4.6f LE O=%4.6f FE" %(opt.x,opt.fun))
fig, ax = plt.subplots()
ax.plot(x,f(x),"b-",lw=2)
ax.plot(opt.x,opt.fun,"rx",lw=2)
ax.set(xlabel="r",ylabel="O")
ax.grid(True)
plt.show()