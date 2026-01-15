#L_05_10.py
#e-Funktion für negatives Wachstum
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,5,100)
T_2=1                #Halbwertszeit
lam=np.log(2)/T_2    #Zerfallskonstante
y=100*np.exp(-lam*t) #radioaktver Zerfall
#Grafikbereich
fig, ax = plt.subplots(figsize=(8,6),label='Radioaktiver Zerfall')
ax.plot(t,y)
ax.set_xlabel('Zeit t')
ax.set_ylabel('N in %',rotation=True)
ax.text(3,70,r'$N\left( t\right)  =N_{0}\cdot e^{-\lambda \cdot t}$')
plt.show()