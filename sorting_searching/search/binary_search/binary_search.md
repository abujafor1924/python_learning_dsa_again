# বাইনারি সার্চ বিস্তারিত বাংলায়

বাইনারি সার্চ একটি দক্ষ অ্যালগরিদম যা **সর্টেড (সাজানো)** লিস্ট থেকে কোনো আইটেম খুঁজে পেতে ব্যবহৃত হয়। এটি বারবার সার্চের পরিসরকে অর্ধেক ভাগ করে।

## মূল বৈশিষ্ট্য
- **টাইম কমপ্লেক্সিটি**: O(log n)
- **প্রয়োজনীয়তা**: লিস্ট অবশ্যই সর্টেড থাকতে হবে
- **পদ্ধতি**: ডিভাইড এন্ড কনকয়ার (বিভক্ত কর ও জয় কর)

## অ্যালগরিদমের ধাপ
১. সম্পূর্ণ সর্টেড লিস্ট দিয়ে শুরু করুন
২. টার্গেটের সাথে মিডল এলিমেন্ট তুলনা করুন
৩. টার্গেট মিডল এলিমেন্টের সমান হলে, ইনডেক্স রিটার্ন করুন
৪. টার্গেট ছোট হলে, বাম অংশে সার্চ করুন
৫. টার্গেট বড় হলে, ডান অংশে সার্চ করুন
৬. খুঁজে পাওয়া বা সার্চ স্পেস খালি না হওয়া পর্যন্ত পুনরাবৃত্তি করুন

## পাইথন উদাহরণ

### ১. ইটারেটিভ পদ্ধতি (Iterative Approach)
```python
def binary_search_iterative(arr, target):
    """
    ইটারেটিভ বাইনারি সার্চ ইমপ্লিমেন্টেশন।
    
    আর্গুমেন্ট:
        arr: সর্টেড লিস্ট
        target: খোঁজার উপাদান
        
    রিটার্ন:
        টার্গেট পাওয়া গেলে ইনডেক্স, নাহলে -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # মধ্যবর্তী ইনডেক্স
        
        # টার্গেট মাঝখানে আছে কিনা চেক করুন
        if arr[mid] == target:
            return mid
        
        # টার্গেট বড় হলে, বাম অংশ উপেক্ষা করুন
        elif arr[mid] < target:
            left = mid + 1
        
        # টার্গেট ছোট হলে, ডান অংশ উপেক্ষা করুন
        else:
            right = mid - 1
    
    return -1  # টার্গেট পাওয়া যায়নি
```

### ২. রিকার্সিভ পদ্ধতি (Recursive Approach)
```python
def binary_search_recursive(arr, target, left, right):
    """
    রিকার্সিভ বাইনারি সার্চ ইমপ্লিমেন্টেশন।
    
    আর্গুমেন্ট:
        arr: সর্টেড লিস্ট
        target: খোঁজার উপাদান
        left: বর্তমান বাম সীমা
        right: বর্তমান ডান সীমা
        
    রিটার্ন:
        টার্গেট পাওয়া গেলে ইনডেক্স, নাহলে -1
    """
    if left > right:
        return -1  # বেস কেস: টার্গেট নেই
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# সহজে ব্যবহারের জন্য র্যাপার ফাংশন
def binary_search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)
```

### ৩. বিল্ট-ইন পদ্ধতি (Built-in Method)
পাইথনে বাইনারি সার্চের জন্য বিল্ট-ইন মডিউল আছে:
```python
import bisect

def binary_search_builtin(arr, target):
    """
    Python এর bisect মডিউল ব্যবহার করে বাইনারি সার্চ।
    """
    index = bisect.bisect_left(arr, target)
    
    # চেক করুন যে ইনডেক্স সীমার মধ্যে আছে এবং মান মিলে যায়
    if index < len(arr) and arr[index] == target:
        return index
    return -1
```

## ব্যবহারের উদাহরণ
```python
# সর্টেড লিস্ট তৈরি
numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
target = 23

# ইটারেটিভ পদ্ধতি
result1 = binary_search_iterative(numbers, target)
print(f"ইটারেটিভ: টার্গেট {target} ইনডেক্স {result1} এ আছে")

# রিকার্সিভ পদ্ধতি
result2 = binary_search(numbers, target)
print(f"রিকার্সিভ: টার্গেট {target} ইনডেক্স {result2} এ আছে")

# বিল্ট-ইন পদ্ধতি
result3 = binary_search_builtin(numbers, target)
print(f"বিল্ট-ইন: টার্গেট {target} ইনডেক্স {result3} এ আছে")
```

## টেস্ট কেস সহ সম্পূর্ণ উদাহরণ
```python
# সম্পূর্ণ উদাহরণ
def main():
    # সর্টেড লিস্ট
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    # বিভিন্ন টেস্ট কেস
    test_cases = [10, 50, 100, 25, 110]
    
    print("বাইনারি সার্চ ডেমো")
    print("ডেটা:", data)
    print("-" * 40)
    
    for target in test_cases:
        result = binary_search_iterative(data, target)
        if result != -1:
            print(f"টার্গেট {target} ইনডেক্স {result} এ পাওয়া গেছে")
        else:
            print(f"টার্গেট {target} লিস্টে নেই")

if __name__ == "__main__":
    main()
```

## ভিজ্যুয়ালাইজেশন
```
প্রথম ধাপ: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
           left=0, right=9, mid=4 (value=50)
           50 < 70, তাই ডান অংশে যান

দ্বিতীয় ধাপ: [60, 70, 80, 90, 100]
            left=5, right=9, mid=7 (value=80)
            80 > 70, তাই বাম অংশে যান

তৃতীয় ধাপ: [60, 70]
            left=5, right=6, mid=5 (value=60)
            60 < 70, তাই ডান অংশে যান

চতুর্থ ধাপ: [70]
            left=6, right=6, mid=6 (value=70)
            70 == 70, পাওয়া গেছে!
```

## গুরুত্বপূর্ণ বিষয়
1. **লিস্ট সর্টেড থাকতে হবে** - অন্যথায় কাজ করবে না
2. **মিড ইনডেক্স ক্যালকুলেশন** - `mid = (left + right) // 2`
3. **সীমা আপডেট** - `left = mid + 1` বা `right = mid - 1`
4. **শর্ত** - `while left <= right:` (অনুপস্থিত হলে লুপ থেমে যায়)

## রিয়েল-লাইফ ব্যবহার
- ডিকশনারিতে শব্দ খোঁজা
- ফোনবুকে নাম খোঁজা
- ডাটাবেজে রেকর্ড খোঁজা (ইনডেক্সড কলাম)
- গেমসে হাই-স্কোর তালিকা

এই পদ্ধতিটি লিনিয়ার সার্চের (O(n)) তুলনায় অনেক বেশি কার্যকর, বিশেষত বড় ডেটাসেটের জন্য।