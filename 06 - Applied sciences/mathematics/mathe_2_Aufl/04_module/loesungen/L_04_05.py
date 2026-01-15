#L_04_05.py
import numpy as np
import matplotlib.pyplot as plt
#Funktionsdefinition
def f(x):
    return -x**2 + 5*x - 3,-2*x + 5, 0*x - 2
#Grafikbereich
fig, ax = plt.subplots(3,1,label='Funktionen')
x=np.linspace(0,5,100)
ax[0].plot(x,f(x)[0])
ax[1].plot(x,f(x)[1])
ax[2].plot(x,f(x)[2])
fig.tight_layout()
plt.show()