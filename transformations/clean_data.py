import pandas as pd


def clean_data(data):
    cleaned_data = data.dropna()  # Remove null values
    print("Cleaned data:")
    print(cleaned_data)
    return cleaned_data
