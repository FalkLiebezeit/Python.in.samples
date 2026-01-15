#09_plot_extremwerte.py
import numpy as np
import matplotlib.pyplot as plt
x1,x2=-5,5
y1,y2=-10,4
#Funktionsdefinition
def f(x):
    return -x**3/4 + 3*x - 4
#zentraler Differenzenquotient
def ableitung(f,x,h=1e-3):
    return (f(x+h)-f(x-h))/(2*h)
#1. Ableitung
def diff1(x):
    return ableitung(f,x)
#2. Ableitung
def diff2(x):
    return ableitung(diff1,x)
#Grafikbereich
fig, ax = plt.subplots()
x = np.linspace(x1, x2,500)
ax.plot(x,f(x),lw=2,color='r')
ax.plot(x,diff1(x),'b--',label='1. Ableitung')
ax.plot(x,diff2(x),'g-.',label='2. Ableitung')
ax.set_xlim(x1,x2)
ax.set_ylim(y1,y2)
ax.legend(loc='best')
ax.set(xlabel='x',ylabel='y')
ax.grid(True)

plt.show()

'''
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_005.pdf")
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_005.svg")
'''