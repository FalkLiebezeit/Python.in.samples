#06_plot_planetenbahn.py
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
#Koordinatendaten
x=np.array([0.2,-0.7,-0.3,1.2,2.0,-2.4])
y=np.array([1.8,1.6,-1.8,-1.6,1.1,0.5])
n=np.size(x)
#Koeffizientenmatrix
A=np.array([x**2,y**2]).T
#Inhomogenitätsvektor
e=np.ones(n)
#Lösung des Gleichungssystems
L=inv(A.T@A)@A.T@e
#Halbachsen berechnen
a,b=1./np.sqrt(L[0]),1./np.sqrt(L[1])
#Ausgabe
print("Koeffizientenmatrix des überbestimmten Gleichungssystems\n",A)
print("Koeffizientenmatrix der Normalgleichung\n",A.T@A)
print("Inhomogenitätsvektor der Normalgleichung\n",A.T@e)
print("Lösungsvektor\n",L)
print("Halbachsen der Ellipse")
print("a =",a)
print("b =",b)
t=np.linspace(0,2*np.pi,500)
xa=a*np.sin(t)
ya=b*np.cos(t)
fig, ax = plt.subplots()
ax.set_title(r"$\frac{x^{2}}{a^{2}} +\frac{y^{2}}{b^{2}} =1$")
ax.set(xlabel="x",ylabel="y")
ax.plot(x,y,'ro',lw=2)
ax.plot(xa,ya,'b--')
plt.show()