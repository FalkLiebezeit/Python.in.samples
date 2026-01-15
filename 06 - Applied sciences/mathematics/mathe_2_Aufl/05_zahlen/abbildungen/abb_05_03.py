#abb_05_03.py
#Verteilung der Primzahlen
import numpy as np
import matplotlib.pyplot as plt

def f(n):
    return n/np.log(n)

fig,ax= plt.subplots(figsize=(8,6))
n=np.linspace(100,1e9,100)
ax.plot(n,f(n),lw=2,color='red')
ax.set_title(r'$\pi \left( n\right)  =\frac{n}{\log \left( n\right)} $')
ax.set_xlabel('n')
ax.set_ylabel('Anzahl der Primzahlen',rotation=90)
plt.show()