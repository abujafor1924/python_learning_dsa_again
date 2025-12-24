def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    
    # Recursive Case
    return n * factorial(n - 1)

# টেস্ট
print(factorial(5))  # Output: 120
print(factorial(4))  # Output: 24