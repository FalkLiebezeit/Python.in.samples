#03_grid.py
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,20,500)
u=325*np.sin(2*np.pi*50*t/1000)
fig=plt.figure()
ax=fig.add_subplot()
#fig, ax = plt.subplots()
ax.plot(t,u,linewidth=2)
ax.grid(color='black',linestyle='solid',lw=0.5)
#ax.grid(color='black',ls='dashed',lw=0.5)
#ax.grid(color='black',ls='dotted',lw=0.5)
#ax.grid(color='black',ls='dashdot',lw=0.5)
#ax.grid(True)
plt.show()