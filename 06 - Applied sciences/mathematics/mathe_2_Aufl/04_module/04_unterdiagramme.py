#04_unterdiagramme.py
import numpy as np
import matplotlib.pyplot as plt
#Funktionsdefinition
def f(x):
    return x**2,np.sin(x),x,np.cos(x)
#Grafikbereich
fig, ax = plt.subplots(2,2,label='Funktionen')
x=np.linspace(0,10,100)
for i,j,k in [[0,0,0],[0,1,1],[1,0,2],[1,1,3]]:
    ax[i,j].plot(x,f(x)[k])
fig.tight_layout()
plt.show()

# fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/04_004.pdf")
# fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/04_004.svg")