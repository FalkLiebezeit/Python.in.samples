#L_08_03.py
import numpy as np
import matplotlib.pyplot as plt
U=100. #int!
R=10.  #int!
C=1e-6
L=1e-2
w=2.0*np.pi*np.linspace(2e2,1.5e4,1000)
Y=1./R+1/(1j*w*L)+1j*w*C 
I=Y*U
plt.figure(figsize=(8,6))
plt.plot(w,np.real(I),lw=2,color="black",label="Realteil")
plt.plot(w,np.imag(I),lw=2,color="green",label="Imaginärteil")
plt.plot(w,np.abs(I),lw=2,color="red",label="Betrag")
plt.xlabel("$\omega$ 1/s")
plt.ylabel("I in A")
plt.legend(loc="best")
plt.grid(True)
plt.show()


