from preswald.ingestion import load_csv


def ingest_data():
    data = load_csv("ingestion/sample_data.csv")
    print("Data loaded successfully:")
    print(data.head())
    return data
