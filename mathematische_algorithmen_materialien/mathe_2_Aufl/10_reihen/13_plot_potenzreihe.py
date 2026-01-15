#13_plot_potenzreihe.py
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,0.999,100)
y=1/(1-x)
ya=1+x+x**2+x**3+x**4+x**5
fig, ax =plt.subplots()
ax.set_ylim(0,5)
ax.plot(x,y,'b',lw=2,label='genau')
ax.plot(x,ya,'r--',lw=2,label='approximiert')
ax.set(xlabel='x',ylabel='y')
ax.legend(loc='best')
plt.show()
