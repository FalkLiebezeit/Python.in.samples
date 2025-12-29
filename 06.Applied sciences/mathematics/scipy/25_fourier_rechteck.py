#25_fourier_rechteck.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,fftfreq  
f=50     #Frequenz in Hz
T=1/f    #Periodendauer
umax=325 #Amplitude
N=6000   #Anzahl der Abtastungen
Ta=T/N   #Abtastzeit
t=np.linspace(0,T,N)
#Klirrfaktor berechnen
def klirrfaktor(u):
    z=0
    for i in range(1,len(u)):
        z=z+u[i]**2  
    return np.sqrt(z)/u[0]   
#Rechteckfunktion
@np.vectorize
def ur(t):
    if t < T/2:
        return umax
    else:
        return -umax
#Sägezahn
@np.vectorize
def us(t):
    return 1e4*(t-T/2)
#Dreieck
@np.vectorize
def ud(t):
    m=100
    if t < T/2:
        return m*t
    else:
        return -m*(t-T/2)+m*T/2
#Parabelbögen
@np.vectorize
def up(t):
    if t < T/2:
        return -(t-T/4)**2+(T/4)**2
    else:
        return (t-3*T/4)**2-(T/4)**2
u_t=ur(t)
#Transformation in den Frequenzbereich 
U_fft = fft(u_t)
#Beträge der Amplituden im Frequenzbereich
U_f=2*np.abs(U_fft)/N
#Oberschwingungen berechnen
fk=fftfreq(N,Ta)
pos=np.where(fk>0) #nur positve Frequenzen
#Unterdiagramme erzeugen
print("Klirrfaktor %2.3f"%klirrfaktor(U_f[pos]))
fig,ax=plt.subplots(2,1)
#Rechteckspannung darstellen
ax[0].plot(1e3*t,u_t,"b-",lw=2)
ax[0].set(xlabel="t in ms",ylabel="U in V")
#Frequenzspektrum darstellen
ax[1].stem(fk[pos],U_f[pos])
ax[1].set(xlabel="f in Hz",ylabel="Amplituden")
ax[1].set_xlim(0,1000)
fig.tight_layout()
plt.show()

# fig.savefig('06_037.png')
# fig.savefig('06_037.svg')