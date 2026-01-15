#abb_14_04.py
#links- und rechtssteil
import numpy as np
import matplotlib.pyplot as plt
#
l=1
k=1.5
x=np.linspace(0,2.5,500)
h1=l*k*(l*x)**(k-1)*np.exp(-(l*x)**k)
h2 = h1[::-1]
fig,ax=plt.subplots()
ax.plot(x, h1,'r-')
ax.plot(x, h2,'b-')
#links
ax.vlines(0.468,0,0.742,label='Modus',ls='dashdot',color='r')
ax.vlines(0.6,0,0.722,label='Median',ls='dotted',color='g')
ax.vlines(0.7,0,0.695,label='Mittelwert',color='k')
#rechts
ax.vlines(1.8,0,0.695,color='k') #Mittelwert
ax.vlines(1.9,0,0.722,ls='dotted',color='g') #Median
ax.vlines(2,0,0.742,ls='dashdot',color='r') #Modus
#Steilheit
ax.text(0.3,0.9,"linkssteil",fontsize='11')
ax.text(1.7,0.9,"rechtssteil",fontsize='11')
ax.set_xlabel("x")
ax.set_ylabel("h(x)")
ax.legend(loc='lower center',fontsize='11')
ax.set_xticks([])
ax.set_ylim(0,1)
plt.show()