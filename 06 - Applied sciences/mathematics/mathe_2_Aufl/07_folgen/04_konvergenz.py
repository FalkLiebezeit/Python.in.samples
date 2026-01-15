#04_konvergenz.py
def a(n):
    return 2**(1/n)
    
def b(n):
    return (1/2)**(1/n)
    
def c(n):
    x=0.5
    return (1-x**n)**(1/n)

print(" n\ta(n)\t b(n)\t   c(n)")
print("______________________________________")
for n in range(1,11):
    print(" %2i| %3.6f | %3.6f | %3.6f" %(n,a(n),b(n),c(n)))
