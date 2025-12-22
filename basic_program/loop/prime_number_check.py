

"""
🧠 Thinking

1 ও নিজে ছাড়া আর কারো দিয়ে ভাগ যায়?

2 থেকে n-1 পর্যন্ত check

loop দরকার
Docstring for basic_program.loop.prime_number_check
"""

n = int(input("Enter number: "))

if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
