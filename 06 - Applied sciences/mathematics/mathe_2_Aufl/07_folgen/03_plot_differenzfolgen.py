#03_plot_differenzfolgen.py
import numpy as np
import matplotlib.pyplot as plt
#Folge
def b(n):
    return n**2
#1. Differenzfolge
def delta_b1(n):
    return b(n+1)-b(n)
#2. Differentfolge
def delta_b2(n):
    return delta_b1(n+1)-delta_b1(n)
#Grafikbereich
fig,ax=plt.subplots()
n=np.arange(1,11,1)
#delta_b1,delta_b2=folgen(n)
ax.scatter(n,b(n), marker='+',color='r')
ax.scatter(n,delta_b1(n),marker='x',color='b')
ax.scatter(n,delta_b2(n),marker='o',color='g')
ax.set_title("Differenzfolgen")
ax.set_xlabel('n')
ax.set_ylabel(r'$b_{n},\  \Delta b_{n},\  \Delta^{2} b_{n}$')
ax.set_xlim(0.5,10.5)
ax.set_ylim(-10,102)
plt.show()



