def bigmod(a, b, m):
    """
    Calculate (a^b) % m efficiently using modular exponentiation.

    This function uses the fast exponentiation method:
    - If b is even: (a^b) % m = ((a^(b/2) % m)^2) % m
    - If b is odd:  (a^b) % m = (a % m * (a^(b-1) % m)) % m

    Arguments:
    a -- base (integer)
    b -- exponent (non-negative integer)
    m -- modulus (integer, > 0)

    Returns:
    result of (a^b) % m

    Example:
    >>> bigmod(3, 13, 7)
    3
    """

    # Base case: anything power 0 is 1
    if b == 0:
        return 1

    # If exponent is even
    if b % 2 == 0:
        half = bigmod(a, b // 2, m)  # Recursively calculate a^(b/2) % m
        result = (half * half) % m    # Square it and take modulo
        return result
    else:
        # If exponent is odd
        result = (a % m * bigmod(a, b - 1, m)) % m
        return result


# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    base = 3
    exponent = 13
    modulus = 7
    result = bigmod(base, exponent, modulus)
    print(f"{base}^{exponent} % {modulus} = {result}")
