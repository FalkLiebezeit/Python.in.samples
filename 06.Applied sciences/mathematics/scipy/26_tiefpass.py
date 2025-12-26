#26_tiefpass.py
import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft,ifft,fftfreq 
f=50     #Frequenz in Hz
T = 1/f  #Periodendauer
fg=1.1*f #Grenzfrequenz
N=6000   #Anzahl Abtastungen
Ta=T/N   #Abtastzeit
t = np.linspace(0,T,N)
u_t=10*np.sin(2*np.pi*f*t)+8*np.random.randn(t.size)
#Transformation in den Frequenzbereich
U_fft = fft(u_t)
#Abtastfrequenz berechnen
fk = fftfreq(N,Ta)
#Signal im Frequenzbereich filtern
F_g=U_fft*(np.abs(fk) < fg)
#Rücktransformation in den Zeitbereich
u_g = ifft(F_g)
fig, ax=plt.subplots(2,1,figsize=(6,6))
#verrauschtes Signal
ax[0].plot(1e3*t, u_t)
ax[0].set(xlabel="t in ms",ylabel="u(t)",title="verrauschtes Signal")
#gefiltertes Signal
ax[1].plot(1e3*t, u_g.real,lw=2)
ax[1].set(xlabel="t in ms",ylabel="u(t)",title="gefiltertes Signal")
fig.tight_layout()
plt.show()

# fig.savefig('06_039.png')
# fig.savefig('06_039.svg')
