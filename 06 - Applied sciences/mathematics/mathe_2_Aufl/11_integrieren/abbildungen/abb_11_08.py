#abb_11_08.py
#Dreieck
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

fig,ax = plt.subplots()
ax.vlines(5,0,3,color='b')
ax.hlines(0,0,5,color='b')
ax.add_artist(lines.Line2D([0, 5], [0, 3],color='b'))
ax.text(2.5,-0.3,r"$\Delta x$",fontsize=12)
ax.text(5.1,1.4,r"$\Delta y$",fontsize=12)
ax.text(2.5,1.8,r"$\Delta s$",fontsize=12)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
plt.show()

