#11_einfaerben_parabel.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 5,100)
y1 = (x-3)**2
y2 = -(x-2)**2+8
fig, ax=plt.subplots()
ax.plot(x, y1, x, y2, color='black')
ax.fill_between(x, y1, y2, where=y2 >=y1, facecolor='b', alpha=0.2)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()