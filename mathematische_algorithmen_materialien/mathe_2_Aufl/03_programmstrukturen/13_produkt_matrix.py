#13_produkt_matrix.py
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
b=[[9,8,7],
   [6,5,4],
   [3,2,1]]
n=len(a) #Anzahl der Zeilen
c=[[0]*n for i in range(n)]
for i in range(n):     #Zeilen
    for j in range(n): #Spalten
        for k in range(n):
            c[i][j]=c[i][j] + a[i][k]*b[k][j]            
#Ausgabe
print("Matrix A")
for i in range(n):print(a[i])
print("Matrix B")
for i in range(n):print(b[i])
print("Matrixprodukt")
for i in range(n):print(c[i])



