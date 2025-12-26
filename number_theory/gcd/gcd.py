# ------------------------------
# Step 1: Take two numbers from user
# ------------------------------
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"\nFinding GCD of {a} and {b}...")

# ------------------------------
# Step 2: Euclidean Algorithm
# ------------------------------
x, y = a, b  # Save original numbers for printing later

while b != 0:
    print(f"\nCurrent numbers: a = {a}, b = {b}")
    remainder = a % b
    print(f"Step: a % b = {a} % {b} = {remainder}")
    a = b
    b = remainder

# ------------------------------
# Step 3: Print the result
# ------------------------------
print(f"\nGCD of {x} and {y} is: {a}")
