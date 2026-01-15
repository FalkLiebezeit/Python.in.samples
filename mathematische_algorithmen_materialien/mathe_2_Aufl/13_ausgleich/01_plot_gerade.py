#01_plot_gerade.py
import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt
xi=np.array([1,2,3,4,5])
yi=np.array([6,6.8,10,10.5,10.2])
n=len(xi)
#Koeffizientenmatrix
A=np.array([[np.sum(xi**2) ,np.sum(xi)],
            [np.sum(xi),n]])
#Inhomogenitätsvektor
y=np.array([np.sum(xi*yi),np.sum(yi)])
#Lösungsvektor
L=solve(A,y)
a,b=L[0],L[1]
E=0 #Fehlerfunktional
for i in range(n):
    E=E + (yi[i] - (a*xi[i] + b))**2
#Ausgaben
print("Fehlerfunktional\n E =",E)
print("Koeffizientenmatrix\n",A)
print("Inhomogenitätsvektor\n",y)
print("Lösungsvektor\n",L)
print("Steigung        a=",a)
print("Achsenabschnitt b=",b)
#Funktionsplot
xa=np.linspace(0,np.max(xi),500)
ya=a*xa+b
fig, ax = plt.subplots()
ax.set(xlabel="x",ylabel="y",title=r"$y=ax+b$")
ax.plot(xi,yi,'r+')
ax.plot(xa,ya,'b')
ax.set_ylim(0,15)
plt.show()
