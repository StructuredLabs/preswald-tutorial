from orchestration.pipeline import run_pipeline
from visualization.create_dashboard import create_dashboard

if __name__ == "__main__":
    print("Running Preswald Tutorial App...")
    data = run_pipeline()
    create_dashboard(data)
