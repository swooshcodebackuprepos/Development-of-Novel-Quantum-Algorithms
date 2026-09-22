# Data Files

## Files
- `historical_data.csv` — Adjusted close prices (S&P 500, STOXX50E, N225, FTSE, GLD),
  2019-01-01 to 2024-05-31
- `returns.csv` — Daily percentage returns derived from the above

## How the CSVs Were Generated

`fetch_data.py` downloads data from Yahoo Finance via `yfinance`. Two known issues
affected reproduction:

1. **Yahoo tightened its bot protection in 2024–2025**, causing `yfinance` versions
   ≤ 0.2.50 to return `YFTzMissingError`. The fix uses `curl_cffi` as the HTTP
   session with browser impersonation, and a newer `yfinance` version (1.7.0)
   for the download step only.

2. **`Adj Close` was removed from yfinance ≥ 0.2.51.** The original code relies on
   that column. The workaround uses `auto_adjust=False` with yfinance 1.7.0 to
   retrieve `Adj Close`, then reverts to yfinance 0.2.50 for the rest of the
   pipeline.

## Reproducing the Data

The cached CSVs in this directory allow the rest of the pipeline to run without
live API calls. If regenerating:

    pip install yfinance==1.7.0 curl_cffi
    python src/fetch_data.py
    pip install yfinance==0.2.50
    python src/preprocess_data.py

## Note on the Local Verification Solver

`solve_local.py` uses `dimod.ExactSolver` to verify BQM construction without a
D-Wave Leap API credential. This is a reproducibility aid, not a substitute
for the D-Wave Leap Hybrid Sampler.
