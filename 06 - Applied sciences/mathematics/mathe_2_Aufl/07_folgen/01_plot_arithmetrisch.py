#01_plot_arithmetrisch.py
import numpy as np
import matplotlib.pyplot as plt
#Folgen
def folgen(n):
    return 4*n,n**2
#Grafikbereich
fig,ax=plt.subplots()
n=np.arange(1,11,1)
an,bn=folgen(n)
ax.scatter(n,an,marker='+',color='r')
ax.scatter(n,bn,marker='x',color='b')
ax.set(xlabel='x',ylabel=r'$a_{n},b_{n}$')
ax.text(9,30,r"$a_{n}=4n$")
ax.text(7.5,80,r"$b_{n}=n^{2}$")
ax.set_xlim(0.5,10.5)
ax.set_ylim(0,102)
plt.show()


