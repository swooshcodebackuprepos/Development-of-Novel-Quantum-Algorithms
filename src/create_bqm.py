import dimod
import pandas as pd

def create_real_world_bqm(returns):
    num_assets = returns.shape[1]
    mean_returns = returns.mean().values
    correlation_matrix = returns.corr().values

    bqm = dimod.BinaryQuadraticModel('BINARY')
    for i in range(num_assets):
        for j in range(i + 1, num_assets):
            bqm.add_interaction(i, j, correlation_matrix[i, j])
    for i in range(num_assets):
        bqm.add_variable(i, -mean_returns[i])  # Negative for maximization in a minimization framework

    return bqm

if __name__ == "__main__":
    returns = pd.read_csv('data/returns.csv', index_col='Date')
    bqm = create_real_world_bqm(returns)
