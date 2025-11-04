#L_04_02.py
'''rechte Achse beschriften'''
import numpy as np
import matplotlib.pyplot as plt
R=1
I=np.linspace(0,10,100)
U=R*I
P=R*I**2
fig=plt.figure()#fig-Objekt erzeugen
ax1=fig.add_subplot() #ax1 Objekt erzeugen
ax2=ax1.twinx() #ax2-Objekt für rechte Achsenbeschriftung
#Plotten
ax1.plot(I,U,'b-')
ax2.plot(I,P,'r-')
#Beschriftung der Achsen
ax1.set(xlabel='I in A',ylabel='U in V')
ax2.set(ylabel='P in W')
plt.show()

