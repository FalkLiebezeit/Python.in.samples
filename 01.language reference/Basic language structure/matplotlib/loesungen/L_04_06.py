#L_04_06.py
#Wellenausbreitung: Zeitbild und Ortsbild
#Unterdiagramme nebeneinander
import numpy as np
import matplotlib.pyplot as plt
f=440   #Frequenz in Hz
c=340   #Schallgeschwindigkeit in m/s
#Berechnungen
w=2*np.pi*f      #Kreisfrequenz
T=  2*np.pi/w    #Periodendauer
lam=f/c
k=2*np.pi/lam #Wellenzahl
#Wertebereich
t = np.linspace(0, T, 500) #Zeitbereich
x = np.linspace(0,lam,500) #Ausdehnung der Welle
#Funktionsdefinition
y1=10*np.sin(w*t) #Zeitbild
y2=10*np.sin(k*x) #Ortsbild
#zwei Unterdiagramme nebeneinander
fig, ax = plt.subplots(1,2,figsize=(10,3),label='f = 440 Hz')
#Zeitbild
ax[0].spines[['top', 'right']].set_visible(False)
ax[0].spines[['left','bottom']].set_position(("data", 0))
ax[0].plot(1e3*t, y1,'b-',lw=1.5)
ax[0].set_title('Zeitbild')
ax[0].set_xlabel('t/ms',loc='right')
ax[0].set_ylabel('y',loc='top',rotation=0)
ax[0].plot(1,0,'>k',transform=ax[0].get_yaxis_transform(),clip_on=False)
ax[0].plot(0,1,'^k',transform=ax[0].get_xaxis_transform(),clip_on=False)
ax[0].text(2.1,1.4,r'$T=\frac{2\pi }{\omega } $',fontsize=12)
#Ortsbild
ax[1].spines[['top', 'right']].set_visible(False)
ax[1].spines[['left','bottom']].set_position(("data", 0))
ax[1].plot(x,y2,'r-',lw=1.5)
ax[1].set_title('Ortsbild')
ax[1].set_xlabel('x/m',loc='right')
ax[1].set_ylabel('y',loc='top',rotation=0)
ax[1].plot(1,0,'>k',transform=ax[1].get_yaxis_transform(),clip_on=False)
ax[1].plot(0,1,'^k',transform=ax[1].get_xaxis_transform(),clip_on=False)
ax[1].text(1.2,1.4,r'$\lambda =\frac{2\pi }{k} $',fontsize=12)
fig.tight_layout()
# fig.savefig('04_041.png')
# fig.savefig('04_041.svg')
plt.show()