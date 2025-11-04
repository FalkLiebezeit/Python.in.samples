#09_logachse.py
import numpy as np
import matplotlib.pyplot as plt
omega=np.linspace(0.1,100,1000)
fig, ax = plt.subplots()
for n in range(1,4):
    A=1./(np.sqrt(1.+omega**(2*n)))
    ax.semilogx(omega,A)
ax.set_xlabel('Frequenz in Hz')
ax.set_ylabel('A')
ax.grid(True)
fig.show()
#unter Zeile 5 einfügen:
#ax.set_xscale('log')
#ax.plot(omega,A)