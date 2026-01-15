#L_03_10.py
#Transponieren einer Matrix
a=[[10,11,12,13],
   [14,15,16,17],
   [18,19,20,21],
   [22,23,24,25]]
n=len(a) #Anzahl der Zeilen
#Leere (n,n) - Liste erzeugen
c=[[0]*n for i in range(n)]
for i in range(n):    #Zeilen
    for j in range(n):#Spalten
        c[i][j]=a[j][i]
#Ausgabe
print("Matrix a")
for i in range(n):print(a[i])
print("Transponierte Matrix")
for i in range(n):print(c[i])

'''
a=[[10,11],
   [14,15]]

b=[[10,11,12,13],
   [14,15,16,17],
   [18,19,20,21],
   [22,23,24,25]]

'''
'''
Die Laufzeit ist proportional zu n
'''