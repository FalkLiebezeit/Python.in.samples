#11_plot_numdifftools_kurvendiskussion.py
import numpy as np
import matplotlib.pyplot as plt
from numdifftools import Derivative
from scipy.optimize import newton
x1,x2=0,5.5
y1,y2=-8,5
#Funktionsdefinition
def f(x):
    y=x**5-15*x**4+85*x**3-225*x**2+274*x-120
    return y
#1. Ableitung
def df_1(x):
    df = Derivative(f,n=1)
    return df(x)
#2. Ableitung    
def df_2(x):
    df = Derivative(f,n=2)
    return df(x)
#Berechnungen
x = np.linspace(x1, x2, 500)
xi=newton(f,[0.5,1.7,3.1,4.5,6])
m=newton(df_1,[1.3,2.5,3.6,4.6])
w=newton(df_2,[2.5,2,4])
print("Nullstellen\n",xi)
for i in range(len(m)):
    if df_2(m[i])<0:
        print("Maxima x =",m[i],"y =",f(m[i]))
    elif df_2(m[i])>0:
        print("Minima x =",m[i],"y =",f(m[i]))   
print("Wendepunkte\n",w)
#Grafikbereich
fig,ax=plt.subplots()
ax.set_xlim(x1,x2)
ax.set_ylim(y1,y2)
ax.plot(x,f(x),lw=2,color='r',label='Funktion')
ax.plot(x,df_1(x),'b--',label='1. Ableitung')
ax.plot(x,df_2(x),'g-.',label='2. Ableitung')
ax.legend(loc='best')
ax.set(xlabel='x',ylabel='y')
ax.grid(True)
plt.show()

'''
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_008.pdf")
fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/09_008.svg")
'''
