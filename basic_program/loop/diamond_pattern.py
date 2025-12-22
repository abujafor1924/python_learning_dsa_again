

"""
এটি তৈরি করতে মূলত loop ব্যবহার করতে হয়:

উপরের অংশের জন্য (triangle up)

মাঝের অংশের জন্য (longest row)

নিচের অংশের জন্য (triangle down)
Docstring for basic_program.loop.diamond_pattern
"""

# Diamond pattern program

n = 4  # Diamond এর row সংখ্যা (middle পর্যন্ত)

# Upper part of diamond
for i in range(1, n + 1):
    # Space print করা
    for j in range(n - i):
        print(" ", end="")
    # Star print করা
    for k in range(2 * i - 1):
        print("*", end="")
    print()  # New line

# Lower part of diamond
for i in range(n - 1, 0, -1):
    # Space print করা
    for j in range(n - i):
        print(" ", end="")
    # Star print করা
    for k in range(2 * i - 1):
        print("*", end="")
    print()  # New line









#=================== others patterns ===================
# Diamond pattern program (simple version)

n = int(input("Enter the number of rows for half diamond: "))  # User input

# Diamond তৈরি করা
for i in range(1, n*2):  # 1 থেকে 2*n-1 পর্যন্ত
    if i <= n:
        stars = 2*i - 1
        spaces = n - i
    else:
        stars = 2*(2*n - i) - 1
        spaces = i - n
    print(" " * spaces + "*" * stars)
