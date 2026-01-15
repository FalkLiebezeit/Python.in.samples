#11_001.py
import numpy as np
import matplotlib.pyplot as plt
#
def f(x):
    return x**2
#
def F(x):
    return x**3/3  
#Gerade
def gerade(x,a=0,b=10):
    return 0*x+(F(b)-F(a))/(b-a)
#
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(8,3),label='bestimmtes Integral')
x=np.linspace(0,10,100)
#links
ax1.plot(x,f(x),'r-',lw=1.5)
ax1.set(xlabel='x',ylabel='y',title=r'$\int^{10}_{0} x^{2}dx=\frac{1000}{3}$')
ax1.fill_between(x,f(x), where=f(x)<100,alpha=0.2)
ax1.text(7.7,25.4,r'$\frac{1000}{3} $',fontsize=12)
ax1.set_ylim(0,100)
#rechts
ax2.plot(x,gerade(x),'r-')
ax2.fill_between(x,gerade(x),alpha=0.2)
ax2.set_xlabel('x')
ax2.set_ylim(0,60)
ax2.text(4.5,13.8,r'$\frac{1000}{3} $',fontsize=12)
fig.tight_layout()
plt.show()

