import plotly.express as px
import pandas as pd

# Beispiel-Daten erzeugen
data = pd.DataFrame({
    "X-Werte": [1, 2, 3, 4, 5],
    "Y-Werte": [10, 20, 15, 30, 25]
})

fig = px.line(data, x="X-Werte", y="Y-Werte", title="Plotly Interaktives Liniendiagramm", markers=True)
fig.show()