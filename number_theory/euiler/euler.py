

"""
What is Euler’s Totient Function (φ(n))?

Euler’s Totient Function φ(n) counts the number of integers from 1 to n that are coprime with n.

Two numbers are coprime if their GCD = 1.

Example:

n = 9

Numbers from 1 to 9: 1, 2, 3, 4, 5, 6, 7, 8, 9

Coprime with 9: 1, 2, 4, 5, 7, 8 → total 6 numbers

So, φ(9) = 6
Docstring for number_theory.euiler.euler
"""

# ------------------------------
# Function to find GCD
# ------------------------------
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# ------------------------------
# Take input from user
# ------------------------------
n = int(input("Enter a number n: "))

# ------------------------------
# Count numbers coprime with n
# ------------------------------
count = 0
print(f"\nChecking numbers from 1 to {n} for coprime with {n}...")

for i in range(1, n + 1):
    g = gcd(i, n)
    print(f"GCD({i}, {n}) = {g}")
    if g == 1:
        print(f"{i} is coprime with {n}")
        count += 1

# ------------------------------
# Print Euler's Totient Function value
# ------------------------------
print(f"\nEuler's Totient Function φ({n}) = {count}")
