#19_meshgrid_demo.py
import numpy as np
import matplotlib.pyplot as plt
x=y=np.linspace(1,6,6)
x,y=np.meshgrid(x,y)
fig, ax=plt.subplots()
ax.plot(x,y,marker='x',color='red',ls='none')
plt.show()
#unter Zeile 7 einfügen
'''
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
'''