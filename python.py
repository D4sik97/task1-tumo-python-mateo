import numpy as np
from scipy import stats
import matplotlib as plt

n = 10  
p = 1 / 2
# TODO: Create an array of all possible outcomes (0 through n sixes)
k_values = np.arange(0, n + 1)
print(k_values)
# TODO: Calculate the PMF (probability mass function) at each k using scipy
# Hint: stats.binom.pmf(k, n, p)
pmf_values = stats.binom.pmf(k_values, n, p)


# Print a summary table
print(f"{'Sixes (k)':<12} {'P(X=k)':<12}")
print("-" * 24)
for k, prob in zip(k_values, pmf_values):
    print(f"{k:<12} {prob:<12.7f}")

print(f"Sum of PMF values: {np.sum(pmf_values):.4f}")