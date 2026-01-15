#05_plot_bremsweg.py
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
v=np.array([10,20,30,40,50])
s=np.array([1.2,3.8,9.2,17,24.9])
n=len(v) #np.size(v)
A=np.array([v**2,v]).T
L=inv(A.T@A)@A.T@s
print("Lösungsvektor L\n",L)
a,b =L[0],L[1]
#Ausgleichsfunktion für Bremsweg
def sa(a,b,v):
    return a*v**2 +b*v
#Prognose
v1,v2,v3=80,100,150
print("s = %3.4fv^2 + %3.4fv"%(a,b))
print("Bremswege für:")
print("v = %3.2f km/h s = %3.2f m"%(v1,sa(a,b,v1)))
print("v = %3.2f km/h s = %3.2f m"%(v2,sa(a,b,v2)))
print("v = %3.2f km/h s = %3.2f m"%(v3,sa(a,b,v3)))
#Funktionsplot
fig, ax = plt.subplots()
va=np.linspace(0,np.max(v),500)
ax.set_title(r"$s\left( v\right) = av^{2}$ + bv")
ax.set(xlabel="Geschwindigkeit v",ylabel="Bremsweg s")
ax.plot(v,s,'r+')
ax.plot(va,sa(a,b,va),'b')
plt.show()