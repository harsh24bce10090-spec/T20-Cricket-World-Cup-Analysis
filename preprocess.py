import pandas as pd

def clean_data():
    df = pd.read_csv("data/t20.csv")

    df.dropna(inplace=True)

    df.to_csv("data/cleaned.csv", index=False)

    print("Data Cleaned")
