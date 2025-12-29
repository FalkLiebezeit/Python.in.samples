#06_linienstil.py
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,6.3,500)
y1=np.sin(x)
y3=np.sin(3*x)/3
y5=np.sin(5*x)/5
y7=np.sin(7*x)/7
y=y1+y3+y5+y7
fig, ax = plt.subplots()
ax.plot(x,y1,color='b',lw=2,linestyle='-')
ax.plot(x,y3,color='r',lw=2,linestyle='--')
ax.plot(x,y5,color='m',lw=2,linestyle=':')
ax.plot(x,y7,color='g',lw=2,linestyle='-.')
ax.plot(x,y,color='black',lw=3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
plt.show()