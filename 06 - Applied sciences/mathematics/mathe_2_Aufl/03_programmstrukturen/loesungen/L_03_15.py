#L_03_15.py
#Gaussumme rekursiv
def gaussSumme(n):
    if n==0:
        return 0
    else:
        return n + gaussSumme(n-1)

n=100
print(gaussSumme(n))
print(n*(n+1)/2)
    