#abb_14_02.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode

a=np.loadtxt("../daten.txt")
modus=mode(a)
m=modus[0]
median=np.median(a)
mu=np.mean(a)
sigma=np.std(a)
textstr = '\n'.join((
    r'$x_{mod}=%.2f$' % (m, ),
    r'$\bar{x}=%.2f$' % (mu, ),
    r'$\tilde{x}=%.2f$' % (median, ),
    r'$\sigma=%.2f$' % (sigma, )))
n=len(a)
k=round(np.sqrt(n)+1) #Anzahl der Klassen
#
fig,ax=plt.subplots(figsize=(8,6))
ax.hist(a,bins=k,edgecolor='b',color='w')
ax.set_xlabel("Messwerte")
ax.set_ylabel("absolute Häufigkeit")
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.7, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
plt.show()