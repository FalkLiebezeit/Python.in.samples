#L_04_01.py
#zwei Funktionen
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,3,100)
y1=np.cos(x)
y2=x
fig, ax = plt.subplots()
ax.plot(x,y1)
ax.plot(x,y2)
plt.show()
