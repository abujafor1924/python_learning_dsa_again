n = int(input("Enter rows: "))
for i in range(1, 2*n):
    if i <= n:
        stars = i
    else:
        stars = 2*n - i
    print(" "*(n-stars), end="")
    for j in range(1, stars+1):
        print(j, end="")
    for j in range(stars-1, 0, -1):
        print(j, end="")
    print()
