import pandas as pd

def summarize_csv(input_path: str):
    df = pd.read_csv(input_path)

    print("Basic Info")
    print(df.info())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nStatistics")
    print(df.describe())


if __name__ == "__main__":
    summarize_csv("examples/sample.csv")