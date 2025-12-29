#09_flaeche_parabel.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integral
from scipy.optimize import root

def f(x):
    return -(x-4)**2+10

x = np.linspace(0,8,100)
x0=[0,5]
xn=root(f,x0,method='hybr')
a,b=xn.x[0],xn.x[1]
A=integral.quad(f,a,b)[0]
#Ausgabe
print("Nullstellen:",a,b)
print("Flaeche:",A,"FE")
#Darstellung
fig, ax = plt.subplots()
ax.plot(x, f(x), "b-", lw=2)
ax.grid(True)
ax.set(xlabel="x",ylabel="f(x)")
ax.fill_between(x,f(x),where=f(x)>=0,color='g',alpha=0.2)
plt.show()