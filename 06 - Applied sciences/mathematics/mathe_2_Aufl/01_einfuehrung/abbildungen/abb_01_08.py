#abb_01_08.py
#Rundungs- und Verfahrensfehler
import numpy as np
import matplotlib.pyplot as plt

x  = np.arange(0, 3, .02)
f1 = np.exp(x) #Rundungsfehler
f2 = f1[::-1]  #Verfahrensfehler

fig, ax = plt.subplots(figsize=(6,4))
ax.plot(x, f1, 'r--', label="Rundungsfehler")
ax.plot(x, f2, 'b:', label="Verfahrensfehler")
ax.plot(x, f1 + f2, 'k', label="Gesamtfehler")

legend = ax.legend(loc='upper center', shadow=True, fontsize='12')

ax.set_xlabel("Anzahl der Rechenoperationen")
ax.set_ylabel("Fehler")
ax.set_xticks([])
ax.set_yticks([])
plt.show()
'''
fig.savefig("/Users/veit/documents/Python_Mathe/Dateien_fuer_Autor/Abbildungen/01_008.png")
'''