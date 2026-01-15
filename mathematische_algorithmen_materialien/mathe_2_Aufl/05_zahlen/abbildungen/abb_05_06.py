#abb_05_06.py
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
brueche=[1/2,1/4,1/8,1/16,1/32,1/32]
b=["1/2","1/4","1/8","1/16","1/32","1/32"]
a = (0.025, 0.1, 0.1, 0.1,0.1,0.1)
ax.pie(brueche,explode=a,labels=b,shadow=False)
ax.axis('equal')
plt.show()