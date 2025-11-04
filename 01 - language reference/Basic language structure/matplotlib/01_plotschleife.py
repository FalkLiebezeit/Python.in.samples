#01_plotschleife.py
import matplotlib.pyplot as plt
lx,ly =[],[]
for x in range(11):
    y=x**2
    lx.append(x)
    ly.append(y)
plt.plot(lx,ly)
plt.show()