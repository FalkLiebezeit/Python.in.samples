#04_arithmetischer_mittelwert.py
import numpy as np

def arithmetischM(x):
    n=len(x)
    summe=0
    for i in range(n):
        summe=summe+x[i]
    return summe/n

a=np.loadtxt('daten.txt')
print("Arithmetischer Mittelwert")
print(arithmetischM(a))
print(np.mean(a),"NumPy")

