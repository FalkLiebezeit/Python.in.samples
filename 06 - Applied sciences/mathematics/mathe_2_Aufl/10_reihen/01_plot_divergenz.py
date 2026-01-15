#01_plot_divergenz.py
import matplotlib.pyplot as plt
summe=0
fig, ax = plt.subplots()
for k in range(1,11):
    summe=summe + k**2
    ax.scatter(k,k**2,marker='x',color='b')
    ax.scatter(k,summe,marker='+',color='r')
ax.set_title(r'$\sum^{n}_{k=1} k^{2}$')
ax.set(xlabel='k',ylabel=r'$k^{2},\  \sum^{}_{} k^{2}$')
ax.text(8,35,"Folge",fontsize=12)
ax.text(8,300,"Reihe",fontsize=12)
plt.show()