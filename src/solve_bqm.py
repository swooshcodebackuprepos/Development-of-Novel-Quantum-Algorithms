from dwave.system import LeapHybridSampler
import pandas as pd
import dimod

from create_bqm import create_real_world_bqm
from solve_local import solve_locally


def solve_with_dwave(bqm):
    """Requires an active D-Wave Leap API credential."""
    sampler = LeapHybridSampler()
    solution = sampler.sample(bqm)
    return solution


if __name__ == "__main__":
    returns = pd.read_csv('data/returns.csv', index_col='Date')
    bqm = create_real_world_bqm(returns)

    print(f"BQM built: {len(bqm.variables)} variables, "
          f"{len(bqm.quadratic)} interactions")

    try:
        solution = solve_with_dwave(bqm)
        print("D-Wave solution:", solution.first.sample)
    except Exception as e:
        print(f"D-Wave unavailable ({e}).")
        print("Running local verification only.")
        solution = solve_locally(bqm)
        print("Local verification solution:", solution.first.sample)
