#08_achsenstil.py
import numpy as np
import matplotlib.pyplot as plt
#Funktionsdefinition
def f(x):
    #y=np.sin(np.pi*x)
    y=x**2-4
    return y
#Grafikbereich
fig, ax = plt.subplots()
ax.spines[['top', 'right']].set_visible(False)
ax.spines[['left','bottom']].set_position(("data", 0))
x = np.linspace(-5, 5, 100)
ax.plot(x,f(x),'r-',lw=2)
ax.set_xlabel('x',loc='right')
ax.set_ylabel('f(x)',loc='top',rotation=0)
plt.show()

# ax.plot(1,0,'>k',transform=ax.get_yaxis_transform(),clip_on=False)
# ax.plot(0,1,'^k',transform=ax.get_xaxis_transform(),clip_on=False)