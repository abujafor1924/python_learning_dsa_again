def max_of_three(a, b, c):
    """
    তিনটি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা বের করে
    """

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# ---- main ----
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Greatest number:", max_of_three(a, b, c))
