"""
# Problem 3: At least one success
# Toss 3 coins. Each Head gives 1 point. 
# Find the expected (average) points.

# Step 1: Define the probability of Head for a fair coin
p_head = 0.5

# Step 2: Use linearity of expectation
# Expected value of total points = sum of expected points of each coin
# E[X] = E[coin1] + E[coin2] + E[coin3]
# Each coin has expected value: 1 * probability of Head + 0 * probability of Tail
# E[coin1] = 1 * 0.5 + 0 * 0.5 = 0.5
# E[coin2] = 0.5
# E[coin3] = 0.5

# Step 3: Add them up
expected_points = 0.5 + 0.5 + 0.5  # = 1.5

# So the expected (average) score when tossing 3 coins = 1.5
print(expected_points)  # Output: 1.5

Docstring for number_theory.combinatorics.probability.expactation_at_least_one_success
"""


n = 3
p_head = 0.5
point_per_head = 1

expected_points = n * p_head * point_per_head
print(f"Expected Points: {expected_points}")
