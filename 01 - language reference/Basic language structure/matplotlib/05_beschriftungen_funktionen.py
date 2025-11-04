#05_beschriftungen_funktionen.py
import numpy as np
import matplotlib.pyplot as plt
R1,R2,R3=2,4,8
I=0.2
P=1
I=np.linspace(0.1, 1, 100)
U1=R1*I
U2=R2*I
U3=R3*I
U=P/I
fig, ax = plt.subplots()
ax.plot(I,U1,I,U2,I,U3,lw=2,color='blue')
ax.plot(I,U,lw=2,color='green')
ax.set(xlabel='I in A',ylabel='U in V',title='Leistungshyperbel U=P/I')
ax.annotate(r'$R_1$',xy=(1,2),xytext=(+2,-3),textcoords='offset points')
ax.annotate(r'$R_2$',xy=(1,4),xytext=(+2,-3),textcoords='offset points')
ax.annotate(r'$R_3$',xy=(1,8),xytext=(+2,-3),textcoords='offset points')
ax.grid(True)
plt.show()