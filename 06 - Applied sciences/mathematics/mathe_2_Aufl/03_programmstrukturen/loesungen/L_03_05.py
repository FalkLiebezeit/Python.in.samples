#L_03_05.py
#for - while Vergleich
n=3
for i in range(n):
    for j in range(n):
        print("i: ", i, " j: ", j)
print()        
i=0
while i<n:
    j=0
    while j<n:  
        print("i: ", i, " j: ", j)
        j=j+1
    i=i+1