#L_03_16.py
#Potenz rekursiv
def potenz(a,n):
    if n==0:
        return 1
    else:
        return a*potenz(a,n-1)
a=2
n=100
print(potenz(a,n))
print(a**n)