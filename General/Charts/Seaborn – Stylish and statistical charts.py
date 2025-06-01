import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Beispiel-Daten erstellen
data = pd.DataFrame({
    "Kategorie": ["A", "B", "C", "D"],
    "Werte": [10, 15, 7, 12]
})

# Seaborn-Stil verwenden
sns.set_theme(style="whitegrid")
sns.barplot(x="Kategorie", y="Werte", data=data, palette="coolwarm")

plt.title("Seaborn Balkendiagramm")
plt.show()