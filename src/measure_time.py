from dwave.system import LeapHybridSampler
import pandas as pd
import time
import dimod

def measure_quantum_time(bqm):
    start_time = time.time()
    sampler = LeapHybridSampler()
    solution = sampler.sample(bqm)
    return time.time() - start_time, solution

if __name__ == "__main__":
    returns = pd.read_csv('data/returns.csv', index_col='Date')
    bqm = create_real_world_bqm(returns)
    q_time_real_world, solution_real_world = measure_quantum_time(bqm)
    print("Quantum Time with Real-World Data:", q_time_real_world)
    print("Solution with Real-World Data:", solution_real_world.first.sample)
