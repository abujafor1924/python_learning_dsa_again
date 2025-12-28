"""  
Problem 1: Simple Dice Expected Value

Problem:
একটা 6-sided ডাইস repeated roll করছো।

প্রতিবার number এর মান score।

একবার roll করার expected score কত?

Solution:

Outcomes = {1,2,3,4,5,6}

Probability = 1/6

Formula:
"""

outcomes = [1,2,3,4,5,6]
prob = 1/6

expected_value = sum(x*prob for x in outcomes)
print(f"Expected Value: {expected_value:.6f}")
