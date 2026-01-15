def f(x):
    return x**2

a,b=0,10
n=1
h=b-a
r=(f(a)+f(b))*h/2

for i in range(1,5):
    r=(r+h*sum(f(a+(i-1/2)*h)))/2
    for j in range(1,i):
        r=(4**j*r-r)/(4*+j-1)
    n=2*n
    h=h/2
print(r)

