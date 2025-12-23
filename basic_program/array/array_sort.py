# array input
arr = list(map(int, input().split()))

n = len(arr)

# selection sort
for i in range(n):
    min_index = i  # ধরি i-ই smallest

    for j in range(i + 1, n):
        # যদি এর থেকে ছোট পাই
        if arr[j] < arr[min_index]:
            min_index = j

    # swap
    arr[i], arr[min_index] = arr[min_index], arr[i]

# output
print(arr)
