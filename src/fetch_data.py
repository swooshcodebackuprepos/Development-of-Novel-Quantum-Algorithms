import yfinance as yf
import pandas as pd
from curl_cffi import requests

def fetch_data(tickers, start, end):
    # Use a longer timeout and a specific browser impersonation
    session = requests.Session(impersonate="chrome110", timeout=15)
    
    data = yf.download(
        tickers, 
        start=start, 
        end=end, 
        session=session, 
        auto_adjust=False, 
        progress=False
    )['Adj Close']
    
    data.ffill(inplace=True)
    return data

if __name__ == "__main__":
    tickers = ['^GSPC', '^STOXX50E', '^N225', '^FTSE', 'GLD']
    data = fetch_data(tickers, "2019-01-01", "2024-05-31")
    data.to_csv('data/historical_data.csv')
    print("CSV generated successfully")
