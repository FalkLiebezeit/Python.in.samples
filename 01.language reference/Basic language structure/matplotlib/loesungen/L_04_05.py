#L_04_05.py
#Unterdiagramme untereinander
import numpy as np
import matplotlib.pyplot as plt
L=0.1 #Induktivität in H
C=2   #Kapazität in F
f = np.linspace(0.1, 5, 1000) #Werte für Frequenzbereich
XL=2*np.pi*f*L #Funktionsfefinition für induktivemn Blindwiderstand
Xc=1/(2*np.pi*f*C) #Funktionsdefinition für kapazitiven Blindwiderstand
fig, ax = plt.subplots(2)#ax-Objekt für 2 Unterdiagramme
#Induktivität
ax[0].plot(f, XL,color="blue",linewidth=2)
ax[0].set(ylabel=r'$X_L$',title='induktiver Blindwiderstand')
ax[0].text(0.065,2.2,r'$X_{L}= \omega L$',fontsize=12)
ax[0].grid(True)
#Kapazität
ax[1].plot(f,Xc,color="red",linewidth=2)
ax[1].set(xlabel='f in Hz',ylabel=r'$X_c$',title='kapazitiver Blindwiderstand')
ax[1].text(0.2,0.65,r'$X_{C}=\frac{1}{\omega C} $',fontsize=12)
ax[1].grid(True)
fig.tight_layout()
plt.show()
