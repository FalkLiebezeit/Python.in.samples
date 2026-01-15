#L_03_12.py
n=12
k=0
#Quadrat
for i in range(n):
    for j in range(n):
        print("* ",end='')
        k=k+1
    print()
print(k," ns")
#Dreieck
k=0
for i in range(n):
    for j in range(n-i):
        print("* ",end='')
        k=k+1
    print()
print(k," ns")