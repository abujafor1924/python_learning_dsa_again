

"""
Problem:

2টা কয়েন ছুড়ে অন্তত 1টা Head আসার Probability?

CP Trick:

❌ Direct count করো না
✅ Complement ব্যবহার করো

No Head = TT

Probability = (1/2) × (1/2) = 1/4
Docstring for number_theory.combinatorics.probability.at_least_one_event
"""


p_no_head = (1/2) ** 2
ans = 1 - p_no_head
print(ans)
