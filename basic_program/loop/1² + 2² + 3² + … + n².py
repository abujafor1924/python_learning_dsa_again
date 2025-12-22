

"""
🧠 Thinking

প্রতিটি সংখ্যার square নিতে হবে

একটার পর একটা → loop
Docstring for basic_program.loop.1² + 2² + 3² + … + n²
"""
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):     # 1 থেকে n
    total += i * i            # i² যোগ

print(total)
