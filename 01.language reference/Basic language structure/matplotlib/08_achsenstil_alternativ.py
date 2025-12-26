#08_achsenstil.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import AxesZero
fig = plt.figure()
ax = fig.add_subplot(axes_class=AxesZero)
for achsen in ['xzero', 'yzero']:
    ax.axis[achsen].set_visible(True)#Achsenposition
for raender in ['left', 'right', 'bottom', 'top']:
    ax.axis[raender].set_visible(False)#Raender unsichtbar
ax.text(5.5,-1.4,'x')
ax.text(-1,22,'f(x)')
x = np.linspace(-5, 5, 100)
ax.plot(x, x**2-4,'r-',lw=2)
plt.show()
#unter Zeile 8 einfügen
#ax.axis[achsen].set_axisline_style('-|>')
