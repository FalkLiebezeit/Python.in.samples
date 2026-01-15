#08_002.py
#Bisektionsverfahren
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
x1=15
x2=20
a1,b1=17,19
a2,b2=17.5,18.5
b=19
#
def f(x):
    return np.exp(x/4)-5*x-1
#
xn=optimize.newton(f,17)#Nullstelle
#
fig,ax =plt.subplots(label='Bisektion')
x = np.linspace(x1,x2,100)
ax.plot(x,f(x),'b',lw=2)
ax.plot(xn,f(xn),'ro') #Punkt
#Schnittpunkt mit x-Achse
ax.hlines(0,x1,x2,'black',lw=1)
#vertikale Linien
ax.vlines(a1,f(a1),0,'black',lw=1)
ax.vlines(b1,f(b1),0,'black',lw=1)
ax.vlines(a2,f(a2),0,'black',lw=1)
ax.vlines(b2,f(b2),0,'black',lw=1)
ax.text(16.92,1.5,'$a$',fontsize=12)
ax.text(18.94,-4.8,'$b$',fontsize=12)
ax.set_title(r'$y=\  e^{\frac{x}{4} }\  -5x-1$')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()



