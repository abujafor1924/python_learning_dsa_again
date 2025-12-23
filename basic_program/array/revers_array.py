arr = [1, 2, 3, 4]

# দুইটা pointer ব্যবহার
l = 0
r = len(arr) - 1

while l < r:
    # swap
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1

print(arr)  # [4, 3, 2, 1]
