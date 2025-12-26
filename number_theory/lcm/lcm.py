# ------------------------------
# Step 1: Take two numbers from user
# ------------------------------
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"\nFinding LCM of {a} and {b}...")

# ------------------------------
# Step 2: Calculate GCD using Euclidean Algorithm
# ------------------------------
x, y = a, b  # Save original numbers
a_copy, b_copy = a, b

while b_copy != 0:
    print(f"Current numbers: a = {a_copy}, b = {b_copy}")
    remainder = a_copy % b_copy
    print(f"a % b = {a_copy} % {b_copy} = {remainder}")
    a_copy = b_copy
    b_copy = remainder

gcd = a_copy
print(f"\nGCD of {x} and {y} is: {gcd}")

# ------------------------------
# Step 3: Calculate LCM using formula
# ------------------------------
lcm = (x * y) // gcd
print(f"LCM of {x} and {y} is: {lcm}")
