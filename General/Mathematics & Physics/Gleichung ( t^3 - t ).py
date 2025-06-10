import matplotlib.pyplot as plt
import numpy as np

# Bereich für t definieren
t_values = np.linspace(-10, 10, 500)  # Werte von -10 bis 10

# Funktionen berechnen
y_values = t_values**3 - t_values

# Plot erstellen
plt.figure(figsize=(8, 6))
plt.plot(t_values, y_values, label=r'$t^3 - t$', color='blue')
plt.axhline(0, color='red', linestyle='--', label='y = 0')

# Labels und Legende
plt.title("Visualisierung der Funktion $t^3 - t$")
plt.xlabel("$t$")
plt.ylabel("$y$")
plt.legend()
plt.grid()
plt.show()