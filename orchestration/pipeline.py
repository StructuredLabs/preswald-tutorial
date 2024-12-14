from ingestion.load_csv import ingest_data
from transformations.clean_data import clean_data


def run_pipeline():
    print("Starting pipeline...")
    data = ingest_data()
    cleaned_data = clean_data(data)
    print("Pipeline completed successfully!")
    return cleaned_data
