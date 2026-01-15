#05_plot_konvergenz.py
import numpy as np
import matplotlib.pyplot as plt
#Definition der Folgen
def folgen(n):
    x=0.5
    return 2**(1/n), (1/2)**(1/n), (1-x**n)**(1/n)
#Grafikbereich
fig, ax = plt.subplots()
n=np.arange(1,17,1)
an,bn,cn=folgen(n)
ax.plot(n,an,'r+',label=r'$\left(2\right)^{\frac{1}{n}}$')
ax.plot(n,bn,'bx',label=r'$\left(\frac{1}{2}\right)^{\frac{1}{n}}$')
ax.plot(n,cn,'go',label=r'$\left(1-x^{n}\right)^{\frac{1}{n} }$')
#ax.hlines(1,1,15)
ax.set(xlabel='n',ylabel='$a_{n},b_{n},c_{n}$')
ax.legend(loc='best')
ax.set_xlim(0,16)
plt.show()
