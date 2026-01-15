#abb_06_03.py
#Schnittpunkte: zwei Parabeln
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x1=np.linspace(-6,6,900)
x21=5.- x1**2
x22=np.sqrt(x1+5)
ax.plot(x1,x21,'r--',lw=2,label=r'$x_{1}^{2} + x_{2}=5$')
ax.plot(x1,x22,'b-',lw=2,label= r'$-x_{1} + x^{2}_{2}=5$')
ax.plot(x1,-x22,'b-',lw=2)
#plt.plot(x1,np.zeros(len(x1)),color='black')
ax.set_xlim(-6,6)
ax.set_ylim(-6,6)
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
ax.legend(loc='best')
ax.grid(True)
plt.show()
