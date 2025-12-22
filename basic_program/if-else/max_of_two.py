def max_of_two(a, b):
    """
    দুইটি সংখ্যার মধ্যে বড় সংখ্যা রিটার্ন করে
    """

    if a > b:
        return a
    else:
        return b


# ---- main ----
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greater number:", max_of_two(a, b))
