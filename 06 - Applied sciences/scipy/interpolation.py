from scipy import interpolate
import numpy as np

x = np.linspace(0, 10, 10)
y = np.sin(x)

f = interpolate.interp1d(x, y)
print("Interpolierter Wert bei 5.5:", f(5.5))