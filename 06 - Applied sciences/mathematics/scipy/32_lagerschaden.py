#32_lagerschaden.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,fftfreq    
f1=20 #1200 1/min
fn=[f1,2*f1,3*f1,4*f1,5*f1]
a1=[4,5,4,3,2,1] #defekt
a2=[4,0.22,0.21,0.15,0.11] #unbeschädigt
#Frequenz
T=20
N=5000
Ta=T/N #Abtastzeit
t = np.linspace(0,T,N)
#verrauschte Signale
ur = a1[0]*np.sin(2*np.pi*fn[0]*t)\
    +a1[1]*np.sin(2*np.pi*fn[1]*t)\
    +a1[2]*np.sin(2*np.pi*fn[2]*t)\
    +a1[3]*np.sin(2*np.pi*fn[3]*t)\
    +a1[4]*np.sin(2*np.pi*fn[4]*t)\
    +np.random.normal(size=N)

ug = a2[0]*np.sin(2*np.pi*fn[0]*t)\
    +a2[1]*np.sin(2*np.pi*fn[1]*t)\
    +a2[2]*np.sin(2*np.pi*fn[2]*t)\
    +a2[3]*np.sin(2*np.pi*fn[3]*t)\
    +a2[4]*np.sin(2*np.pi*fn[4]*t)\
    +np.random.normal(size=N)
#Transformation in den Frequenzbereich 
U_fftd = fft(ur) #defekt
U_fftg = fft(ug)
fk=fftfreq(N,Ta)
pos=np.where(fk>0)
#Beträge der Amplituden
Usd=2.0/N*np.abs(U_fftd) #defekt
Usf=2.0/N*np.abs(U_fftg) 
#Frequenzspektrum
fig,ax=plt.subplots(3,1,figsize=(6,6))
#Zeitbereich
ax[0].plot(t,ur,"b-",lw=1)
ax[0].set_xlim(0,10)
ax[0].set(xlabel="t in s",ylabel="a",title="verrauschtes Signal")
#beschädigtes Lager
ax[1].plot(fk[pos],Usd[pos],"r-",lw=2)
ax[1].set(xlabel="f in Hz",ylabel="a",title="beschädigtes Lager")
#unbeschädigtes Lager
ax[2].plot(fk[pos],Usf[pos],"g-",lw=2)
ax[2].set(xlabel="f in Hz",ylabel="a",title="unbeschädigtes Lager")
fig.tight_layout()
plt.show()

# fig.savefig('06_046.png')
# fig.savefig('06_046.svg')

