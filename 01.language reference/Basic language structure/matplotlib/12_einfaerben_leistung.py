#12_einfaerben_leistung.py
import numpy as np
import matplotlib.pyplot as plt
f=50
URms=230
R=10
Xc=10
XL=0
Z=np.sqrt(R**2 + (XL-Xc)**2)
phi=np.arctan((XL-Xc)/R)
I=URms/Z
t=np.linspace(0,20,500)
u=np.sqrt(2)*URms*np.sin(2*np.pi*f*t*1e-3)
i=np.sqrt(2)*I*np.sin(2*np.pi*f*t*1e-3-phi)
p=u*i
fig, ax=plt.subplots()
ax.plot(t, p, color='black')
ax.fill_between(t,0,p,where=p>=0,facecolor='r',alpha=0.2,label="positiver Anteil")
ax.fill_between(t,0,p,where=p<=0,facecolor='g',alpha=0.2,label="negativer Anteil")
ax.set(xlabel='t in ms',ylabel='p(t) in Watt',title='Wechselstromleistung')
ax.legend(loc='best')
plt.show()