#L_04_01.py
#Matrix transponieren
import numpy as np
a=np.array([[1,2,3],
           [4,5,6],
           [7,8,9]])
n=len(a[0])       #Anzahl der Zeilen
c=np.zeros([n,n]) #leere (n,n)-Matrix erzeugen
for i in range(n):    #Zeilen
    for j in range(n):#Spalten
        c[j,i]=a[i,j]
#Ausgabe
print("Matrix A\n",a)
print("Transponierte von A\n",c)

