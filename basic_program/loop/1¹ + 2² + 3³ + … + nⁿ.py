

"""
🧠 Thinking

সংখ্যা বাড়ছে

power-ও বাড়ছে

প্রতিটি term আলাদা → loop ছাড়া অসম্ভব
Docstring for basic_program.loop.1¹ + 2² + 3³ + … + nⁿ
"""

n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total += i ** i           # i এর power i

print(total)
