arr = [3, 7, 2, 9, 5]

# প্রথম element কে max ধরা
max_val = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]

print("Maximum:", max_val)
