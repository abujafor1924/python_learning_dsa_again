

"""
Ah! You want bigmod functions, i.e., modular exponentiation which calculates:

(
𝑎
𝑏
)
m
o
d
 
 
𝑚
(a
b
)modm

efficiently, even for very large numbers. Let me explain clearly with Python and step-by-step prints.

1️⃣ Why BigMod?

When a and b are huge, directly calculating 
𝑎
𝑏
a
b
 will overflow.
Instead, we use modular exponentiation:

(
𝑎
𝑏
)
m
o
d
 
 
𝑚
=
(
(
𝑎
𝑏
/
2
m
o
d
 
 
𝑚
)
2
m
o
d
 
 
𝑚
)
(if b is even)
(a
b
)modm=((a
b/2
modm)
2
modm)(if b is even)
(
𝑎
𝑏
)
m
o
d
 
 
𝑚
=
(
𝑎
m
o
d
 
 
𝑚
⋅
𝑎
𝑏
−
1
m
o
d
 
 
𝑚
)
(if b is odd)
(a
b
)modm=(amodm⋅a
b−1
modm)(if b is odd)

This is also called fast exponentiation modulo m.
Docstring for number_theory.bigmod.bigmod
"""



def bigmod(a, b, m):
    print(f"Calculating {a}^{b} % {m}")
    if b == 0:
        print("b = 0, return 1")
        return 1
    elif b % 2 == 0:
        print(f"b = {b} is even, split problem: ({a}^{b//2})^2")
        half = bigmod(a, b // 2, m)
        result = (half * half) % m
        print(f"({a}^{b//2})^2 % {m} = {result}")
        return result
    else:
        print(f"b = {b} is odd, multiply by a: {a} * {a}^{b-1}")
        result = (a % m * bigmod(a, b - 1, m)) % m
        print(f"{a} * {a}^{b-1} % {m} = {result}")
        return result

# ------------------------------
# Input numbers
# ------------------------------
a = int(input("Enter base a: "))
b = int(input("Enter exponent b: "))
m = int(input("Enter modulus m: "))

# ------------------------------
# Compute bigmod
# ------------------------------
res = bigmod(a, b, m)
print(f"\n{a}^{b} % {m} = {res}")
