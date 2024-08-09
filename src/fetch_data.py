import yfinance as yf
import pandas as pd

def fetch_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    data.ffill(inplace=True)
    return data

if __name__ == "__main__":
    tickers = ['^GSPC', '^STOXX50E', '^N225', '^FTSE', 'GLD']
    data = fetch_data(tickers, "2019-01-01", "2024-05-31")
    data.to_csv('data/historical_data.csv')
