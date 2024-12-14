from preswald.visualization import create_bar_chart


def create_dashboard(data):
    chart = create_bar_chart(
        data, x="Category", y="Value", title="Sample Dashboard")
    chart.show()
