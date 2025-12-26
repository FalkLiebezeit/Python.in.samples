#L03_04.py
#Lösen eines linearen Gleichungssystems
#gegeben ist die erweiterte Koeffizientenmatrix
import numpy as np
#erweiterte Koeffizientenmatrix
Ab = np.array([[3, 2, 1, 10],
               [1, 2, 3, 14],
               [2, 1, 4, 16]])
m=len(Ab) #Anzahl der Zeilen
A=Ab[0:m,0:m] #Koeffizientenmatrix
b=Ab[:,m]     #Inhomogenitätsvektor
#Lösung
loesung=np.linalg.solve(A,b)
#Ausgabe
print("Lösung eines linearen Gleichungssystems")
print("Koeffizientenmatrix\n",A)
print("Inhomogenitätsvektor\n",b)
print("Lösung:\n",loesung)



#print(m)

'''
#Koeffizientenmatrix
A = np.array([[3, 2, 1],
              [1, 2, 3],
              [2, 1, 4]])
#Inhomogenitätsvektor
b = np.array([10, 14, 16])
'''
