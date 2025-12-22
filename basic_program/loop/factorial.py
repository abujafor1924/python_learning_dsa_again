

"""
🧠 Thinking

n! = 1×2×3×…×n

বারবার গুণ → loop
Docstring for basic_program.loop.factorial
"""

n = int(input("Enter n: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)
