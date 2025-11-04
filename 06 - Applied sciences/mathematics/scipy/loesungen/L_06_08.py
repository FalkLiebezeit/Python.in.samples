#L_06_08.py
#DGL 1. Ordnung
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
xmax=1
xi=[-xmax,xmax] 
y0 =[1]    
def dgl(x,ya):
    y=ya
    #dy_dx=-x/y
    #dy_dx=1+x-y
    #dy_dx=y*np.tan(x)-2*np.sin(x)
    #dy_dx=2*x-y*x**2
    dy_dx=np.exp(-x*y)
    return dy_dx

x = np.linspace(-xmax,xmax,500)
z = solve_ivp(dgl,xi,y0,dense_output=True)
y = z.sol(x).flatten()
fig,ax=plt.subplots()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.plot(x,y,"r-",lw=2)
plt.show()




