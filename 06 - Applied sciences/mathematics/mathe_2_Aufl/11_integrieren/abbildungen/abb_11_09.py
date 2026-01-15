#abb_11_09.py
#Rotationsfläche
import numpy as np
import matplotlib.pyplot as plt
#
def f(x):
    return np.sqrt(x)
#
fig,ax = plt.subplots()
x=np.linspace(0,5,500)
ax.plot(x,f(x),'b-',lw=2)
ax.set_ylim(-3,3)
ax.hlines(0,5,0,color='k',linestyles='dashdot')
#Delta x
xi=2.25
ax.vlines(2,0,f(xi),color='k')
ax.vlines(2.5,0,f(xi),color='k')
ax.hlines(f(xi),2,2.5,color='k')
#Fuellen
ax.fill_between(x,f(x),facecolor='g',alpha=0.2)
ax.text(2.15,-0.25,r"$\Delta x$")
ax.set_xlabel('x')
ax.set_ylabel('y',rotation=True)
plt.show()