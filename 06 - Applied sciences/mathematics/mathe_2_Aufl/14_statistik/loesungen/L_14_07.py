#L_14_07.py
import numpy as np

def stdaw(x):
    n=len(x)
    summe=0
    sum_rq=0
    for i in range(n):
        summe=summe + x[i]
        sum_rq=sum_rq + x[i]**2    
    mittelwert=summe/n
    v=(sum_rq - n*mittelwert**2)/(n-1)
    return np.sqrt(v)   

a=np.loadtxt("../daten.txt")
print("Standardabweichung")
print(stdaw(a))
print(np.std(a,ddof=1),"NumPy")