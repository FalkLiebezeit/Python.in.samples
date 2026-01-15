#03_007.py
#Laufzeitkomplexität
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.axisartist.axislines import AxesZero
#
n=np.linspace(1,10,200)
#
y0=np.log2(n+1)
y1=n
y2=n**2
y3=n**3
#Grafik
fig = plt.figure(label='Laufzeitkomplexität')
ax = fig.add_subplot(axes_class=AxesZero)
#Achsen
ax.axis['right'].set_visible(False)
ax.axis['top'].set_visible(False)
ax.axis['left'].set_axisline_style("-|>")
ax.axis['bottom'].set_axisline_style("-|>")
#Zeichnen
ax.plot(n,y0,'k-',label=r"$\mathcal{O}\left(log_{2}  n\right) $")
ax.plot(n,y1,'g-',label=r"$\mathcal{O}(n)$")
ax.plot(n,y2,'b-.',label=r"$\mathcal{O}(n^2)$")
ax.plot(n,y3,'r--',label=r"$\mathcal{O}(n^3)$")
ax.set_xlabel("Eingabegröße n",fontsize=12)
#ax.set_ylabel(r"$\mathcal{O}(n)$",rotation=90,fontsize=12)
ax.set_ylabel('Laufzeit in Schritten',fontsize=12)
ax.legend(loc='best',fontsize=12)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(1,5)
ax.set_ylim(1,5)
plt.show()