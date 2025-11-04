#L_08_04.py
import numpy as np
import matplotlib.pyplot as plt
R=60     #Widerstandsbelag
L=0.6e-3 #Induktivitätsbelag
G=1e-6   #Ableitungsbelag
C=50e-9  #Kapazitätsbelag
wp=1e3   #Kreisfreqenz im Punkt p
def Z(w):
    return np.sqrt((R+1j*w*L)/(G+1j*w*C))

w=2.0*np.pi*np.linspace(1,3e3,10000)
Zp=Z(wp)
plt.figure(figsize=(8,6))
plt.plot(np.real(Z(w)),np.imag(Z(w)),lw=2)
plt.plot(np.real(Zp),np.imag(Zp),"o",c="red")
plt.title("Ortskurve für Wellenwiderstand")
plt.xlabel("Realteil in $\Omega$")
plt.ylabel("Imaginärteil in $\Omega$")
plt.grid(True)
plt.show()
