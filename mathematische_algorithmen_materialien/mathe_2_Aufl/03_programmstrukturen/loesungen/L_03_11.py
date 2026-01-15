#L_03_11.py
#Multiplikation einer Matrix mit einer Konstanten
s=2
a=[[10,11,12,13,15],
   [14,15,16,17,18],
   [18,19,20,21,25],
   [22,23,24,25,27],
   [32,33,34,35,38]]
m=len(a) #Anzahl der Zeilen
#Leere (m,m) - Liste erzeugen
c=[[0]*m for i in range(m)]
for i in range(m):    #Zeilen
    for j in range(m):#Spalten
        c[i][j]=s*a[i][j]
#Ausgabe
print("Matrix a")
for i in range(m):print(a[i])
print("Matrix c")
for i in range(m):print(c[i])