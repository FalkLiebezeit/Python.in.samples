#12_summe_matrix.py
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
b=[[9,8,7],
   [6,5,4],
   [3,2,1]]
n=len(a) #Anzahl der Zeilen
#Leere (n,n) - Liste erzeugen
c=[[0]*n for i in range(n)]
for i in range(n):    #Zeilen
    for j in range(n):#Spalten
        c[i][j]=a[i][j] + b[i][j]
#Ausgabe
print("Matrix A\n",a)
print("Matrix b\n",b)
print("Summe\n",c)

