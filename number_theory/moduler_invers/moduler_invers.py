# Extended Euclidean Algorithm Theory:
# -----------------------------------
# The Extended Euclidean Algorithm finds integers x and y such that:
#     a*x + b*y = gcd(a, b)
# Where gcd(a, b) is the greatest common divisor of a and b.
# x and y are called coefficients of Bézout’s identity.
#
# Applications:
# - Finding modular inverses
# - Solving Diophantine equations
# - Cryptography (RSA, etc.)
#
# Example:
# a = 30, b = 20
# gcd(30, 20) = 10
# We want x and y such that 30*x + 20*y = 10
# Solution: x = 1, y = -1 → 30*1 + 20*(-1) = 10 ✅
#
# How the algorithm works:
# 1. Base case: if b == 0, gcd(a, 0) = a and coefficients are (1, 0)
# 2. Recursive case: call extended_gcd(b, a % b)
#    Then update x = y1, y = x1 - (a // b)*y1
#    This propagates the coefficients back up the recursion.



def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Returns (gcd, x, y) such that a*x + b*y = gcd
    """
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)


def mod_inverse(a, m):
    """
    Calculate modular inverse of a under modulo m
    using Extended Euclidean Algorithm.
    Returns x such that (a * x) % m = 1
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        print(f"No modular inverse exists for {a} modulo {m}")
        return None  # Inverse doesn't exist
    else:
        # Make sure x is positive
        return x % m


# ------------------------------
# Example
# ------------------------------
a = 3
m = 7
inv = mod_inverse(a, m)
print(f"Modular inverse of {a} modulo {m} is: {inv}")



# ---------------------------------------------
# Extended Euclidean Algorithm Example in Python
# ---------------------------------------------

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Returns a tuple (gcd, x, y) such that:
        a*x + b*y = gcd(a, b)
    """
    if b == 0:
        # Base case: gcd(a, 0) = a, coefficients x = 1, y = 0
        return (a, 1, 0)
    else:
        # Recursively call with (b, a % b)
        g, x1, y1 = extended_gcd(b, a % b)
        # Update x and y using results from recursion
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)


# ------------------------------
# Example Usage
# ------------------------------
a = 30
b = 20
gcd_value, x, y = extended_gcd(a, b)

print(f"GCD({a}, {b}) = {gcd_value}")
print(f"Coefficients: x = {x}, y = {y}")
print(f"Check: {a}*{x} + {b}*{y} = {a*x + b*y}")
