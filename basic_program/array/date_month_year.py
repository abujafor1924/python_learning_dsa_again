s = input()  # 21/9/2013

day = ""
month = ""
year = ""

i = 0

# day
while s[i] != '/':
    day += s[i]
    i += 1

i += 1  # '/' skip

# month
while s[i] != '/':
    month += s[i]
    i += 1

i += 1  # '/' skip

# year
while i < len(s):
    year += s[i]
    i += 1

print(int(day))
print(int(month))
print(int(year))
