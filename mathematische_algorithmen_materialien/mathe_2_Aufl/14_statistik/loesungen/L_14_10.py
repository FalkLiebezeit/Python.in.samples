#L_14_10.py
import numpy as np
from scipy.stats import skew,kurtosis
import matplotlib.pyplot as plt
#
n=2
#n=3
#n=4
#n=5
a=np.random.weibull(n,1000)
#
xmax=2.65
x0=0.1
y0=150
dd=6
#Grafikbereich
fig,ax=plt.subplots(figsize=(8,8))
ax.hist(a,bins=20,edgecolor='b',color='w')
ax.text(x0,y0,r"$\bar{x}=%.2f$" %(np.mean(a)),fontsize=12)
ax.text(x0,y0-dd,r"$\tilde{x}=%.2f$" %(np.median(a)),fontsize=12)
ax.text(x0,y0-dd*2,r"$s=%.2f$" %(np.std(a,ddof=1)),fontsize=12)
ax.text(x0,y0-dd*3,r"$S=%.2f$" %(skew(a)),fontsize=12)
ax.text(x0,y0-dd*4,r"$w=%.2f$" %(kurtosis(a)),fontsize=12)
ax.set_xlim(0,xmax)
ax.set_ylim(0,y0+dd)
plt.show()

