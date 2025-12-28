"""
# Problem 5: Balls Without Replacement
# Bag contains 3 Red balls and 2 Blue balls.
# If we pick one ball:
#   - Red gives 1 point
#   - Blue gives 0 points
# Find the expected score.

# Step 1: Calculate probabilities
# Total balls = 3 + 2 = 5
prob_red = 3 / 5  # Probability of picking a Red ball
prob_blue = 2 / 5 # Probability of picking a Blue ball

# Step 2: Apply the definition of expected value
# E[X] = sum(score * probability for each outcome)
# Red: score 1 * probability 3/5
# Blue: score 0 * probability 2/5
expected_score = 1 * prob_red + 0 * prob_blue  # = 0.6

# Step 3: Output the expected score
print(expected_score)  # Output: 0.6

Docstring for number_theory.combinatorics.probability.expactations_balls_without_replacement
"""



p_red = 3/5
p_blue = 2/5

expected_score = 1*p_red + 0*p_blue
print(f"Expected Score: {expected_score}")
