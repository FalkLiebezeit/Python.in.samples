import numpy as np
from scipy.optimize import minimize

# Zielfunktion
def f(x):
    return x**2 + 10*np.sin(x)

result = minimize(f, x0=0)
print("Minimum bei:", result.x)