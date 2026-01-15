#05_plot_konvergenz.py
from math import *
import matplotlib.pyplot as plt
n=10
summe=0
fig, ax = plt.subplots()
for k in range(0,n+1):
    summe=summe+1/factorial(k)
    ax.scatter(k,summe,marker='x',color='r')
ax.hlines(exp(1),0,10,color='black',ls='dashed')
ax.set_title(r'$\sum^{\ n}_{k=0} \frac{1}{k!} $')
ax.set(xlabel='k',ylabel='Summe')
plt.show()
