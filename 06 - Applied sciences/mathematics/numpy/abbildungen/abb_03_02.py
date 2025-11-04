#03_002.py
#Vektoren addieren
import numpy as np
import matplotlib.pyplot as plt

F1x,F1y=-6,4
F2x,F2y=4,-8
F3x,F3y=4,2
Fresx=F1x+F2x+F3x
Fresy=F1y+F2y+F3y

plt.quiver([F1x],[F1y], angles='xy', scale_units='xy', scale=1,color='r')
plt.quiver([F2x],[F2y], angles='xy', scale_units='xy', scale=1,color='g')
plt.quiver([F3x],[F3y], angles='xy', scale_units='xy', scale=1,color='y')
plt.quiver([Fresx],[Fresy], angles='xy', scale_units='xy', scale=1,color='b')
plt.text(2.1,-2,r"$F_{res}$",fontsize=12)
plt.text(-5.8,3.0,r"$F_{1}$",fontsize=12)
plt.text(4.1,-7.8,r"$F_{2}$",fontsize=12)
plt.text(4,1.7,r"$F_{3}$",fontsize=12)
plt.xticks([-6,-4,-2,0,2,4,6])
plt.yticks([-8,-6,-4,-2,0,2,4])
plt.grid(True)
#plt.savefig("03_002.png")
#plt.savefig("03_002.svg")
plt.show()
