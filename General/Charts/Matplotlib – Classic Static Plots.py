import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Sinuskurve", color="blue", linestyle="--")
plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")
plt.title("Matplotlib Beispiel")
plt.legend()
plt.grid(True)
plt.show()