#17_qrt_grafik.py
import numpy as np
import matplotlib.pyplot as plt
zeilen=5
spalten=10
A3=1.152
B4=1.669
werte = np.loadtxt("./DataInput/daten.txt")
n=len(werte)
tabelle=np.reshape(werte,(zeilen,spalten),order='F')
h=np.linspace(1,spalten,spalten)
mw=[]
staw=[]
for i in range(spalten):
    mw.append(round(np.mean(tabelle[0:zeilen,i]),2))
    staw.append(round(np.std(tabelle[0:zeilen,i],ddof=1),3))
mmw=np.mean(mw)
mws=np.mean(staw)
OEGm=mmw+A3*mws
UEGm=mmw-A3*mws
OEGs=B4*mws
x=[1,spalten]
y1=[OEGm,OEGm]
y2=[mmw,mmw]
y3=[UEGm,UEGm]
y4=[OEGs,OEGs]
fig, ax = plt.subplots(2, 1)
ax[0].set_title("Mittelwertkarte")
ax[0].plot(x,y1,'r-')
ax[0].plot(x,y2,'g-')
ax[0].plot(x,y3,'r-')
ax[0].plot(h,mw,'bx-')
ax[0].set_ylabel("Mittelwert")
ax[1].set_title("Standardabweichungskarte")
ax[1].plot(x,y4,'r-')
ax[1].plot(h,staw,'gx-')
ax[1].set_xlabel("Stichproben")
ax[1].set_ylabel("s")
fig.tight_layout()
plt.show()