#01_nullstellen.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

def f(x):
    #y=(x-1)*(x-2)*(x-5)*(x-10)
    y=10*np.exp(-0.5*x)*np.sin(x)
    return y

x = np.linspace(0,15,100)
x0=[0,2,6,9,12] #Startwerte
#hybr,lm,broyden1,broyden2,anderson
#linearmixing,diagbroyden,excitingmixing,krylov,df-sane
xn=root(f,x0,method='hybr')
print(xn.x)
fig, ax = plt.subplots()
ax.plot(x,f(x),"r-",lw=2)
ax.scatter(xn.x,[0,0,0,0,0],color="k",marker="x")
ax.set(xlabel="x",ylabel="y")
ax.grid(True)
plt.show()