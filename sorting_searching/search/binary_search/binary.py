def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
target = 23

index = binary_search_iterative(arr, target)
print(f"Element found at index: {index}" if index != -1 else "Element not found")



def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
   
   
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
target = 45
index = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Element found at index: {index}" if index != -1 else "Element not found")