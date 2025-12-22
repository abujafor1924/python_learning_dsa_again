def sort_three_numbers(a, b, c):
    """
    তিনটি সংখ্যা ছোট থেকে বড় ক্রমে সাজিয়ে রিটার্ন করে
    """

    numbers = [a, b, c]  # list এ রাখা
    numbers.sort()      # ছোট থেকে বড় sort

    return numbers


# ---- main ----
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Sorted order:", sort_three_numbers(a, b, c))
