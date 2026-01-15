#04_plot_newton.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
#Funktionsdefinition
def f(x):
    y=(x-1)*(x-2)*(x-3)
    return y
#Grafikbereich
fig, ax= plt.subplots(label='Nullstellen')
xn=newton(f,[1.1,2.1,3.1]) #Berechnung der Nullstellen
x=np.linspace(0.5,3.5,200)
ax.plot(x,f(x),'b-',lw=1.5)
ax.scatter(xn,[0,0,0],marker='x',color='red')
ax.hlines(0,3.5,0,color='black',lw=0.8)
ax.text(0.6,0.63,'Nullstellen\n%.2f\n%.2f\n%.2f'%(xn[0],xn[1],xn[2]))
ax.set_xlim(0.5,3.5)
ax.set_ylim(-1,1)
ax.set(xlabel='x',ylabel='y')
plt.show()

'''
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/08_006.pdf")
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/08_006.svg")
'''