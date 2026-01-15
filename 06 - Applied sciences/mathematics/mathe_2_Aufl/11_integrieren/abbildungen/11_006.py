#11_006.py
#Trapezsummen
import numpy as np
import matplotlib.pyplot as plt
n=10
x=np.linspace(0,11,200)

def f(x):
    return x**2

fig,ax = plt.subplots()
ax.set_title('Trapezsummen')

for i in range(n+1):
    ax.vlines(i,0,f(i),color='b')

p =[f(i) for i in range(n+1)]
ax.plot(p,color='b',lw=2)
ax.plot(x,f(x),color='r',lw=2,ls='dashed')
ax.set_xlim(0,10.5)
ax.set_ylim(0,105)
ax.text(1,80,r'$y=x^{2}$')
ax.text(5.3,7,r'$\Delta x$')
ax.set_xlabel('x')
ax.set_ylabel('y',rotation=True)

plt.show()

'''
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/11_006.pdf")
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/11_006.svg")
'''
