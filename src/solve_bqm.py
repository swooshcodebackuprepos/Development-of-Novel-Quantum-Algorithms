from dwave.system import LeapHybridSampler
import pandas as pd
import dimod

def solve_with_dwave(bqm):
    sampler = LeapHybridSampler()
    solution = sampler.sample(bqm)
    return solution

if __name__ == "__main__":
    returns = pd.read_csv('data/returns.csv', index_col='Date')
    bqm = create_real_world_bqm(returns)
    solution = solve_with_dwave(bqm)
    print("Optimal Portfolio:", solution.first.sample)
