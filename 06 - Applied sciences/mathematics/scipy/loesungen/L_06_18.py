#L_06_18.py
#Klirrfaktor für Einweggleichrichtung
import numpy as np
import matplotlib.pylab as plt
from scipy.fft import fft,fftfreq  
f=50     #Frequenz in Hz
T=1./f   #Periodendauer
N=6000   #Anzahl der Abtastungen
Ta=T/N   #Abtastzeit
t=np.linspace(0,T,N)
#Klirrfaktor berechnen
def klirrfaktor(u):
    z=0
    for i in range(1,len(u)):
        z=z+u[i]**2  
    return np.sqrt(z)/u[0]   

@np.vectorize
def ug(t):
    umax=10
    if t < T/2:
        return umax*np.sin(2*np.pi*f*t)
    else:
        return 0

u_t=ug(t)
#Transformation in den Frequenzbereich 
U_fft = fft(u_t)
#Beträge der Amplituden im Frequenzbereich
U_f=2*np.abs(U_fft)/N
#Oberschwingungen berechnen
fk=fftfreq(N,Ta)
pos=np.where(fk>0) #nur positve Frequenzen
print("Klirrfaktor %2.3f"%klirrfaktor(U_f[pos]))
fig,ax=plt.subplots(2,1,figsize=(6,6))
#Rechteckspannung darstellen
ax[0].plot(1e3*t,u_t,"b-",lw=2)
ax[0].grid(True)
ax[0].set_xlabel("Zeit in ms");
ax[0].set_ylabel("Spannung in V",color="blue")
#Frequenzspektrum darstellen
ax[1].stem(fk[pos],U_f[pos])
ax[1].grid(True)
ax[1].set_xlabel("Frequenz f in Hz")
ax[1].set_ylabel("Amplituden")
ax[1].set_xlim(0,1000)
fig.tight_layout()
plt.show()

