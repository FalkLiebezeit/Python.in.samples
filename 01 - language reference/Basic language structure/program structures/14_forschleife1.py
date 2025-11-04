#14_forschleife1.py
def f(x):
    return x**2
    
print(" x\ty")
for x in range(11):
    y=f(x)
    print("%2i  %6.3f" %(x, y))
