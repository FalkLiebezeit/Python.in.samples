#04_beschriftungen_legende.py
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,20,0.001)
Ueff=[230,230] #für horizontale Linie
u=325*np.sin(2*np.pi*50*t*1e-3)
fig, ax = plt.subplots()
ax.plot(t,u,'b',lw=2,label='Momentanwert: u(t)')
ax.plot([0,20],Ueff,'r--',label='Effektivwert: 230V')
ax.plot(5,325,'ro',label="Spitzenwert:325V") #roter Punkt
ax.set(xlabel='t in ms',ylabel='u(t) in V',title='50 Hz Wechselspannung')
#ax.legend(loc='upper right')
#ax.legend(loc='lower left')
ax.legend(loc='best')
ax.grid(color='g',ls='dashed',lw='0.5')
plt.show()