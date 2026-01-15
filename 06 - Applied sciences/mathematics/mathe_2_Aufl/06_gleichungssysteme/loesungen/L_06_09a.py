#L_06_09a.py
from scipy.optimize import fsolve
#from scipy.optimize import broyden1,broyden2,newton_krylov,anderson,
def f(x):
    x1,x2=x
    f1=2*x1**2 + x2**2 - 1
    f2=(0.5*x1-0.5)**2 + 2*(x2-0.25)**2 - 1
    return [f1,f2]
#berechnet jeweils nur einen Lösungsvektor
L = fsolve(f,[-3,4])
print("Lösungsvektor\n",L)