#20_scipy_nichtlinear2.py
from scipy.optimize import fsolve,newton
def f(x):
    x1,x2=x
    f1= x1**2 + x2 -  5
    f2=-x1    + x2**2-5
    return [f1,f2]
print("Lösungsvektoren")
start=[-3,-2],[-2,2],[1,3],[2,-3]
for k in start:
    print(fsolve(f,[k]))

