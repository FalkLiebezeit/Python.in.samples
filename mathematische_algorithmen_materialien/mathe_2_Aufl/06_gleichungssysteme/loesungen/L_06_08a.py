#L_06_08a.py
from scipy.optimize import fsolve
#from scipy.optimize import broyden1,broyden2,newton_krylov,anderson,
def f(x):
    x1,x2=x
    f1= x1 + x2 + 1
    f2=-x1**2 + x2 + 3
    return [f1,f2]
#berechnet jeweils nur einen Lösungsvektor
L = fsolve(f,[-3,2])
print("Lösungsvektor\n",L)