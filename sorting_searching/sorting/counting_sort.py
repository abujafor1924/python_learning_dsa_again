

"""  
কাউন্টিং সর্ট কি?
কাউন্টিং সর্ট একটি নন-কম্পারিজন ভিত্তিক সর্টিং অ্যালগরিদম। এটি এলিমেন্টের সংখ্যা গণনা করে এবং সেই গণনা ব্যবহার করে এলিমেন্টগুলিকে সঠিক পজিশনে বসায়। এটি ইন্টিজার সর্টিং এর জন্য বিশেষভাবে উপযোগী।

কিভাবে কাজ করে?
১. ইনপুট অ্যারেতে সর্বোচ্চ এবং সর্বনিম্ন মান খুঁজে বের করুন।
২. একটি কাউন্ট অ্যারে তৈরি করুন যার সাইজ হবে (max-min+1)।
৩. প্রতিটি এলিমেন্টের ঘটনার সংখ্যা গণনা করুন।
৪. কাউন্ট অ্যারেকে ক্রমিক যোগ করুন (cumulative sum)।
৫. আউটপুট অ্যারে তৈরি করুন এবং প্রতিটি এলিমেন্টকে সঠিক পজিশনে বসান।
৬. আউটপুট অ্যারে কপি করুন মূল অ্যারেতে।

অ্যালগরিদম স্টেপস
ধাপ ১: max = অ্যারের সর্বোচ্চ মান, min = অ্যারের সর্বনিম্ন মান
ধাপ ২: range = max - min + 1
ধাপ ৩: count[range] অ্যারে তৈরি করো, সব 0 দিয়ে ইনিশিয়ালাইজ করো
ধাপ ৪: প্রতিটি এলিমেন্টের কাউন্ট ইনক্রিমেন্ট করো
ধাপ ৫: কাউন্ট অ্যারেতে ক্রমিক যোগ করো
ধাপ ৬: আউটপুট অ্যারে তৈরি করো
ধাপ ৭: প্রতিটি এলিমেন্টকে সঠিক পজিশনে বসাও
"""


def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    
    range_size = max_val - min_val + 1
    count = [0] * range_size
    output = [0] * len(arr)
    
    for num in arr:
        count[num - min_val] += 1
    
    for i in range(1, range_size):
        count[i] += count[i-1]

    for num in reversed(arr):
        position = count[num - min_val] - 1
        output[position] = num
        count[num - min_val] -= 1
    
    return output

arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))

# ===================== Copy From AI =============================
def counting_sort_stable(arr, key=lambda x: x):
    if not arr:
        return arr
    
    # ধাপ ১: সর্বোচ্চ ও সর্বনিম্ন মান
    max_val = key(max(arr, key=key))
    min_val = key(min(arr, key=key))
    range_size = max_val - min_val + 1
    
    # ধাপ ২: কাউন্ট ও আউটপুট অ্যারে
    count = [0] * range_size
    output = [None] * len(arr)
    
    # ধাপ ৩: কাউন্টিং
    for item in arr:
        count[key(item) - min_val] += 1
    
    # ধাপ ৪: ক্রমিক যোগ
    for i in range(1, range_size):
        count[i] += count[i-1]
    
    # ধাপ ৫: স্টেবল আউটপুট (পেছন থেকে)
    for item in reversed(arr):
        index = key(item) - min_val
        position = count[index] - 1
        output[position] = item
        count[index] -= 1
    
    return output

# উদাহরণ
arr = [("apple", 3), ("banana", 1), ("cherry", 2), ("date", 1)]
sorted_by_number = counting_sort_stable(arr, key=lambda x: x[1])
print("স্টেবল সর্ট:", sorted_by_number)


def counting_sort_negative(arr):
    if not arr:
        return arr
    
    # ধাপ ১: সর্বোচ্চ ও সর্বনিম্ন মান
    max_val = max(arr)
    min_val = min(arr)
    
    # নেগেটিভ সংখ্যা হ্যান্ডেল
    offset = -min_val if min_val < 0 else 0
    range_size = max_val - min_val + 1
    
    # ধাপ ২: কাউন্ট অ্যারে
    count = [0] * range_size
    output = [0] * len(arr)
    
    # ধাপ ৩: কাউন্টিং
    for num in arr:
        count[num + offset] += 1
    
    # ধাপ ৪: ক্রমিক যোগ
    for i in range(1, range_size):
        count[i] += count[i-1]
    
    # ধাপ ৫: আউটপুট তৈরি
    for num in reversed(arr):
        position = count[num + offset] - 1
        output[position] = num
        count[num + offset] -= 1
    
    return output

# উদাহরণ
arr = [-5, -10, 0, -3, 8, 5, -1, 10]
print("নেগেটিভ সহ সর্ট:", counting_sort_negative(arr))


def counting_sort_inplace(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    # কাউন্ট অ্যারে
    count = [0] * range_size
    
    # কাউন্টিং
    for num in arr:
        count[num - min_val] += 1
    
    # অ্যারেতে সরাসরি লিখি
    index = 0
    for i in range(range_size):
        value = i + min_val
        for _ in range(count[i]):
            arr[index] = value
            index += 1
    
    return arr

# উদাহরণ
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort_inplace(arr)
print("ইন-প্লেস সর্ট:", arr)


def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # ডিজিট 0-9
    
    # কাউন্টিং
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # ক্রমিক যোগ
    for i in range(1, 10):
        count[i] += count[i-1]
    
    # আউটপুট তৈরি
    for i in range(n-1, -1, -1):
        index = (arr[i] // exp) % 10
        position = count[index] - 1
        output[position] = arr[i]
        count[index] -= 1
    
    return output

def counting_sort_characters(s):
    if not s:
        return ""
    
    # ASCII values: 'a'=97, 'z'=122
    min_val = ord('a')
    max_val = ord('z')
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    output = [''] * len(s)
    
    # কাউন্টিং
    for char in s:
        if 'a' <= char <= 'z':
            count[ord(char) - min_val] += 1
    
    # ক্রমিক যোগ
    for i in range(1, range_size):
        count[i] += count[i-1]
    
    # আউটপুট তৈরি
    for char in reversed(s):
        if 'a' <= char <= 'z':
            index = ord(char) - min_val
            position = count[index] - 1
            output[position] = char
            count[index] -= 1
    
    # অন্যান্য ক্যারেক্টার যোগ
    result = []
    output_index = 0
    
    for char in s:
        if 'a' <= char <= 'z':
            result.append(output[output_index])
            output_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

text = "counting sort example"
print("সর্টেড ক্যারেক্টার:", counting_sort_characters(text))

def get_frequency(arr):
    if not arr:
        return {}
    
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    
    for num in arr:
        count[num - min_val] += 1
    
    frequency = {}
    for i in range(range_size):
        if count[i] > 0:
            value = i + min_val
            frequency[value] = count[i]
    
    return frequency

arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("ফ্রিকোয়েন্সি:", get_frequency(arr))