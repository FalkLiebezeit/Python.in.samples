#23_heron2.py
def wurzel(z,n=5):
    a=(z+1)/2
    i=0
    while i<n:
        a=(a+z/a)/2
        i=i+1
    return a

z1=2
w=wurzel(z1)
print("Die Wurzel aus",z1,"ist:")
print(w)
print(z1**(1/2),"genau")
