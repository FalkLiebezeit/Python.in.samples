from scipy import integrate

# Funktion definieren
def f(x):
    return x**2

# Integriere f von 0 bis 1
result, error = integrate.quad(f, 0, 1)
print("Integral:", result)