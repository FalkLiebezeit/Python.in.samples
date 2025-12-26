#29_getriebe.py
import matplotlib as mlt
import matplotlib.pyplot as plt
x1,x2=-12,22
y1,y2=-17,12
fig,ax=plt.subplots()
ax.axis([x1,x2,y1,y2])
#(x,y),Radius
k1=mlt.patches.Circle((-5,5),5,fill=False,lw=2,edgecolor='b')
k2=mlt.patches.Circle((-5,-5),5,fill=False,lw=2,edgecolor='b')
k3=mlt.patches.Circle((10,-5),10,fill=False,lw=2,edgecolor='b')
ax.add_patch(k1)
ax.add_patch(k2)
ax.add_patch(k3)
#x1,x2,y1,y2
ax.plot([-5,-5],[-5, 5],lw=1,color='black',ls='-.')
ax.plot([-5,10],[-5,-5],lw=1,color='black',ls='-.')
ax.plot([-5,10],[5,-5],lw=1,color='black',ls='-.')
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
plt.show()
'''
ax.set_axis_off() #Alternative für Zeile 22
'''