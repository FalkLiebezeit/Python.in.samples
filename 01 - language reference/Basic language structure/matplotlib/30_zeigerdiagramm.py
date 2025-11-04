#30_zeigerdiagramm.py
import matplotlib.pyplot as plt
x1,x2=0,12
y1,y2=0,8
lb=2   #Linienbreite
pb=0.5 #Pfeilbreite
pl=1   #Pfeillänge
U_R=10 #ohmscher Spannungsfall
U_L=5  #induktiver Spannungsfall
I=12   #Stromstärke 
fig,ax=plt.subplots()
ax.axis([x1,x2,y1,y2])
#Pfeile: x,y,x+dx,y+dy
ax.arrow(0,1.8,I,0,color='r',lw=lb,length_includes_head=True,
         head_width=pb,head_length=pl)
ax.arrow(0,2,U_R,0,color='b',lw=lb,length_includes_head=True,
         head_width=pb,head_length=pl)
ax.arrow(U_R,2,0,U_L,color='b',lw=lb,length_includes_head=True,
         head_width=pb,head_length=pl)
ax.arrow(0,2,U_R,U_L,color='b',lw=lb,length_includes_head=True,
         head_width=pb,head_length=pl)
#Beschriftungen
ax.annotate("$I$",xy=(5,1),xytext=(5,1),fontsize=12)
ax.annotate("$U_g$",xy=(5,5),xytext=(5,5.5),fontsize=12)
ax.annotate("$U_L$",xy=(10.5,4),xytext=(10.5,4),fontsize=12)
ax.annotate("$U_R$",xy=(5,3),xytext=(5,2.5),fontsize=12)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
ax.set_aspect('equal')
plt.show()
'''
ax.set_axis_off() #Alternative für Zeile 29
'''