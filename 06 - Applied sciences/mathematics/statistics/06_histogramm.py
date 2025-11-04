#06_histogramm.py
import numpy as np
import matplotlib.pyplot as plt
werte = np.loadtxt("./DataInput/daten.txt")
n=len(werte)
k=int(np.sqrt(n)+0.5)
fig, ax=plt.subplots()
ax.hist(werte,bins=k,edgecolor="b",color="w")
ax.set(xlabel="Messwerte",ylabel="absolute Häufigkeit")
plt.show()
