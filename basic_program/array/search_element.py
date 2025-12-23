arr = [5, 8, 12, 20]
target = 12

found = False

# array ঘুরে দেখা
for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not Found")
