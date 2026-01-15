#06_plot_rekursion.py
import matplotlib.pyplot as plt
u=v=1
k=0.1   #Wachstumskonstante
Vmax=10 #Wachstumsschranke
delta_t=1
fig, ax = plt.subplots(label='Wachstum')
for i in range(26):
    u=u+k*delta_t*u
    v=v+k*delta_t*(Vmax-v)
    ax.plot(i,u,'ro')
    ax.plot(i,v,'bx')
ax.set(xlabel='Zeit',ylabel='Population')
plt.show()

# fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/07_005.pdf")
# fig.savefig("/Users/veit/documents/Python_Mathe/Export_Mathe_Python_neu/Abbildungen/07_005.svg")