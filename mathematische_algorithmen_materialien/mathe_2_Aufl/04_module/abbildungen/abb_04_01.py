#abb_04_01.py
#NumPy ndarray
import matplotlib.pyplot as plt
from matplotlib import patches
#
sg=11
fig, ax = plt.subplots(figsize=(5,2),linewidth=20)
#x1,x2,y1,y2
ax.axis([-1,121,-5,42])
#x1,y1,x2,y2
header = patches.Rectangle((0,0),19,10,fill=False,lw=2,color='red')
array = patches.Rectangle((20,0),100,10,fill=False,lw=2,color='blue')
data_type = patches.Rectangle((20,30),40,10,fill=False,lw=2,color='blue')
head = patches.Rectangle((90,30),10,10,fill=False,lw=2,color='red')
s = patches.Rectangle((90,0),10,10,fill=False,lw=2.5,color='red')
for x in range(1,10):
    ax.vlines(x*10+20,0,10,color='r')
plt.vlines(8,10,35,color='black')
#x,y,dx,dy
ax.arrow(8,35,12,0,width=0.1,head_width=2.8,length_includes_head=True)
ax.arrow(60,35,30,0,width=0.1,head_width=2.8,length_includes_head=True)
ax.arrow(95,10,0,20,width=0.1,head_width=2.8,length_includes_head=True)
ax.add_patch(header)
ax.add_patch(array)
ax.add_patch(data_type)
ax.add_patch(head)
ax.add_patch(s)
#Beschriftungen
ax.text(31,33,"data-type",fontsize=sg)
ax.text(91,41.5,"head",fontsize=sg)
ax.text(2,3.2,"header",fontsize=sg)
ax.text(50,-5,"ndarray",fontsize=sg)
ax.text(102,31,"array \n scalar",fontsize=sg)
ax.axis('off')
ax.set_aspect('equal')
plt.tight_layout()
plt.show()

