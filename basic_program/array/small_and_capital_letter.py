s = input()

small = 0
capital = 0

for ch in s:
    if 'a' <= ch <= 'z':
        small += 1
    elif 'A' <= ch <= 'Z':
        capital += 1

print(small)
print(capital)
