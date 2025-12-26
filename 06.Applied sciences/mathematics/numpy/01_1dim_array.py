#01_1dim_array.py
import numpy as np
x1=list(range(10))
x2=np.arange(10)
x3=np.arange(1,10,0.5)
x4=np.linspace(1,10,10)
x5=np.linspace(1,10,10,endpoint=False)
print("Python Liste:",type(x1),"\n",x1)
print("arange() Schrittweite 1:",type(x2),"\n",x2)
print("arange() Schrittweite 0.5:",type(x3),"\n",x3)
print("linspace() Schrittweite 1:",type(x4),"\n",x4)
print("linspace() Schrittweite 0.9:",type(x5),"\n",x5)