#04_reihenschwingkreis.py
import numpy as np
import matplotlib.pyplot as plt
U=230 #int!
R=10  #int!
C=1e-6
L=1e-2
w=2.0*np.pi*np.linspace(0.01,3e3,1000)
Z=R+1j*w*L+1.0/(1j*w*C) 
I=U/Z
fig,ax=plt.subplots(figsize=(8,6))
ax.plot(w,np.real(I),lw=2,color="red",label="Realteil")
ax.plot(w,np.imag(I),lw=2,color="green",label="Imaginärteil")
#ax.plot(w,I,lw=2,color="red")
ax.set(xlabel="$\omega$ 1/s",ylabel="I in A")
plt.legend(loc="best")
plt.grid(True)
plt.show()

