# Development of Novel Quantum Algorithms
A submission to Womanium Quantum+AI 2024. This project leverages quantum computing to optimize financial portfolios using real-world data. Click [here](https://drive.google.com/file/d/1PGNUShboB4ik_JHZGcIPTh3KYi-aajzp/view?usp=sharing) for a comprehensive project description.

## Team Information:
Team Member 1: _(Nigel Kelly Phillips)_
- Email: nigelphillips@pursuit.org
- Discord ID: Nigel Phillips - USA
- GitHub ID: swooshcode
- Nationality: USA
- Current affiliation: AWS, NYU & Johns Hopkins University

Team Member 2: _(Kazim Mumtaz)_
- Email: kazimmumtaz43@gmail.com
- Discord ID:1129297221142196316
- GitHub ID: KazimMumtaz
- Nationality: Pakistani
- Current affiliation: Quaid-i-Azam School Gojra

Team Member 3: _(Tulsi Chaudhari)_
 - Email: Tchaudhari049@gmail.com
 - Discord ID: CrabbyPohtato
 - GitHub ID: Tatgithub02
 - Nationality: Indian
 - Current affiliation: QUCAN

# Quantum Portfolio Optimization

## Methodology
1. **Data Collection:** 
   - Historical data for S&P 500, EuroStoxx 50, Nikkei 225, FTSE 100, and Gold was fetched using the Yahoo Finance API.
   - The data range is from January 2019 to May 2024.

2. **Data Preprocessing:**
   - Filled missing values using forward fill.
   - Calculated daily returns.

3. **Model Creation:**
   - Created a Binary Quadratic Model (BQM) using mean returns and correlation matrix.

4. **Optimization:**
   - Used the D-Wave Leap Hybrid Sampler to solve the BQM and find the optimal portfolio.

## Results
- **Optimal Portfolio:** Selected assets corresponding to indices 2 (Nikkei 225).
- **Quantum Computation Time:** Approximately 3.54 seconds.

## Further Development: Scalability Testing

### Methodology
- Define a larger Binary Quadratic Model (BQM) for different problem sizes.
- Measure the quantum computation time for each problem size.

### Results
- Computation times for problem sizes: [10, 20, 30, 40, 50]
- Quantum Times: [3.99, 3.60, 3.47, 3.67, 3.73] seconds

# Reproducing the work

## Included folders
- `data/`: Cached CSVs that allow the pipeline to run without live API calls.
- `docs/`: Detailed methodological and analaysis documentation.
- `notebooks/`: Jupyter notebooks for interactive analysis.
- `presentation/`: Presentation summarizing the project.
- `src/`: Source code for data processing and optimization.

## Reproducibility steps
1. Ensure you are using Python 3.11.
2. Install requirements: `pip install -r requirements.txt`
2. Run the data fetching: `python src/fetch_data.py`
3. Run the create model: `python src/create_bqm.py`
4. Run the data preprocessing: `python src/preprocess_data.py`
5. Run the optimization: `python src/solve_bqm.py`
  * If you don't have access to the API, solve it locally instead: `python src/solve_local.py`
  * `solve_local.py` uses `dimod.ExactSolver` to verify BQM construction without a D-Wave Leap API credential. This is a reproducibility aid, not a substitute for the D-Wave Leap Hybrid Sampler.
6. Measure computation time: `python src/measure_time.py`
7. Run a local jupyter notebook server: `Jupyter notebook`
8. Open `notebooks/Novel Quantum Algorithm.ipynb` and click on: `Kernel > Restart & Run All Cells`

## Local data files

These files allow the workflow to be run without needing live API calls. There are two local data files:

- `historical_data.csv` — Adjusted close prices (S&P 500, STOXX50E, N225, FTSE, GLD),
  2019-01-01 to 2024-05-31
- `returns.csv` — Daily percentage returns derived from the above

If you want to regenerate the local data:

1. Install the necessary version of `yfinance`: `pip install yfinance==1.7.0`
2. Run the script to fetch data: `python src/fetch_data.py`

`fetch_data.py` downloads data from Yahoo Finance via the `yfinance` library. Two known issues
affected reproduction:

- **Yahoo tightened its bot protection in 2024–2025**, causing `yfinance` versions ≤ 0.2.50 to return `YFTzMissingError`. The fix uses `curl_cffi` as the HTTP    session with browser impersonation, and a newer `yfinance` version (1.7.0) for the download step only.

- **`Adj Close` was removed from yfinance ≥ 0.2.51.** The original code relies on that column. The workaround uses `auto_adjust=False` with yfinance 1.7.0 to    retrieve `Adj Close`, then reverts to yfinance 0.2.50 for the rest of the pipeline.

3. Install a newer version of yfinance to process the data: `pip install yfinance==0.2.50`
4. Run the data preprocessing script: `python src/preprocess_data.py`

## Authors
- Nigel K. Phillips

## Acknowledgements
I would like to acknowledge Edgardo Gerck, who pioneered the development of the technology behind quantum algorithms. His groundbreaking work, particularly his 1982 publication titled "Solution of the Schrödinger Equation for bound states in closed form" (Phys. Rev. A, 26, 662), set the foundation for advancements in this field. The techniques and insights presented in his paper were among the first to demonstrate significant progress in quantum mechanics and computing.

Gerck's contribution to proving the feasibility of quantum systems is an essential part of the ongoing development of fault-tolerant quantum computing, which has now been achieved by other researchers such as those at Google Quantum AI.

Reference: Phys. Rev. A, 26, 662 (1982) 
https://journals.aps.org/pra/abstract/10.1103/PhysRevA.26.662
