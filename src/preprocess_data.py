import pandas as pd

def preprocess_data(file_path):
    data = pd.read_csv(file_path, index_col='Date')
    returns = data.pct_change().dropna()
    return returns

if __name__ == "__main__":
    returns = preprocess_data('data/historical_data.csv')
    returns.to_csv('data/returns.csv')
