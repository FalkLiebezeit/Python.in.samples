#26_vektor_add.py
import matplotlib.pyplot as plt
xmin, xmax=-8, 5
ymin,ymax=-6, 6
F1x,F1y=-4,4
F2x,F2y=-4,-4
F3x,F3y=2,0
Fresx=F1x+F2x+F3x
Fresy=F1y+F2y+F3y
fig, ax=plt.subplots()
#Vektoren
ax.quiver(F1x,F1y,angles='xy',scale_units='xy', scale=1,color='m')
ax.quiver(F2x,F2y,angles='xy',scale_units='xy', scale=1,color='g')
ax.quiver(F3x,F3y,angles='xy',scale_units='xy', scale=1,color='b')
ax.quiver(Fresx,Fresy,angles='xy',
           scale_units='xy',scale=1,color='r',label="$F_{res}$")
ax.axis([xmin,xmax,ymin,ymax])
ax.set(xlabel="$F_{x}$",title="Vektoraddition")
ax.set_ylabel("$F_{y}$",rotation=True)
ax.legend(loc='best')
plt.show()
