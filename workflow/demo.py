from preswald import Workflow
import pandas as pd

workflow = Workflow()

@workflow.atom()
def load_data():
    # This atom has no dependencies
    return pd.read_csv("data.csv")

@workflow.atom(dependencies=['load_data'])
def clean_data(load_data):
    # The output from load_data is automatically passed in
    return load_data.dropna()

@workflow.atom(dependencies=['clean_data'])
def analyze_data(clean_data):
    # Access the cleaned data from the previous atom
    return clean_data.describe()

results = workflow.execute()
print(results)
