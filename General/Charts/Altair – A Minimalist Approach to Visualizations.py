import altair as alt
import pandas as pd

data = pd.DataFrame({
    "X": [1, 2, 3, 4, 5],
    "Y": [5, 10, 15, 10, 5]
})

chart = alt.Chart(data).mark_line(point=True).encode(
    x="X",
    y="Y"
).properties(title="Altair Liniendiagramm")

chart.show()