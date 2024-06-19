import pandas as pd

def load_sales_data(filepath):
    return pd.read_csv(filepath)

def process_sales_data(df):
    df['Variation'] = df['Revenue'].pct_change().fillna(0) * 100
    return df

if __name__ == "__main__":
    df = load_sales_data('monthly_sales_report/data/sales_data.csv')
    df = process_sales_data(df)
    print(df.head())
