"""
Local verification solver for reproducibility.
Does NOT replace the D-Wave Leap Hybrid Sampler.
"""
import dimod
import pandas as pd
from create_bqm import create_real_world_bqm


def solve_locally(bqm):
    n = len(bqm.variables)
    if n > 20:
        raise ValueError(
            f"ExactSolver is only suitable for BQMs under 20 variables. "
            f"This BQM has {n}."
        )
    sampler = dimod.ExactSolver()
    return sampler.sample(bqm)


if __name__ == "__main__":
    returns = pd.read_csv('data/returns.csv', index_col='Date')
    bqm = create_real_world_bqm(returns)
    print(f"BQM built: {len(bqm.variables)} variables, {len(bqm.quadratic)} interactions")
    solution = solve_locally(bqm)
    print("Local verification solution:", solution.first.sample)
