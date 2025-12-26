#L04_04.py
'''Oberschwingungen für Rechteckfunktion'''
import numpy as np
import matplotlib.pyplot as plt
#Synthese von Recht- oder Saegezahn-Schwingungen
def fourier(n=9):
    fig, ax = plt.subplots()
    x=np.linspace(0,4*np.pi,500)
    s=0
    for k in range(1,n,2):
        y=10*np.sin(k*x)/k
        s=s+y
        ax.plot(x,y)
    ax.plot(x,s)
    plt.show()
#Funktionsaufruf
fourier(30)