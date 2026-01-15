#abb_14_06.py
import numpy as np
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import scipy.stats as stats
#
x = np.linspace(-5, 5, 100)
#
fig, ax = plt.subplots(figsize=(8,6))
distnames = ['laplace', 'norm','uniform']
for distname in distnames:
    if distname == 'uniform':
        dist = getattr(stats, distname)(loc=-2, scale=4)
    else:
        dist = getattr(stats, distname)
    data = dist.rvs(size=1000)
    w = kurtosis(data, fisher=False) #Wölbung
    y = dist.pdf(x)
    ax.plot(x, y,label="{}:{}".format(distname,round(w, 3)))
    ax.legend()
ax.set_xlabel(r"$x$",fontsize=12)
ax.set_ylabel(r"$f(x)$",rotation=0,fontsize=12)
plt.show()
