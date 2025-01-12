from preswald import text, connect, view, slider, plotly, connections, Workflow
import pandas as pd
import plotly.express as px

# Create workflow
workflow = Workflow()

# Title
text("# Earthquake Analytics Dashboard 🌍")

# Load and connect data
connection_name = connect("data/earthquake_data.csv", "earthquake_connection")

# Slider for filtering magnitude
min_magnitude = slider("Minimum Magnitude", min_val=0.0,
                       max_val=10.0, default=5.0)


@workflow.atom()
def load_data():
    data = pd.DataFrame(connections[connection_name])
    data['Magnitude'] = pd.to_numeric(data['Magnitude'], errors='coerce')
    return data


@workflow.atom(dependencies=['load_data'])
def filter_data(load_data):
    return load_data[load_data['Magnitude'] >= min_magnitude.get('value', min_magnitude)]


@workflow.atom(dependencies=['filter_data'])
def create_map(filter_data):
    fig_map = px.scatter_geo(
        filter_data,
        lat='Latitude',
        lon='Longitude',
        color='Magnitude',
        size='Magnitude',
        hover_name='ID',
        title="Earthquake Map"
    )
    return fig_map


@workflow.atom(dependencies=['filter_data'])
def create_histogram(filter_data):
    fig_hist = px.histogram(
        filter_data,
        x="Magnitude",
        nbins=20,
        title="Distribution of Magnitudes"
    )
    return fig_hist


@workflow.atom(dependencies=['filter_data'])
def create_scatter(filter_data):
    fig_scatter = px.scatter(
        filter_data,
        x="Depth",
        y="Magnitude",
        color="Magnitude",
        title="Depth vs Magnitude",
        labels={"Depth": "Depth (km)", "Magnitude": "Magnitude"}
    )
    return fig_scatter


# Execute workflow
results = workflow.execute()

# Display visualizations
text("## Earthquake Locations")
plotly(results['create_map'].value)
plotly(results['create_histogram'].value)
plotly(results['create_scatter'].value)
