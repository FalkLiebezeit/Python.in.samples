#10_skalarprodukt.py
a=[1,2,3]
b=[3,2,1]
n=len(a) #Anzahl der Elemente
c=0
for i in range(n):  
    c = c + a[i]*b[i]
#Ausgabe
print(a)
print(b)
print("Skalarprodukt:",c)

