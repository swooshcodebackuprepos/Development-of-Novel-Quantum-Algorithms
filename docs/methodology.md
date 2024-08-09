# Methodology

## Data Collection
- **Source**: Yahoo Finance API.
- **Assets**: S&P 500, EuroStoxx 50, Nikkei 225, FTSE 100, and Gold.
- **Period**: January 2019 to May 2024.
- **Fetching Data**: Used yfinance to download adjusted closing prices.

## Data Preprocessing
- **Handling Missing Values**: Applied forward fill to handle missing data.
- **Calculating Returns**: Computed daily returns from adjusted closing prices.

## Model Creation
- **Binary Quadratic Model (BQM)**: Formulated using mean returns and the correlation matrix.
  - **Variables**: Represent asset selection.
  - **Objective**: Maximize returns with constraints modeled by the correlation matrix.

## Quantum Optimization
- **Solver**: D-Wave Leap Hybrid Sampler.
- **Process**: Solved the BQM to determine the optimal portfolio.
