#L06_12a.py
from scipy.optimize import fsolve
def f(x):
    x1,x2,x3=x
    f1=x1*x2 +x2 +x3 -13
    f2=2*x1 + x1*x2  +x3 -14
    f3=x1 + x2 +x2*x3 - 17
    return [f1,f2,f3]
print("Lösungsvektoren")
start=[-3,-2,1],[-2,2,1],[1,3,1]
for k in start:
    print(fsolve(f,[k]))