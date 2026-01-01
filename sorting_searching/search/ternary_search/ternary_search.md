# টার্নারি সার্চ বিস্তারিত বাংলায়

টার্নারি সার্চ হল বাইনারি সার্চের একটি এক্সটেনশন যা সার্চ স্পেসকে **তিন ভাগে** বিভক্ত করে। এটি একটি ডিভাইড এন্ড কনকয়ার অ্যালগরিদম।

## মূল বৈশিষ্ট্য
- **টাইম কমপ্লেক্সিটি**: O(log₃ n) ≈ O(log n) (বাইনারি সার্চের চেয়ে কিছুটা বেশি কন্সট্যান্ট)
- **প্রয়োজনীয়তা**: লিস্ট অবশ্যই সর্টেড (মোনোটনিক) থাকতে হবে
- **পদ্ধতি**: সার্চ স্পেসকে তিন সমান ভাগে বিভক্ত করা

## বাইনারি সার্চ vs টার্নারি সার্চ
| বিষয় | বাইনারি সার্চ | টার্নারি সার্চ |
|------|---------------|----------------|
| বিভাজন | ২ ভাগে | ৩ ভাগে |
| তুলনা প্রতি ধাপে | ১ বার | ২ বার |
| টাইম কমপ্লেক্সিটি | O(log₂ n) | O(log₃ n) |
| ব্যবহার | সাধারণ সর্টেড অ্যারে | ইউনিমোডাল ফাংশনের জন্য ভাল |

## অ্যালগরিদমের ধাপ
১. সার্চ স্পেসের দুটি মিডপয়েন্ট খুঁজুন
২. অ্যারে/লিস্টকে তিন ভাগে বিভক্ত করুন
৩. টার্গেটের সাথে দুটি মিডপয়েন্ট তুলনা করুন
৪. নির্ধারণ করুন টার্গেট কোন পার্টিশনে আছে
৫. সেই পার্টিশনে সার্চ চালিয়ে যান

## পাইথন ইমপ্লিমেন্টেশন

### ১. ইটারেটিভ টার্নারি সার্চ
```python
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
```

### ২. রিকার্সিভ টার্নারি সার্চ
```python
def ternary_search_recursive(arr, target, left, right):
    """
    রিকার্সিভ টার্নারি সার্চ ইমপ্লিমেন্টেশন।
    
    আর্গুমেন্ট:
        arr: সর্টেড লিস্ট
        target: খোঁজার উপাদান
        left: বর্তমান বাম সীমা
        right: বর্তমান ডান সীমা
        
    রিটার্ন:
        টার্গেট পাওয়া গেলে ইনডেক্স, নাহলে -1
    """
    if left > right:
        return -1  # বেস কেস
    
    # দুটি মিডপয়েন্ট ক্যালকুলেশন
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    
    # টার্গেট মিডপয়েন্টে আছে কিনা চেক
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    
    # টার্গেট কোন পার্টিশনে আছে রিকার্সিভলি সার্চ
    if target < arr[mid1]:
        # প্রথম পার্টিশনে
        return ternary_search_recursive(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        # তৃতীয় পার্টিশনে
        return ternary_search_recursive(arr, target, mid2 + 1, right)
    else:
        # দ্বিতীয় পার্টিশনে
        return ternary_search_recursive(arr, target, mid1 + 1, mid2 - 1)

# সহজে ব্যবহারের জন্য র্যাপার ফাংশন
def ternary_search(arr, target):
    return ternary_search_recursive(arr, target, 0, len(arr) - 1)
```

### ৩. কনটিনিউয়াস টার্নারি সার্চ (ফাংশন মিনিমাইজেশনের জন্য)
```python
def ternary_search_continuous(func, left, right, precision=1e-9, max_iter=100):
    """
    কনটিনিউয়াস টার্নারি সার্চ (ইউনিমোডাল ফাংশনের মিনিমাম/ম্যাক্সিমাম খোঁজার জন্য)।
    
    আর্গুমেন্ট:
        func: ইউনিমোডাল ফাংশন
        left: ইন্টারভালের শুরু
        right: ইন্টারভালের শেষ
        precision: নির্ভুলতা
        max_iter: সর্বোচ্চ ইটারেশন
        
    রিটার্ন:
        মিনিমাম/ম্যাক্সিমাম পয়েন্ট
    """
    for _ in range(max_iter):
        if abs(right - left) < precision:
            break
            
        # দুটি মিডপয়েন্ট
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        
        # ফাংশনের মান তুলনা
        f_mid1 = func(mid1)
        f_mid2 = func(mid2)
        
        # মিনিমাম খুঁজতে (ম্যাক্সিমাম খুঁজতে বিপরীত করতে হবে)
        if f_mid1 < f_mid2:
            right = mid2
        else:
            left = mid1
    
    return (left + right) / 2
```

## ব্যবহারের উদাহরণ
```python
# সর্টেড লিস্ট তৈরি
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
target = 15

print("ডেটা:", numbers)
print("টার্গেট:", target)
print()

# ইটারেটিভ টার্নারি সার্চ
result_iter = ternary_search_iterative(numbers, target)
print(f"ইটারেটিভ টার্নারি সার্চ: ইনডেক্স {result_iter}")

# রিকার্সিভ টার্নারি সার্চ
result_rec = ternary_search(numbers, target)
print(f"রিকার্সিভ টার্নারি সার্চ: ইনডেক্স {result_rec}")

# বাইনারি সার্চের সাথে তুলনা
def binary_search(arr, target):
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

binary_result = binary_search(numbers, target)
print(f"বাইনারি সার্চ: ইনডেক্স {binary_result}")
```

## ভিজ্যুয়ালাইজেশন উদাহরণ
```
ডেটা: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91, 104]
টার্গেট: 38

প্রথম ধাপ:
লিস্ট: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91, 104]
left=0, right=11
mid1 = 0 + (11-0)//3 = 3 (value=12)
mid2 = 11 - (11-0)//3 = 7 (value=45)

38 > 12 এবং 38 < 45
তাই মধ্যবর্তী পার্টিশনে: [16, 23, 38, 45, 56]

দ্বিতীয় ধাপ:
লিস্ট: [16, 23, 38, 45, 56]
left=4, right=8
mid1 = 4 + (8-4)//3 = 5 (value=23)
mid2 = 8 - (8-4)//3 = 7 (value=45)

38 > 23 এবং 38 < 45
তাই মধ্যবর্তী পার্টিশনে: [38, 45]

তৃতীয় ধাপ:
লিস্ট: [38, 45]
left=6, right=7
mid1 = 6 + (7-6)//3 = 6 (value=38) ← পাওয়া গেছে!
```

## রিয়েল-লাইফ অ্যাপ্লিকেশন

### ১. ফাংশন অপটিমাইজেশন
```python
# প্যারাবোলার মিনিমাম খোঁজা
def quadratic_function(x):
    return (x - 5)**2 + 3

# টার্নারি সার্চ দিয়ে মিনিমাম খোঁজা
min_point = ternary_search_continuous(quadratic_function, 0, 10, precision=1e-7)
print(f"ফাংশনের মিনিমাম x = {min_point:.5f}")
print(f"মিনিমাম ভ্যালু = {quadratic_function(min_point):.5f}")
```

### ২. ত্রিমাত্রিক ডেটা সার্চ
```python
# 3D গ্রিডে ভ্যালু সার্চ
def ternary_search_3d(arr, target):
    """
    3D সর্টেড অ্যারে জন্য টার্নারি সার্চ (প্রতিটি ডাইমেনশন সর্টেড)
    """
    def search(x1, x2, y1, y2, z1, z2):
        if x1 > x2 or y1 > y2 or z1 > z2:
            return None
        
        # প্রতিটি ডাইমেনশনে মিডপয়েন্ট
        mx1 = x1 + (x2 - x1) // 3
        mx2 = x2 - (x2 - x1) // 3
        
        my1 = y1 + (y2 - y1) // 3
        my2 = y2 - (y2 - y1) // 3
        
        mz1 = z1 + (z2 - z1) // 3
        mz2 = z2 - (z2 - z1) // 3
        
        # টার্গেট চেক
        for i in [mx1, mx2]:
            for j in [my1, my2]:
                for k in [mz1, mz2]:
                    if arr[i][j][k] == target:
                        return (i, j, k)
        
        # রিকার্সিভলি সার্চ (সিমপ্লিফাইড লজিক)
        # প্রকৃত ইমপ্লিমেন্টেশনে সব পার্টিশন চেক করতে হবে
        
        return None
    
    return search(0, len(arr)-1, 0, len(arr[0])-1, 0, len(arr[0][0])-1)
```

## পারফরম্যান্স বিশ্লেষণ
```python
import time
import random
import math

def performance_comparison():
    """বাইনারি vs টার্নারি সার্চ পারফরম্যান্স তুলনা"""
    
    # বিভিন্ন সাইজের ডেটাসেট
    sizes = [1000, 10000, 100000, 1000000]
    
    print("বাইনারি vs টার্নারি সার্চ পারফরম্যান্স তুলনা")
    print("-" * 60)
    print(f"{'Size':<10} {'Binary Time':<15} {'Ternary Time':<15} {'Ratio':<10}")
    print("-" * 60)
    
    for size in sizes:
        # সর্টেড ডেটা জেনারেট
        data = sorted(random.sample(range(size * 10), size))
        target = random.choice(data)
        
        # বাইনারি সার্চ টাইম
        start = time.time()
        for _ in range(1000):
            binary_search(data, target)
        binary_time = time.time() - start
        
        # টার্নারি সার্চ টাইম
        start = time.time()
        for _ in range(1000):
            ternary_search_iterative(data, target)
        ternary_time = time.time() - start
        
        print(f"{size:<10} {binary_time:<15.6f} {ternary_time:<15.6f} {ternary_time/binary_time:<10.3f}")

# পারফরম্যান্স টেস্ট চালান
performance_comparison()
```

## সীমাবদ্ধতা ও বিবেচনা

### সুবিধা:
1. কিছু ক্ষেত্রে বাইনারি সার্চের চেয়ে কম ইটারেশন লাগে
2. ইউনিমোডাল ফাংশন অপটিমাইজেশনে ভাল কাজ করে
3. মাল্টি-ডাইমেনশনাল সার্চে এক্সটেন্ড করা যায়

### অসুবিধা:
1. প্রতি ধাপে ২টি তুলনা লাগে
2. ক্যাশে মেমরি এক্সেস কম ইফিসিয়েন্ট
3. বাইনারি সার্চের তুলনায় সাধারণত কম ব্যবহার হয়

### কখন ব্যবহার করবেন:
- ইউনিমোডাল ফাংশনের মিনিমাম/ম্যাক্সিমাম খুঁজতে
- যখন তুলনা অপারেশন সস্তা হয়
- ৩-এর পাওয়ারে সাইজের ডেটাসেটে
- শিক্ষণীয় উদ্দেশ্যে

### কখন ব্যবহার করবেন না:
- সাধারণ সর্টেড অ্যারে সার্চে (বাইনারি ভাল)
- যখন তুলনা অপারেশন ব্যয়বহুল
- রিয়েল-টাইম সিস্টেমে যেখানে পারফরম্যান্স ক্রিটিক্যাল

## উপসংহার
টার্নারি সার্চ একটি আকর্ষণীয় অ্যালগরিদম যা বাইনারি সার্চের ধারণাকে একধাপ এগিয়ে নেয়। যদিও সাধারণ সার্চ অপারেশনের জন্য বাইনারি সার্চই বেশি কার্যকর, বিশেষ কিছু সমস্যা (যেমন ইউনিমোডাল ফাংশন অপটিমাইজেশন) এর জন্য টার্নারি সার্চ দারুণ কাজ করে।