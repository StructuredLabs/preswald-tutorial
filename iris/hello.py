from preswald import text, connect, view, slider, plotly, connections
import pandas as pd
import plotly.express as px

# Title
text("# Iris Datset 🌺")

# Load and connect data
connection_name = connect("iris.csv", "iris_connection")

# Slider for filtering petal length
# The slider allows filtering data by petal length
min_petal_length = slider("Minimum Petal Length", min_val=0.0,
                          max_val=7.0, default=2.0)

# Load the Iris dataset and filter based on petal length
data = pd.read_csv("iris.csv")
data['petal.length'] = pd.to_numeric(data['petal.length'], errors='coerce')

# Filter data based on the slider value
filtered_data = data[data['petal.length'] >=
                     min_petal_length.get('value', min_petal_length)]

# Summary of filtered data
text(f"### Total Records with Petal Length ≥ {
     min_petal_length.get('value', min_petal_length)}: {len(filtered_data)}")

# Petal vs Sepal Length scatter plot
text("## Petal vs Sepal Length Scatter Plot")
fig_scatter = px.scatter(
    filtered_data,
    x="petal.length",
    y="sepal.length",
    color="variety",
    title="Petal Length vs Sepal Length",
    labels={
        "petal.length": "Petal Length (cm)", "sepal.length": "Sepal Length (cm)"}
)
plotly(fig_scatter)

# Petal length distribution histogram
fig_hist = px.histogram(
    filtered_data,
    x="petal.length",
    nbins=20,
    title="Distribution of Petal Lengths",
    color="variety",
    labels={"petal.length": "Petal Length (cm)"}
)
plotly(fig_hist)

# Sepal Width vs Petal Length scatter plot
fig_scatter2 = px.scatter(
    filtered_data,
    x="petal.length",
    y="sepal.width",
    color="variety",
    title="Sepal Width vs Petal Length",
    labels={
        "petal.length": "Petal Length (cm)", "sepal.width": "Sepal Width (cm)"}
)
plotly(fig_scatter2)
