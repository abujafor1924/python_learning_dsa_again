def nth_palindrome(n):
    """
    এই function n-th palindrome number রিটার্ন করে
    """

    count = 0   # কয়টা palindrome পাওয়া গেছে
    num = 1     # সংখ্যা শুরু 1 থেকে

    while True:
        # সংখ্যাকে string বানিয়ে উল্টো করে চেক
        if str(num) == str(num)[::-1]:
            count += 1

            # যদি n-th palindrome পাওয়া যায়
            if count == n:
                return num

        num += 1


# ---- main ----
n = int(input("Enter n (n < 100): "))
print("Nth Palindrome:", nth_palindrome(n))
