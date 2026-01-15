#L_07_4.py
def g(a1,q,n):
    a=a1
    al=[a1]
    for i in range(2,n+1):
        a=a*q
        al.append(a)
    return al
#
n=6
a1=5
q=3
print(g(a1,q,n))