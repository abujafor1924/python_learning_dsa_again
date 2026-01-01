# পারমুটেশন জেনারেশন বিস্তারিত বাংলায়

পারমুটেশন হল উপাদানগুলোর সম্ভাব্য সব বিন্যাস। n টি উপাদানের জন্য মোট n! টি পারমুটেশন হয়।

## পারমুটেশন জেনারেশনের বিভিন্ন পদ্ধতি

### ১. ব্যাকট্র্যাকিং পদ্ধতি (সবচেয়ে সাধারণ)
```python
def permutations_backtracking(nums):
    """
    ব্যাকট্র্যাকিং ব্যবহার করে সব পারমুটেশন জেনারেট করা।
    """
    def backtrack(path, used, result):
        if len(path) == len(nums):
            result.append(path[:])  # কপি সংরক্ষণ
            return
        
        for i in range(len(nums)):
            if not used[i]:
                # উপাদান ব্যবহার করুন
                used[i] = True
                path.append(nums[i])
                
                # রিকার্সিভলি পরবর্তী উপাদান
                backtrack(path, used, result)
                
                # ব্যাকট্র্যাক
                path.pop()
                used[i] = False
    
    result = []
    used = [False] * len(nums)
    backtrack([], used, result)
    return result

# উদাহরণ
nums = [1, 2, 3]
perms = permutations_backtracking(nums)
print("ব্যাকট্র্যাকিং পদ্ধতি:")
for i, perm in enumerate(perms):
    print(f"{i+1}: {perm}")
```

### ২. Python এর itertools ব্যবহার করে
```python
import itertools

def permutations_itertools(nums):
    """
    Python এর বিল্ট-ইন itertools ব্যবহার করে।
    """
    return list(itertools.permutations(nums))

# উদাহরণ
nums = ['a', 'b', 'c']
perms = permutations_itertools(nums)
print("\nItertools পদ্ধতি:")
for i, perm in enumerate(perms):
    print(f"{i+1}: {perm}")
```

### ৩. হিপ অ্যালগরিদম (Heap's Algorithm) - সবচেয়ে কার্যকর
```python
def permutations_heap(nums):
    """
    হিপ অ্যালগরিদম - O(n!) টাইম, O(1) এক্সট্রা স্পেস।
    """
    def generate(k, arr, result):
        if k == 1:
            result.append(arr[:])
        else:
            for i in range(k):
                generate(k-1, arr, result)
                
                # k জোড়/বিজোড় অনুযায়ী swap
                if k % 2 == 0:
                    arr[i], arr[k-1] = arr[k-1], arr[i]
                else:
                    arr[0], arr[k-1] = arr[k-1], arr[0]
    
    result = []
    generate(len(nums), nums[:], result)  # কপি পাস করা
    return result

# উদাহরণ
nums = [1, 2, 3]
perms = permutations_heap(nums)
print("\nহিপ অ্যালগরিদম:")
for i, perm in enumerate(perms):
    print(f"{i+1}: {perm}")
```

### ৪. Next Permutation (Lexicographic Order)
```python
def next_permutation(arr):
    """
    লেক্সিকোগ্রাফিকভাবে পরবর্তী পারমুটেশন খুঁজে দেয়।
    """
    # ১. প্রথম ডিসেন্ডিং পেয়ার খুঁজুন
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    if i >= 0:
        # ২. arr[i] এর চেয়ে বড় ক্ষুদ্রতম সংখ্যা খুঁজুন
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    
    # ৩. i+1 থেকে শেষ পর্যন্ত reverse করুন
    left, right = i + 1, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return i >= 0

def permutations_lexicographic(nums):
    """
    লেক্সিকোগ্রাফিক অর্ডারে পারমুটেশন।
    """
    nums = sorted(nums)  # প্রথমে সর্ট করা
    result = [nums[:]]
    
    while next_permutation(nums):
        result.append(nums[:])
    
    return result

# উদাহরণ
nums = [3, 1, 2]
perms = permutations_lexicographic(nums)
print("\nলেক্সিকোগ্রাফিক অর্ডার:")
for i, perm in enumerate(perms):
    print(f"{i+1}: {perm}")
```

### ৫. রিকার্সিভ সোয়াপ পদ্ধতি
```python
def permutations_swap(nums):
    """
    সোয়াপ ব্যবহার করে রিকার্সিভ পারমুটেশন।
    """
    def backtrack(start, arr, result):
        if start == len(arr):
            result.append(arr[:])
            return
        
        for i in range(start, len(arr)):
            # সোয়াপ করুন
            arr[start], arr[i] = arr[i], arr[start]
            
            # পরবর্তী ইনডেক্সে রিকার্সিভ কল
            backtrack(start + 1, arr, result)
            
            # ব্যাকট্র্যাক (আবার সোয়াপ)
            arr[start], arr[i] = arr[i], arr[start]
    
    result = []
    backtrack(0, nums[:], result)
    return result

# উদাহরণ
nums = ['x', 'y', 'z']
perms = permutations_swap(nums)
print("\nসোয়াপ পদ্ধতি:")
for i, perm in enumerate(perms):
    print(f"{i+1}: {perm}")
```

## বিশেষ ধরনের পারমুটেশন

### ১. ডুপ্লিকেট উপাদান সহ পারমুটেশন
```python
def permutations_with_duplicates(nums):
    """
    ডুপ্লিকেট উপাদান থাকলে ইউনিক পারমুটেশন।
    """
    def backtrack(path, counter, result, n):
        if len(path) == n:
            result.append(path[:])
            return
        
        for num in counter:
            if counter[num] > 0:
                # পছন্দ করুন
                path.append(num)
                counter[num] -= 1
                
                # রিকার্সিভ কল
                backtrack(path, counter, result, n)
                
                # ব্যাকট্র্যাক
                path.pop()
                counter[num] += 1
    
    # কাউন্টার তৈরি
    from collections import Counter
    counter = Counter(nums)
    
    result = []
    backtrack([], counter, result, len(nums))
    return result

# উদাহরণ
nums = [1, 1, 2]
unique_perms = permutations_with_duplicates(nums)
print("\nডুপ্লিকেট সহ পারমুটেশন:")
print(f"মোট ইউনিক পারমুটেশন: {len(unique_perms)}")
for perm in unique_perms:
    print(perm)
```

### ২. k-পারমুটেশন (P(n, k))
```python
def k_permutations(nums, k):
    """
    n টি উপাদান থেকে k টি নিয়ে পারমুটেশন।
    P(n, k) = n! / (n-k)!
    """
    def backtrack(path, used, result):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                
                backtrack(path, used, result)
                
                path.pop()
                used[i] = False
    
    result = []
    used = [False] * len(nums)
    backtrack([], used, result)
    return result

# উদাহরণ
nums = [1, 2, 3, 4]
k = 2
perms_k = k_permutations(nums, k)
print(f"\n{nums} থেকে {k} টি নিয়ে পারমুটেশন:")
print(f"মোট পারমুটেশন: {len(perms_k)}")
for perm in perms_k:
    print(perm)
```

### ৩. সার্কুলার পারমুটেশন
```python
def circular_permutations(nums):
    """
    সার্কুলার পারমুটেশন - (n-1)!
    প্রথম উপাদান ফিক্স করে বাকিগুলো পারমুটেশন।
    """
    if not nums:
        return []
    
    result = []
    first = nums[0]
    remaining = nums[1:]
    
    # বাকি উপাদানগুলোর পারমুটেশন
    for perm in permutations_backtracking(remaining):
        result.append([first] + perm)
    
    return result

# উদাহরণ
nums = [1, 2, 3, 4]
circular_perms = circular_permutations(nums)
print("\nসার্কুলার পারমুটেশন (প্রথম উপাদান ফিক্স):")
print(f"মোট সার্কুলার পারমুটেশন: {len(circular_perms)}")
for perm in circular_perms:
    print(perm)
```

## পারফরম্যান্স তুলনা
```python
import time
import math

def performance_comparison():
    """বিভিন্ন পদ্ধতির পারফরম্যান্স তুলনা"""
    
    nums = list(range(1, 8))  # 7 উপাদান
    print(f"৭ টি উপাদানের পারমুটেশন ({math.factorial(7)} টি)")
    print("=" * 50)
    
    # পদ্ধতি এবং তাদের ফাংশন
    methods = [
        ("ব্যাকট্র্যাকিং", permutations_backtracking),
        ("হিপ অ্যালগরিদম", permutations_heap),
        ("সোয়াপ পদ্ধতি", permutations_swap),
        ("লেক্সিকোগ্রাফিক", permutations_lexicographic),
    ]
    
    for name, func in methods:
        start = time.time()
        result = func(nums)
        end = time.time()
        
        print(f"{name}:")
        print(f"  সময়: {end-start:.4f} সেকেন্ড")
        print(f"  পারমুটেশন সংখ্যা: {len(result)}")
        print(f"  প্রত্যাশিত: {math.factorial(len(nums))}")
        print()
    
    # Itertools (সবচেয়ে দ্রুত)
    start = time.time()
    result = list(itertools.permutations(nums))
    end = time.time()
    print(f"Itertools:")
    print(f"  সময়: {end-start:.4f} সেকেন্ড")
    print(f"  পারমুটেশন সংখ্যা: {len(result)}")

# পারফরম্যান্স টেস্ট
performance_comparison()
```

## ভিজ্যুয়ালাইজেশন
```python
def visualize_permutations(nums):
    """পারমুটেশন ট্রি ভিজ্যুয়ালাইজেশন"""
    def backtrack_tree(path, used, level):
        if len(path) == len(nums):
            print("  " * level + "-> " + str(path))
            return
        
        for i in range(len(nums)):
            if not used[i]:
                print("  " * level + f"চয়ন: {nums[i]}")
                used[i] = True
                path.append(nums[i])
                
                backtrack_tree(path, used, level + 1)
                
                path.pop()
                used[i] = False
    
    print(f"{nums} এর পারমুটেশন ট্রি:")
    used = [False] * len(nums)
    backtrack_tree([], used, 0)

# ছোট উদাহরণ ভিজ্যুয়ালাইজ
nums_small = [1, 2, 3]
visualize_permutations(nums_small)
```

## রিয়েল-লাইফ অ্যাপ্লিকেশন

### ১. পাসওয়ার্ড জেনারেশন
```python
def generate_passwords(chars, length):
    """পাসওয়ার্ড জেনারেশন"""
    passwords = []
    
    def backtrack(password):
        if len(password) == length:
            passwords.append(''.join(password))
            return
        
        for char in chars:
            password.append(char)
            backtrack(password)
            password.pop()
    
    backtrack([])
    return passwords

# উদাহরণ
chars = ['a', 'b', 'c']
length = 2
passwords = generate_passwords(chars, length)
print("\nপাসওয়ার্ড জেনারেশন:")
print(f"ক্যারেক্টার: {chars}, দৈর্ঘ্য: {length}")
print(f"মোট পাসওয়ার্ড: {len(passwords)}")
print(passwords)
```

### ২. শিডিউলিং সমস্যা
```python
def schedule_tasks(tasks):
    """টাস্ক শিডিউলিং - সব সম্ভাব্য ক্রম"""
    schedules = []
    
    def backtrack(schedule, remaining):
        if not remaining:
            schedules.append(schedule[:])
            return
        
        for i in range(len(remaining)):
            schedule.append(remaining[i])
            backtrack(schedule, remaining[:i] + remaining[i+1:])
            schedule.pop()
    
    backtrack([], tasks)
    return schedules

# উদাহরণ
tasks = ['A', 'B', 'C']
schedules = schedule_tasks(tasks)
print("\nটাস্ক শিডিউলিং:")
print(f"টাস্ক: {tasks}")
print(f"সম্ভাব্য শিডিউল সংখ্যা: {len(schedules)}")
for schedule in schedules:
    print(f"  {schedule}")
```

### ৩. DNA সিকোয়েন্স কম্বিনেশন
```python
def dna_combinations(length):
    """DNA সিকোয়েন্স জেনারেশন"""
    bases = ['A', 'T', 'C', 'G']
    sequences = []
    
    def backtrack(sequence):
        if len(sequence) == length:
            sequences.append(''.join(sequence))
            return
        
        for base in bases:
            sequence.append(base)
            backtrack(sequence)
            sequence.pop()
    
    backtrack([])
    return sequences

# উদাহরণ
length = 3
dna_seqs = dna_combinations(length)
print(f"\nDNA সিকোয়েন্স (দৈর্ঘ্য {length}):")
print(f"বেস: A, T, C, G")
print(f"মোট সিকোয়েন্স: {len(dna_seqs)}")
print("প্রথম ২০টি সিকোয়েন্স:")
for i in range(min(20, len(dna_seqs))):
    print(dna_seqs[i], end=" ")
    if (i + 1) % 5 == 0:
        print()
```

### ৪. নম্বর প্লেট জেনারেশন
```python
def generate_number_plates(letters, numbers):
    """গাড়ির নম্বর প্লেট জেনারেশন"""
    plates = []
    
    def backtrack(plate, letters_used, numbers_used):
        if len(plate) == 7:  # 3 letters + 4 numbers
            plates.append(''.join(plate))
            return
        
        if len(plate) < 3:
            # অক্ষর যোগ
            for letter in letters:
                if letter not in letters_used:
                    plate.append(letter)
                    backtrack(plate, letters_used | {letter}, numbers_used)
                    plate.pop()
        else:
            # সংখ্যা যোগ
            for number in numbers:
                if number not in numbers_used:
                    plate.append(number)
                    backtrack(plate, letters_used, numbers_used | {number})
                    plate.pop()
    
    backtrack([], set(), set())
    return plates

# উদাহরণ
letters = ['A', 'B', 'C']
numbers = ['1', '2', '3', '4']
plates = generate_number_plates(letters, numbers)
print(f"\nনম্বর প্লেট (3 অক্ষর + 4 সংখ্যা):")
print(f"অক্ষর: {letters}")
print(f"সংখ্যা: {numbers}")
print(f"মোট প্লেট: {len(plates)}")
print("কিছু প্লেট উদাহরণ:")
for i in range(min(10, len(plates))):
    print(f"  {plates[i]}")
```

## অ্যাডভান্সড কনসেপ্ট

### ১. ইনভার্স পারমুটেশন
```python
def inverse_permutation(perm):
    """ইনভার্স পারমুটেশন"""
    inv = [0] * len(perm)
    for i, p in enumerate(perm):
        inv[p] = i
    return inv

# উদাহরণ
perm = [2, 0, 1]
inv = inverse_permutation(perm)
print(f"\nপারমুটেশন: {perm}")
print(f"ইনভার্স: {inv}")
```

### ২. পারমুটেশন সাইকেল
```python
def permutation_cycles(perm):
    """পারমুটেশন সাইকেল ডিকম্পোজিশন"""
    n = len(perm)
    visited = [False] * n
    cycles = []
    
    for i in range(n):
        if not visited[i]:
            cycle = []
            j = i
            
            while not visited[j]:
                visited[j] = True
                cycle.append(j)
                j = perm[j]
            
            if len(cycle) > 1 or cycle[0] != perm[cycle[0]]:
                cycles.append(cycle)
    
    return cycles

# উদাহরণ
perm = [2, 0, 1, 4, 3]
cycles = permutation_cycles(perm)
print(f"\nপারমুটেশন: {perm}")
print(f"সাইকেল: {cycles}")
```

### ৩. পারমুটেশন সিগনেচার
```python
def permutation_signature(perm):
    """পারমুটেশন সিগনেচার (ইভেন/অড)"""
    n = len(perm)
    visited = [False] * n
    transpositions = 0
    
    for i in range(n):
        if not visited[i]:
            cycle_length = 0
            j = i
            
            while not visited[j]:
                visited[j] = True
                j = perm[j]
                cycle_length += 1
            
            if cycle_length > 0:
                transpositions += cycle_length - 1
    
    # সিগনেচার = (-1)^(transpositions)
    return "ইভেন" if transpositions % 2 == 0 else "অড"

# উদাহরণ
perm = [1, 0, 2, 3]
signature = permutation_signature(perm)
print(f"\nপারমুটেশন: {perm}")
print(f"সিগনেচার: {signature}")
```

## মেমোরি ইফিসিয়েন্ট ভার্সন
```python
def permutations_memory_efficient(nums):
    """
    মেমোরি ইফিসিয়েন্ট পারমুটেশন - জেনারেটর ব্যবহার।
    """
    def backtrack(start):
        if start == len(nums) - 1:
            yield nums[:]
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            yield from backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    
    return backtrack(0)

# ব্যবহার
nums = [1, 2, 3]
print("\nজেনারেটর ব্যবহার করে পারমুটেশন:")
for i, perm in enumerate(permutations_memory_efficient(nums)):
    print(f"{i+1}: {perm}")
```

## উপকারিতা ও সীমাবদ্ধতা

### উপকারিতা:
1. সব সম্ভাব্যতা কভার করে
2. সহজে বোঝা যায়
3. বিভিন্ন সমস্যায় প্রযোজ্য
4. অন্যান্য অ্যালগরিদমের বিল্ডিং ব্লক

### সীমাবদ্ধতা:
1. O(n!) টাইম কমপ্লেক্সিটি
2. বড় n এর জন্য অনুপযুক্ত
3. মেমোরি ব্যয়বহুল

### সমাধান:
1. n ≤ 10 পর্যন্ত ব্যবহার করা ভাল
2. প্রুনিং করে সার্চ স্পেস কমানো
3. জেনারেটর ব্যবহার করে মেমোরি সেভ করা
4. ডাইনামিক প্রোগ্রামিং এর সাথে কম্বাইন করা

## উপসংহার
পারমুটেশন জেনারেশন কম্বিনেটরিক্স এবং অ্যালগরিদমের একটি মৌলিক কনসেপ্ট। বিভিন্ন সমস্যা যেমন শিডিউলিং, ক্রিপ্টোগ্রাফি, গেম থিওরি, এবং ডেটা অ্যানালাইসিসে এর ব্যাপক ব্যবহার আছে। সঠিক পদ্ধতি নির্বাচন করে পারফরম্যান্স অপটিমাইজ করা গুরুত্বপূর্ণ।