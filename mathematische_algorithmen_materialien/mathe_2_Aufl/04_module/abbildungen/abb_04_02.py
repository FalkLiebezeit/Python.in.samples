#abb_04_02.py
#Matplotlib-Objekte
import matplotlib.pyplot as plt
#
fig=plt.figure(figsize=(6,6))
#außen
ax1=fig.add_axes([.1, .1, .8, .8])
ax1.set_title('Figure',color='r')
ax1.text(0.01,0.01,'(0,0)') #links unten
ax1.text(0,01.01,'(0,1)')   #links oben
ax1.text(1,1.01,'(1,1)')    #rechts oben
ax1.text(1.01,0,'(1,0)')    #rechs unten
ax1.set_xticks([])
ax1.set_yticks([])
#ax1.set_lw=4
#innen
ax2=fig.add_axes([.2, .2, .6, .6])
ax2.set_title('Axes',color='b')
ax2.set_xticks([])
ax2.set_yticks([])
#plot area
ax3=fig.add_axes([.3, .3, .4, .4])
ax3.set_title('title')
ax3.set_xlabel('x_Label')
ax3.set_ylabel('y_Label')
ax3.text(0.4,0.05,'Axis',color='r')
ax3.text(0.05,0.4,'Axis',color='r',rotation=90)
ax3.text(.5, .5, 'plot area', ha='center', va='center',size=16, alpha=.5)
plt.show()