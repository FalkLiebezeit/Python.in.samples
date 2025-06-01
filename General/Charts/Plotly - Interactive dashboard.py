import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Beispiel-Daten erstellen
df = pd.DataFrame({
    'Fruit': ['Apple', 'Orange', 'Banana', 'Apple', 'Banana', 'Banana'],
    'Count': [4, 1, 2, 2, 1, 3],
    'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
})

# Dash App initialisieren
app = dash.Dash(__name__)
server = app.server  # Nützlich für Deployment

# App Layout
app.layout = html.Div([
    html.H1("Interaktives Dash-Chart"),
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in df["Fruit"].unique()],
        value=df["Fruit"].unique()[0],  # Standardwert auf erstes Element setzen
        clearable=False,
    ),
    dcc.Graph(id="bar-chart"),
])

# Callback für interaktive Diagrammaktualisierung
@app.callback(
    Output("bar-chart", "figure"),
    [Input("dropdown", "value")]
)
def update_bar_chart(fruit):
    mask = df["Fruit"] == fruit
    if mask.sum() == 0:
        return px.bar(title="Keine Daten verfügbar")
    
    fig = px.bar(df[mask], x="City", y="Count", color="City", barmode="group")
    fig.update_layout(title=f"Anzahl von {fruit} pro Stadt")
    return fig

# Server starten
if __name__ == "__main__":
    #app.run_server(debug=True)
    app.run