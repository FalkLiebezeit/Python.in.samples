#07_plot_exp_ausgleich.py
import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt
xi=np.array([1,2,3,4,5])
yi=np.array([1,3,7,9,21])
ln_y=np.log(yi)
n=len(xi)
A=np.array([xi,np.ones(n)]).T
y=np.array([xi*ln_y,ln_y])
L=inv(A.T@A)@A.T@ln_y
a,b=np.exp(L[1]),L[0]
print("a=%2.3f b=%2.3f" %(a,b))
xa=np.linspace(0,np.max(xi),500)
ya=a*np.exp(b*xa)
fig, ax = plt.subplots()
ax.set(xlabel="x",ylabel="y",title=r"$y=ae^{bx}$")
ax.plot(xi,yi,'r+')
ax.plot(xa,ya,'b')
plt.show()
