# Development-of-Novel-Quantum-Algorithms
Womanium Quantum+AI 2024 Projects

_**Do NOT delete/ edit the format of this read.me file.**_

_**Include all necessary information only as per the given format.**_

## Project Information:

### Team Size:
  - Maximum team size = 3
  - While individual participation is also welcome, we highly recommend team participation :)

### Eligibility:
  - All nationalities, genders, and age groups are welcome to participate in the projects.
  - All team participants must be enrolled in Womanium Quantum+AI 2024.
  - Everyone is eligible to participate in this project and win Womanium grants.
  - Everyone is eligible for Womanium QSL fellowships with Classiq.
  - All successful project submissions earn the Womanium Project Certificate.

### Project Description:
  - Click [here](https://drive.google.com/file/d/1PGNUShboB4ik_JHZGcIPTh3KYi-aajzp/view?usp=sharing) to view the project description.

## Project Submission:
All information in this section will be considered for project submission and judging.

Ensure your repository is public and submitted by **August 9, 2024, 23:59pm US ET**.

Ensure your repository does not contain any personal or team tokens/access information to access backends. Ensure your repository does not contain any third-party intellectual property (logos, company names, copied literature, or code). Any resources used must be open source or appropriately referenced.

### Team Information:
Team Member 1: _(Nigel Kelly Phillips)_
- Email: nigelphillips@pursuit.org
- Discord ID: Nigel Phillips - USA
- GitHub ID: swooshcode
- Nationality: USA
- Current affiliation: Pursuit, SNHU

Team Member 2: _(Kazim Mumtaz)_
- Email: kazimmumtaz43@gmail.com
- Discord ID:1129297221142196316
- GitHub ID: KazimMumtaz
- Nationality: Pakistani
- Current affiliation: N/A


Team Member 3: _(Tulsi Chaudhari)_
 - Email: Tchaudhari049@gmail.com
 - Discord ID: CrabbyPohtato
 - GitHub ID: Tatgithub02
 - Nationality: Indian
 - Current affiliation: N/A

### Project Solution:
_Include a comprehensive summary of all important information about your project solution here._
All necessary code files and any additional information required to judge your project solution should be included in the repository. 

### Project Presentation Deck:
_Link a 5min. presentation recording or deck here._

# Quantum Portfolio Optimization

## Overview
This project leverages quantum computing to optimize financial portfolios using real-world data.

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

## Files
- `src/`: Source code for data processing and optimization.
- `notebooks/`: Jupyter notebooks for interactive analysis.
- `docs/`: Detailed documentation.
- `presentation/`: Presentation summarizing the project.

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Run the data fetching: `python src/fetch_data.py`
3. Run the data preprocessing: `python src/preprocess_data.py`
4. Run the optimization: `python src/solve_bqm.py`
5. Measure computation time: `python src/measure_time.py`

## Authors
- Nigel K. Phillips

## Acknowledgements
I would like to acknowledge Edgardo Gerck, who pioneered the development of the technology behind quantum algorithms. His groundbreaking work, particularly his 1982 publication titled "Solution of the Schrödinger Equation for bound states in closed form" (Phys. Rev. A, 26, 662), set the foundation for advancements in this field. The techniques and insights presented in his paper were among the first to demonstrate significant progress in quantum mechanics and computing.

Gerck's contribution to proving the feasibility of quantum systems is an essential part of the ongoing development of fault-tolerant quantum computing, which has now been achieved by other researchers such as those at Google Quantum AI.

Reference: Phys. Rev. A, 26, 662 (1982) 
https://journals.aps.org/pra/abstract/10.1103/PhysRevA.26.662
