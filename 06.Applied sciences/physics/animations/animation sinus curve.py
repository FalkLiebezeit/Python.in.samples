
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

def f(x,k):
    return np.sin(x-k/20)

def v(k): 
    y.set_data(x,f(x,k))#;print(k)
    return y,

fig,ax=plt.subplots()
x=np.linspace(0,4*np.pi,200)
y, = ax.plot(x,f(x,0),'r-',lw=3)


#Animation
ani=FuncAnimation(fig,v,
                    interval=20,
                    #frames=200,
                    blit=True,
                    #save_count=50,
                    #cache_frame_data=False
                    )
#ani.save('wellen.mp4',fps=30) 
plt.show()
'''
#zum testen
y, = ax.plot([],[],'r-',lw=2)
ax.axis([0,4*np.pi,-1.2,1.2])
ani.save('wellen.mp4',fps=30) #
'''
