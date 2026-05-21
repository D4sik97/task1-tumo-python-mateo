import numpy as np
from scipy import stats
import matplotlib as plt
import random

# task 1
# n = 10  
# p = 1 / 2
# # TODO: Create an array of all possible outcomes (0 through n sixes)
# k_values = np.arange(0, n + 1)
# print(k_values)
# # TODO: Calculate the PMF (probability mass function) at each k using scipy
# # Hint: stats.binom.pmf(k, n, p)
# pmf_values = stats.binom.pmf(k_values, n, p)


# # Print a summary table
# print(f"{'Sixes (k)':<12} {'P(X=k)':<12}")
# print("-" * 24)
# for k, prob in zip(k_values, pmf_values):
#     print(f"{k:<12} {prob:<12.7f}")

# print(f"Sum of PMF values: {np.sum(pmf_values):.4f}")



# task 2

LOOT_TABLE = [
    {"name": "Common Herb",     "probability": 0.55, "gold_value": 5},
    {"name": "Rare Gem",        "probability": 0.25, "gold_value": 20},
    {"name": "Epic Sword",      "probability": 0.15, "gold_value": 60},
    {"name": "Legendary Armor", "probability": 0.05, "gold_value": 200},
]

total = sum(item["probability"] for item in LOOT_TABLE)
print(f"Probabilities sum to: {total}")


def single_loot_drop(loot_table):

    roll = random.random()
    cumulative = 0.0

    for item in loot_table:

        cumulative += item["probability"]

        if roll < cumulative:
            return item

    return loot_table[-1]
    
def run_simulation(loot_table, num_trials=10_000):

    results = []
    gold_earned = []

    for _ in range(num_trials):

        drop = single_loot_drop(loot_table)

        results.append(drop["name"])

        gold_earned.append(drop["gold_value"])

    return results, gold_earned
    
def theoretical_expected_value(loot_table):

    ev = 0

    for item in loot_table:

        ev += (
            item["probability"]
            * item["gold_value"]
        )

    return ev

def print_statistics(loot_table, results, gold_earned):

    num_trials = len(results)

    print("=" * 55)
    print(f"  LOOT DROP SIMULATION — {num_trials:,} Trials")
    print("=" * 55)

    print(f"\n{'Item':<20} {'Target %':>10} {'Actual %':>10} {'Diff':>8}")

    print("-" * 52)

    for item in loot_table:

        name       = item["name"]

        target_pct = item["probability"] * 100

        count = results.count(name)

        actual_pct = (count / num_trials) * 100

        diff = actual_pct - target_pct

        print(
            f"{name:<20} "
            f"{target_pct:>9.1f}% "
            f"{actual_pct:>9.1f}% "
            f"{diff:>+7.2f}%"
        )

    theo_ev = theoretical_expected_value(loot_table)

    sim_ev = np.mean(gold_earned)

    print("\n" + "-" * 52)

    print(f"  Theoretical EV: {theo_ev:.2f} gold")

    print(f"  Simulated   EV: {sim_ev:.2f} gold")

    print("=" * 55)




def plot_results(loot_table, results, gold_earned):

    item_names = [item["name"] for item in loot_table]

    target_rates = [
        item["probability"] * 100
        for item in loot_table
    ]

    simulated_rates = [
        (results.count(name) / len(results)) * 100
        for name in item_names
    ]

    running_avg = np.cumsum(gold_earned) / np.arange(1, len(gold_earned) + 1)

    theoretical_ev = theoretical_expected_value(loot_table)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # LEFT GRAPH
    axes[0].bar(item_names, target_rates, alpha=0.6, label="Target")
    axes[0].bar(item_names, simulated_rates, alpha=0.6, label="Simulated")

    axes[0].set_ylabel("Drop Rate (%)")
    axes[0].set_title("Target vs Simulated Drop Rates")
    axes[0].legend()

    # RIGHT GRAPH
    axes[1].plot(running_avg, label="Running Average Gold")

    axes[1].axhline(
        theoretical_ev,
        linestyle="--",
        label="Theoretical EV"
    )

    axes[1].set_xlabel("Number of Trials")
    axes[1].set_ylabel("Average Gold")
    axes[1].set_title("Law of Large Numbers")
    axes[1].legend()

    plt.tight_layout()
    plt.show()