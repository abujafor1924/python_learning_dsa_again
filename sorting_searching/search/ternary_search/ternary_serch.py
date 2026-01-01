

def ternary_search_iterative(arr, target):
    """
    ইটারেটিভ টার্নারি সার্চ ইমপ্লিমেন্টেশন।
    
    আর্গুমেন্ট:
        arr: সর্টেড লিস্ট
        target: খোঁজার উপাদান
        
    রিটার্ন:
        টার্গেট পাওয়া গেলে ইনডেক্স, নাহলে -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # দুটি মিডপয়েন্ট ক্যালকুলেশন
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # টার্গেট মিডপয়েন্টে আছে কিনা চেক
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        # টার্গেট কোন পার্টিশনে আছে তা নির্ধারণ
        if target < arr[mid1]:
            # টার্গেট প্রথম পার্টিশনে
            right = mid1 - 1
        elif target > arr[mid2]:
            # টার্গেট তৃতীয় পার্টিশনে
            left = mid2 + 1
        else:
            # টার্গেট মধ্যবর্তী পার্টিশনে
            left = mid1 + 1
            right = mid2 - 1
    
    return -1  # টার্গেট পাওয়া যায়নি

arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target=7
print(ternary_search_iterative(arr, target))  # আউটপুট:

def ternary_search_recursive(arr, target, left, right):
    """
    রিকার্সিভ টার্নারি সার্চ ইমপ্লিমেন্টেশন।
    
    আর্গুমেন্ট:
        arr: সর্টেড লিস্ট
        target: খোঁজার উপাদান
        left: সার্চের বাম সীমা
        right: সার্চের ডান সীমা
        
    রিটার্ন:
        টার্গেট পাওয়া গেলে ইনডেক্স, নাহলে -1
    """
    if left > right:
        return -1  # টার্গেট পাওয়া যায়নি
    
    # দুটি মিডপয়েন্ট ক্যালকুলেশন
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    
    # টার্গেট মিডপয়েন্টে আছে কিনা চেক
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    
    # টার্গেট কোন পার্টিশনে আছে তা নির্ধারণ এবং রিকার্সিভ কল
    if target < arr[mid1]:
        return ternary_search_recursive(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search_recursive(arr, target, mid2 + 1, right)
    else:
        return ternary_search_recursive(arr, target, mid1 + 1, mid2 - 1)
   
arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target=7
print(ternary_search_recursive(arr, target, 0, len(arr) - 1))  # আউটপুট: 6 6