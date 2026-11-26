
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load dataset
df = px.data.iris()

# Create Dash application
app = Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Iris Flower Analysis Dashboard"),

    html.Label("Select Flower Species"),

    dcc.Dropdown(
        id="species-dropdown",
        options=[
            {"label": s, "value": s}
            for s in df["species"].unique()
        ],
        value="setosa",
        clearable=False
    ),

    dcc.Graph(id="iris-graph")
])

# Update graph when species changes
@app.callback(
    Output("iris-graph", "figure"),
    Input("species-dropdown", "value")
)
def update_graph(species):
    filtered_df = df[df["species"] == species]

    fig = px.scatter(
        filtered_df,
        x="sepal_length",
        y="petal_length",
        title=f"Iris Flower Analysis: {species}"
    )

    return fig

# Run application
if __name__ == "__main__":
    app.run(debug=True)
