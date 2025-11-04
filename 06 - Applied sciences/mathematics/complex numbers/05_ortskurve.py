#05_ortskurve.py
import numpy as np
import matplotlib.pyplot as plt
R=20
C=1e-6
L1=5e-2
L2=1e-2
wp=10e3 #Kreisfrequenz im Punkt p
#komplexer Widerstand
def Z(w):
    return 1j*w*L1+(R+1j*w*L2)*(1/(1j*w*C))/(R+1j*w*L2+1/(1j*w*C))

w=2.0*np.pi*np.linspace(0.01,3e3,500)
Zp=Z(wp)
fig,ax=plt.subplots(figsize=(8,6))
ax.plot(np.real(Z(w)),np.imag(Z(w)),lw=2)
ax.plot(np.real(Zp),np.imag(Zp),"o",c="red")
ax.set(title="Ortskurve",xlabel="Realteil in $\Omega$",
       ylabel="Imaginärteil in $\Omega$")
plt.grid(True)
plt.show()