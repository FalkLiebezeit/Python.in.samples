#08_001.py
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
#lineares Wachstum
def f1(x):
    return 5*x+1
#exponetielles Wachstum
def f2(x):
    return np.exp(x/4)
#y1=y2
def f3(x):
    return f2(x)-f1(x)
#
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(8,4))
x=np.linspace(0,20,500)
xn=optimize.newton(f3,17) #Nullstelle
#links
ax1.plot(x,f1(x),'b-')
ax1.plot(x,f2(x),'r-')
#Schnittpunkt
ax1.plot(xn,f1(xn),'ro')
#
ax1.set_title(r'$y_{1}=5x+1,\  y_{2}=e^{\frac{x}{4} }$')
ax1.set(xlabel='x',ylabel='y')
#rechts
ax2.plot(x,f3(x))
#Nullstellle
ax2.plot(xn,0,'ro')
#
ax2.set_title(r'$y=\  e^{\frac{x}{4} }\  -5x-1$')
ax2.set(xlabel='x')
#
ax1.grid()
ax2.grid()
plt.show()
