#09_plot_grenzwert.py
import numpy as np
import matplotlib.pyplot as plt
N=17
eps=0.5 #Epsilon Umgebung
g=5     #Grenzwert
#Folge
def a(n):
    return 5*(1-1/(2**n))
#Grafikbereich
fig,ax=plt.subplots()
ax.set_title(r"$a_{n}=5\left(1-\frac{1}{2^{n}}\right)$")
ax.set(xlabel='n',ylabel='$a_{n}$')
n=np.linspace(1,N,N,endpoint=True)
ax.scatter(n,a(n),marker='+',color='r') #Zeichnen
ax.hlines(g+eps,0,N+1) #Schranke oben
ax.hlines(g-eps,0,N+1) #Schranke unten
ax.set_xlim(0,N+1)
ax.set_ylim(0,8)
plt.show()