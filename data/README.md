# Data Files

## Files
- `historical_data.csv` — Adjusted close prices (S&P 500, STOXX50E, N225, FTSE, GLD),
  2019-01-01 to 2024-05-31
- `returns.csv` — Daily percentage returns derived from the above

## Important: yfinance API Change

`fetch_data.py` originally relied on `yfinance` returning an `Adj Close` column.
That column was removed in `yfinance==0.2.51`. The pinned environment uses
`yfinance==0.2.50`, which still returns `Adj Close`.

## Note on the Local Verification Solver

`solve_local.py` uses `dimod.ExactSolver` to verify BQM construction without a
D-Wave Leap API credential. This is a reproducibility aid, not a substitute
for the D-Wave Leap Hybrid Sampler.
