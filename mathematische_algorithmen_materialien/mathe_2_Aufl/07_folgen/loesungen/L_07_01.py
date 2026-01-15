#L07_01.py
import matplotlib.pyplot as plt
#
def a(n):
    return 1/n
#Grafikbereich
fig, ax = plt.subplots()
for n in range(1,11):
    ax.scatter(n,a(n),marker='x',color='b')
    ax.scatter(n,a(n+1)-a(n),marker='+',color='r')
#Achsenbeschriftung
ax.set(xlabel='n',ylabel=r'$a_{n},a_{n+1}-a_{n}$')
ax.set_xlim(0.5,10.5)
ax.set_ylim(-1,1.1)
plt.show()

