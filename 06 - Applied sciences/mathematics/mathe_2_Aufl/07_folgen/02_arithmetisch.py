#02_arithmetisch.py
def a(n):
    return 4*n
print("n   a(n)   a(n+1)-a(n)  (a(n+1)+a(n-1))/2")
for n in range(1,11):
    f1=a(n)
    f2=a(n+1)-a(n)
    f3=(a(n+1)+a(n-1))/2
    print("%2i %5.0f\t%3.0f\t\t%3.0f"%(n,f1,f2,f3))
    