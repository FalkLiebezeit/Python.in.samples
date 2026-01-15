#L_05_09.py
#e-Funktion für positives Wachstum
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,36,500)
a=1             #Anfangswert
b=0.02          #2 Prozent Wachstum
y=a*np.exp(b*t) #Wachstumsfunktion
#Grafikbereich
fig, ax = plt.subplots(figsize=(8,6),label='Exponentielles Wachstum')
ax.plot(t,y)
ax.set_title(r'$y\left( t\right)  =a\cdot e^{b\cdot t}$')#Wachstumsfunktion
ax.set_xlabel('Zeit t')
ax.set_ylabel('y',rotation=True)
plt.show()
