def calculate_sum(n):
    """
    এই function নিচের যোগফল হিসাব করে:
    Σ i * (n - i + 1)
    """

    total = 0  # যোগফল রাখার জন্য

    for i in range(1, n + 1):
        # সূত্র অনুযায়ী যোগ করা
        total += i * (n - i + 1)

    return total


# ---- main ----
n = int(input("Enter n: "))
print("Result:", calculate_sum(n))
