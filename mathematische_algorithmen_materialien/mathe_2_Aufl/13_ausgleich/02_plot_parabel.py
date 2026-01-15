#02_plot_parabel.py
import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt
xi=np.array([1,2,3,4,5])
yi=np.array([5.1,2.1,1,1.8,5.2])
n=len(xi)
#Koeffizientenmatix
A=np.array([[np.sum(xi**4),np.sum(xi**3),np.sum(xi**2),],
            [np.sum(xi**3),np.sum(xi**2),np.sum(xi)],
            [np.sum(xi**2),np.sum(xi),n]])
#Inhomogenitätsvektor
y=np.array([np.sum(xi**2*yi),np.sum(xi*yi),np.sum(yi)])
#Lösungsvektor
L=solve(A,y)
a,b,c=L[0],L[1],L[2]
#Ausgabe der numerischen Werte
print(" a\t b\tc\n",L)
print("%2.3fx^2 %2.3fx %2.3f" %(a,b,c))
#Funktionsplot
xa=np.linspace(0,np.max(xi+1),500)
ya=a*xa**2 + b*xa + c
fig, ax = plt.subplots()
ax.set(xlabel="x",ylabel="y",title=r"$y=ax^2 + bx +c$")
ax.plot(xi,yi,'r+')
ax.plot(xa,ya,'b')
ax.set_xlim(0,6)
ax.set_ylim(0,12)
plt.show()