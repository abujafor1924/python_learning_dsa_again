



"""
মার্জ সর্ট একটি ডিভাইড এন্ড কনকোর অ্যালগরিদম। এটি অ্যারেকে ছোট ছোট অংশে ভাগ করে, প্রতিটি অংশ সর্ট করে, 
এবং তারপর সর্টেড অংশগুলিকে মার্জ করে সম্পূর্ণ সর্টেড অ্যারে তৈরি করে।

মূল ধারণা: ডিভাইড এন্ড কনকোর
ডিভাইড (ভাগ করো): অ্যারেকে দুই সমান (বা প্রায় সমান) ভাগে ভাগ করুন

কনকোর (জয় করো): প্রতিটি ভাগকে রিকার্সিভলি সর্ট করুন

মার্জ (একত্রিত করো): সর্টেড দুই ভাগকে একত্রিত করুন

কিভাবে কাজ করে?
text
1. যদি অ্যারের সাইজ 0 বা 1 হয় → ইতিমধ্যে সর্টেড
2. অ্যারেকে মিড পয়েন্টে দুই ভাগে ভাগ করুন
3. বাম অর্ধেককে রিকার্সিভলি সর্ট করুন
4. ডান অর্ধেককে রিকার্সিভলি সর্ট করুন
5. সর্টেড দুই অর্ধেক মার্জ করুন
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)




# ===================== Copy From AI =============================

def merge_sort_inplace(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        
        # দুই ভাগে সর্ট করি
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        
        # ইন-প্লেস মার্জ করি
        merge_inplace(arr, left, mid, right)

def merge_inplace(arr, left, mid, right):
    # টেম্পোরারি কপি তৈরি
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # মার্জ করি
    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1
    
    # বাকি এলিমেন্ট যোগ করি
    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1
    
    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1

# উদাহরণ
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_inplace(arr)
print("ইন-প্লেস সর্ট:", arr)


def merge_sort_iterative(arr):
    n = len(arr)
    current_size = 1
    
    while current_size < n:
        left = 0
        
        while left < n - 1:
            mid = min(left + current_size - 1, n - 1)
            right = min(left + 2 * current_size - 1, n - 1)
            
            # মার্জ করি
            merge_iterative(arr, left, mid, right)
            left += 2 * current_size
        
        current_size *= 2
    
    return arr

def merge_iterative(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    # টেম্প অ্যারে তৈরি
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # মার্জ করি
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # বাকি এলিমেন্ট
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# উদাহরণ
arr = [38, 27, 43, 3, 9, 82, 10]
print("ইটারেটিভ সর্ট:", merge_sort_iterative(arr.copy()))



def merge_sort_strings(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_strings(arr[:mid])
    right = merge_sort_strings(arr[mid:])
    
    return merge_strings(left, right)

def merge_strings(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i].lower() <= right[j].lower():  # কেস ইনসেনসিটিভ
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

words = ["banana", "Apple", "cherry", "date", "Blueberry"]
print("সর্টেড স্ট্রিংস:", merge_sort_strings(words))