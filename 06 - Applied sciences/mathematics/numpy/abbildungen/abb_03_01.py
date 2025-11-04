#Vektoren verschieben
import numpy as np
import matplotlib.pyplot as plt
x1,y1=2,4
x2,y2=6,4
dx,dy=0,0

plt.quiver([x1+dx],[y1+dy],[x2],[y2], angles='xy', scale_units='xy', scale=1,color='r')
dx,dy=-4,-10
plt.quiver([x1+dx],[y1+dy],[x2],[y2], angles='xy', scale_units='xy', scale=1,color='g')
dx,dy=-2,-4
plt.quiver([x1+dx],[y1+dy],[x2],[y2], angles='xy', scale_units='xy', scale=1,color='b')
dx,dy=-10,-10
plt.quiver([x1+dx],[y1+dy],[x2],[y2], angles='xy', scale_units='xy', scale=1,color='k')

plt.xticks([-10,-8,-6,-4,-2,0,2,4,6,8,10])
plt.yticks([-10,-8,-6,-4,-2,0,2,4,6,8,10])
plt.grid(True)
#plt.savefig("abb_03_01.png")
#plt.savefig("abb_03_01.svg")
plt.show()
