#16_forschleife3.py
def f(x,y):
    return x*y

x0=0
xn=1
y0=1
n=1000
delta_x=(xn-x0)/n
y=y0
for k in range(n+1):
    x=x0+k*delta_x
    y=y + f(x,y)*delta_x
print("%3i %6.3f  %6.4f" %(k, x, y))