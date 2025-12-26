#15_subplot_polar_sinus.py
import numpy as np
import matplotlib.pyplot as plt

def theta_rad(winkel1,winkel2):
    theta=[winkel1,winkel2]
    return np.radians(theta)

winkel=45
x=np.linspace(0, 360, 500)
y=np.sin(np.pi*x/180)
r=[np.cos(np.radians(winkel)),1]
fig=plt.figure(figsize=(8,4))
#Polarkoordinaten
ax1=fig.add_subplot(1,2,1,projection='polar')
ax1.set_rticks([])
ax1.plot(theta_rad(0,winkel),[0,1],'b',lw=2)
ax1.plot(theta_rad(0,winkel),r,'b',lw=2)
ax1.plot(theta_rad(0,winkel),[0,1],'ro')
ax1.grid(True)
#kartesische Koordinaten
ax2=fig.add_subplot(1,2,2)
ax2.spines[['top', 'right']].set_visible(False) 
ax2.spines[['bottom','left']].set_position(('data',0))
ax2.plot(x, y,'b',linewidth=2)
ax2.plot(winkel,np.sin(np.radians(winkel)),'ro')
ax2.plot(0,np.sin(np.radians(0)),'ro')
wg=[]
for w in range(0,361,45):
    wg.append(w)
ax2.set_xticks(wg[1:])
ax2.set_xlabel('x in °',loc='right')
ax2.set_ylabel('f(x)',loc='top',rotation=0)
plt.show()
'''
#Ersatz für Zeile 30 bis 33
plt.xticks([45,90,135,180,225,270,315,360],
           [r'$\frac{1}{4}\pi$',r'$\frac{1}{2}\pi$',
            r'$\frac{3}{4}\pi$',r'$\pi$',r'$\frac{5}{4}\pi$',
            r'$\frac{3}{2}\pi$',r'$\frac{7}{4}\pi$',r'$2\pi$'])
'''