#L04_10.py
'''Zeigerdiagramm Reihenschwingkreis'''
import matplotlib.pyplot as plt
x1=0
x2=12
y1=-4
y2=8
lb=2   #Linienbreite
pb=0.5 #Pfeilbreite
pl=1   #Pfeillänge
U_R=10 #ohmscher Spannungsfall
U_L=5  #induktiver Spannungsfall
U_C=-12#kapazitiver Spannungsfall
I=12   #Stromstärke
fig,ax=plt.subplots()
ax.axis([x1,x2,y1,y2])
#Pfeile: x,y,x+dx,y+dy
#Strom
ax.arrow(0,1.8,I,0,color='r',lw=lb,length_includes_head=True,
         head_width=pb,head_length=pl)
#U_R
ax.arrow(0,2,U_R,0,color='b',lw=lb,length_includes_head=True,
         head_width=pb,head_length=pl)
#U_L
ax.arrow(U_R,lb,0,U_L,color='b',lw=lb,length_includes_head=True,
         head_width=pb,head_length=pl)
#U_C
ax.arrow(U_R,U_L+lb,0,U_L+U_C-lb-pl,color='b',lw=lb,length_includes_head=True,
         head_width=pb,head_length=pl)
#U_g
ax.arrow(0,lb,U_R,U_L+U_C+lb,color='b',lw=lb,length_includes_head=True,
         head_width=pb,head_length=pl)
#Beschriftungen
ax.annotate("$I$",xy=(5,1),xytext=(5,1),fontsize=12)
ax.annotate("$U_g$",xy=(5,1),xytext=(5,-2.1),fontsize=12)
ax.annotate("$U_L$",xy=(10.5,4),xytext=(10.5,4),fontsize=12)
ax.annotate("$U_R$",xy=(5,3),xytext=(5,2.5),fontsize=12)
ax.annotate("$U_C$",xy=(10.5,0),xytext=(10.5,-2),fontsize=12)
#keine Achsenbeschriftung
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
ax.set_aspect('equal')
plt.show()
