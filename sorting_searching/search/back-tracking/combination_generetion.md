# কম্বিনেশন জেনারেশন বিস্তারিত বাংলায়

কম্বিনেশন হল উপাদানগুলোর **অর্ডার বিবেচনা না করে** নির্বাচন। n টি উপাদান থেকে k টি নেওয়ার মোট কম্বিনেশন: C(n, k) = n! / (k! * (n-k)!)

## কম্বিনেশন জেনারেশনের বিভিন্ন পদ্ধতি

### ১. ব্যাকট্র্যাকিং পদ্ধতি (সবচেয়ে সাধারণ)
```python
def combinations_backtracking(nums, k):
    """
    ব্যাকট্র্যাকিং ব্যবহার করে n থেকে k টি উপাদানের কম্বিনেশন।
    """
    def backtrack(start, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, len(nums)):
            path.append(nums[i])          # উপাদান যোগ
            backtrack(i + 1, path, result)  # পরবর্তী উপাদান
            path.pop()                    # ব্যাকট্র্যাক
    
    result = []
    backtrack(0, [], result)
    return result

# উদাহরণ
nums = [1, 2, 3, 4]
k = 2
combs = combinations_backtracking(nums, k)
print("ব্যাকট্র্যাকিং পদ্ধতি:")
for i, comb in enumerate(combs):
    print(f"{i+1}: {comb}")
```

### ২. Python এর itertools ব্যবহার করে
```python
import itertools

def combinations_itertools(nums, k):
    """
    Python এর বিল্ট-ইন itertools ব্যবহার করে।
    """
    return list(itertools.combinations(nums, k))

# উদাহরণ
nums = ['a', 'b', 'c', 'd']
k = 2
combs = combinations_itertools(nums, k)
print("\nItertools পদ্ধতি:")
for i, comb in enumerate(combs):
    print(f"{i+1}: {comb}")
```

### ৩. বাইনারি বিটমাস্ক পদ্ধতি
```python
def combinations_bitmask(nums, k):
    """
    বাইনারি বিটমাস্ক ব্যবহার করে (n ≤ 20 এর জন্য ভাল)।
    """
    n = len(nums)
    result = []
    
    # 1 থেকে 2^n পর্যন্ত সব সংখ্যা
    for mask in range(1, 1 << n):
        # বিট সংখ্যা গণনা
        if bin(mask).count('1') != k:
            continue
        
        # কম্বিনেশন তৈরি
        comb = []
        for i in range(n):
            if mask & (1 << i):  # i-তম বিট চেক
                comb.append(nums[i])
        
        result.append(comb)
    
    return result

# উদাহরণ
nums = [10, 20, 30, 40]
k = 2
combs = combinations_bitmask(nums, k)
print("\nবিটমাস্ক পদ্ধতি:")
for i, comb in enumerate(combs):
    print(f"{i+1}: {comb}")
```

### ৪. রিকার্সিভ পদ্ধতি (C(n,k) = C(n-1,k-1) + C(n-1,k))
```python
def combinations_recursive(nums, k):
    """
    রিকার্সিভ রিলেশন ব্যবহার করে।
    """
    result = []
    
    def combine(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        if start >= len(nums):
            return
        
        # বর্তমান উপাদান নিন
        path.append(nums[start])
        combine(start + 1, path)
        path.pop()
        
        # বর্তমান উপাদান বাদ দিন
        combine(start + 1, path)
    
    combine(0, [])
    return result

# উদাহরণ
nums = [1, 2, 3]
k = 2
combs = combinations_recursive(nums, k)
print("\nরিকার্সিভ পদ্ধতি:")
for i, comb in enumerate(combs):
    print(f"{i+1}: {comb}")
```

### ৫. লেক্সিকোগ্রাফিক অর্ডারে
```python
def next_combination(indices, n):
    """
    পরবর্তী কম্বিনেশন ইনডেক্স খুঁজে দেয়।
    """
    k = len(indices)
    
    # ডান দিক থেকে প্রথম ইনডেক্স খুঁজুন যা সর্বোচ্চ নয়
    i = k - 1
    while i >= 0 and indices[i] == n - k + i:
        i -= 1
    
    if i < 0:
        return False
    
    # এই ইনডেক্স ইনক্রিমেন্ট করুন
    indices[i] += 1
    
    # পরবর্তী ইনডেক্সগুলো সেট করুন
    for j in range(i + 1, k):
        indices[j] = indices[j-1] + 1
    
    return True

def combinations_lexicographic(nums, k):
    """
    লেক্সিকোগ্রাফিক অর্ডারে কম্বিনেশন।
    """
    n = len(nums)
    result = []
    
    if k > n:
        return result
    
    # প্রথম কম্বিনেশন
    indices = list(range(k))
    result.append([nums[i] for i in indices])
    
    # পরবর্তী কম্বিনেশনগুলো
    while next_combination(indices, n):
        result.append([nums[i] for i in indices])
    
    return result

# উদাহরণ
nums = [1, 2, 3, 4, 5]
k = 3
combs = combinations_lexicographic(nums, k)
print("\nলেক্সিকোগ্রাফিক অর্ডার:")
print(f"প্রথম ১০টি কম্বিনেশন:")
for i in range(min(10, len(combs))):
    print(f"  {i+1}: {combs[i]}")
```

## বিশেষ ধরনের কম্বিনেশন

### ১. ডুপ্লিকেট উপাদান সহ কম্বিনেশন (মাল্টিসেট)
```python
def combinations_with_duplicates(nums, k):
    """
    ডুপ্লিকেট উপাদান থাকলে ইউনিক কম্বিনেশন।
    """
    def backtrack(start, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, len(nums)):
            # একই স্তরে একই উপাদান স্কিপ করুন
            if i > start and nums[i] == nums[i-1]:
                continue
            
            path.append(nums[i])
            backtrack(i + 1, path, result)
            path.pop()
    
    nums.sort()  # প্রথমে সর্ট করা জরুরি
    result = []
    backtrack(0, [], result)
    return result

# উদাহরণ
nums = [1, 1, 2, 2, 3]
k = 2
combs = combinations_with_duplicates(nums, k)
print("\nডুপ্লিকেট সহ কম্বিনেশন:")
print(f"মোট ইউনিক কম্বিনেশন: {len(combs)}")
for comb in combs:
    print(f"  {comb}")
```

### ২. কম্বিনেশন সাম (Combination Sum)
```python
def combination_sum(candidates, target):
    """
    সংখ্যার যোগফল টার্গেট হলে কম্বিনেশন।
    একই সংখ্যা বারবার ব্যবহার করা যাবে।
    """
    def backtrack(start, path, current_sum, result):
        if current_sum == target:
            result.append(path[:])
            return
        
        if current_sum > target:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, current_sum + candidates[i], result)
            path.pop()
    
    result = []
    backtrack(0, [], 0, result)
    return result

def combination_sum_no_repeat(candidates, target):
    """
    সংখ্যার যোগফল টার্গেট হলে কম্বিনেশন।
    একই সংখ্যা বারবার ব্যবহার করা যাবে না।
    """
    def backtrack(start, path, current_sum, result):
        if current_sum == target:
            result.append(path[:])
            return
        
        if current_sum > target:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i + 1, path, current_sum + candidates[i], result)
            path.pop()
    
    candidates.sort()
    result = []
    backtrack(0, [], 0, result)
    return result

# উদাহরণ
candidates = [2, 3, 6, 7]
target = 7
print("\nকম্বিনেশন সাম (পুনরাবৃত্তি সহ):")
combs = combination_sum(candidates, target)
for comb in combs:
    print(f"  {comb} = {sum(comb)}")

print("\nকম্বিনেশন সাম (পুনরাবৃত্তি ছাড়া):")
combs2 = combination_sum_no_repeat(candidates, target)
for comb in combs2:
    print(f"  {comb} = {sum(comb)}")
```

### ৩. k এর সব মানের জন্য কম্বিনেশন
```python
def all_combinations(nums):
    """
    k = 0 থেকে n পর্যন্ত সব কম্বিনেশন।
    """
    result = []
    n = len(nums)
    
    for k in range(n + 1):
        result.extend(combinations_backtracking(nums, k))
    
    return result

# উদাহরণ
nums = [1, 2, 3]
all_combs = all_combinations(nums)
print("\nসব সম্ভাব্য কম্বিনেশন:")
for i, comb in enumerate(all_combs):
    print(f"{i+1}: {comb}")
```

### ৪. মাল্টিপল গ্রুপ থেকে কম্বিনেশন
```python
def combinations_from_multiple_groups(groups, k):
    """
    মাল্টিপল গ্রুপ থেকে কম্বিনেশন।
    প্রতিটি গ্রুপ থেকে সর্বোচ্চ ১টি উপাদান।
    """
    def backtrack(group_idx, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        
        if group_idx >= len(groups):
            return
        
        # বর্তমান গ্রুপ থেকে একটি উপাদান নিন
        for item in groups[group_idx]:
            path.append(item)
            backtrack(group_idx + 1, path, result)
            path.pop()
        
        # বর্তমান গ্রুপ থেকে কিছুই নিন না
        backtrack(group_idx + 1, path, result)
    
    result = []
    backtrack(0, [], result)
    # শুধু k দৈর্ঘ্যের কম্বিনেশন রাখুন
    result = [comb for comb in result if len(comb) == k]
    return result

# উদাহরণ
groups = [['A', 'B'], [1, 2, 3], ['X', 'Y']]
k = 2
combs = combinations_from_multiple_groups(groups, k)
print("\nমাল্টিপল গ্রুপ থেকে কম্বিনেশন:")
for comb in combs:
    print(f"  {comb}")
```

### ৫. সাবসেট (সব কম্বিনেশনের সমষ্টি)
```python
def subsets(nums):
    """
    সব সাবসেট জেনারেশন (পাওয়ার সেট)।
    """
    result = []
    n = len(nums)
    
    # ০ থেকে ২^n - ১ পর্যন্ত সব সংখ্যা
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)
    
    return result

def subsets_backtracking(nums):
    """
    ব্যাকট্র্যাকিং ব্যবহার করে সাবসেট।
    """
    def backtrack(start, path, result):
        result.append(path[:])  # বর্তমান সাবসেট সংরক্ষণ
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, result)
            path.pop()
    
    result = []
    backtrack(0, [], result)
    return result

# উদাহরণ
nums = [1, 2, 3]
print("\nসব সাবসেট (পাওয়ার সেট):")
all_subsets = subsets(nums)
for subset in all_subsets:
    print(f"  {subset}")

print(f"\nমোট সাবসেট সংখ্যা: {len(all_subsets)} (2^{len(nums)} = {2**len(nums)})")
```

## পারফরম্যান্স তুলনা
```python
import time
import math

def performance_comparison():
    """বিভিন্ন পদ্ধতির পারফরম্যান্স তুলনা"""
    
    n = 20
    k = 10
    nums = list(range(1, n+1))
    
    print(f"C({n}, {k}) = {math.comb(n, k)} টি কম্বিনেশন")
    print("=" * 50)
    
    # শুধু পদ্ধতিগুলো টেস্ট করুন যেগুলো practical
    methods = [
        ("ইটারটুলস", combinations_itertools),
    ]
    
    # বড় ডেটার জন্য শুধু itertools
    start = time.time()
    combs = combinations_itertools(nums, k)
    end = time.time()
    
    print(f"Itertools:")
    print(f"  সময়: {end-start:.4f} সেকেন্ড")
    print(f"  কম্বিনেশন সংখ্যা: {len(combs)}")
    print()
    
    # ছোট ডেটার জন্য অন্যান্য পদ্ধতি
    small_nums = [1, 2, 3, 4, 5]
    k = 3
    
    methods = [
        ("ব্যাকট্র্যাকিং", combinations_backtracking),
        ("বিটমাস্ক", combinations_bitmask),
        ("লেক্সিকোগ্রাফিক", combinations_lexicographic),
    ]
    
    for name, func in methods:
        start = time.time()
        combs = func(small_nums, k)
        end = time.time()
        
        print(f"{name}:")
        print(f"  সময়: {end-start:.6f} সেকেন্ড")
        print(f"  কম্বিনেশন সংখ্যা: {len(combs)}")
        print(f"  প্রত্যাশিত: C({len(small_nums)}, {k}) = {math.comb(len(small_nums), k)}")
        print()

# পারফরম্যান্স টেস্ট
performance_comparison()
```

## রিয়েল-লাইফ অ্যাপ্লিকেশন

### ১. লটারি কম্বিনেশন
```python
def lottery_combinations(numbers, k):
    """
    লটারি সংখ্যার কম্বিনেশন জেনারেটর।
    """
    combs = combinations_backtracking(numbers, k)
    return combs

# উদাহরণ
lottery_numbers = list(range(1, 50))  # 1 থেকে 49
k = 6  # ৬টি সংখ্যা
print(f"\nলটারি কম্বিনেশন (1-49 থেকে {k}টি):")
print(f"মোট সম্ভাব্য কম্বিনেশন: {math.comb(49, 6):,}")
print("\nপ্রথম ৫টি কম্বিনেশন:")
combs = lottery_combinations(lottery_numbers[:10], k)  # শুধু প্রথম ১০টি সংখ্যা
for i in range(min(5, len(combs))):
    print(f"  {combs[i]}")
```

### ২. টিম নির্বাচন
```python
def select_team(players, team_size):
    """
    প্লেয়ারদের থেকে টিম নির্বাচন।
    """
    teams = combinations_backtracking(players, team_size)
    return teams

# উদাহরণ
players = ['আলী', 'বাবু', 'চন্দ্র', 'দিপু', 'এলান', 'ফারহান']
team_size = 3
teams = select_team(players, team_size)
print(f"\n{len(players)} জন প্লেয়ার থেকে {team_size} জনের টিম:")
print(f"মোট টিম: {len(teams)}")
print("\nকিছু টিম:")
for i in range(min(10, len(teams))):
    print(f"  টিম {i+1}: {teams[i]}")
```

### ৩. প্রোডাক্ট কম্বিনেশন
```python
def product_combinations(products, k):
    """
    প্রোডাক্টের কম্বিনেশন (ব্যান্ডল অফার)।
    """
    combs = combinations_backtracking(products, k)
    
    # প্রাইস সহ কম্বিনেশন
    priced_combs = []
    for comb in combs:
        total_price = sum(product['price'] for product in comb)
        discount = total_price * 0.1  # 10% ডিসকাউন্ট
        priced_combs.append({
            'products': comb,
            'total_price': total_price,
            'discounted_price': total_price - discount
        })
    
    return priced_combs

# উদাহরণ
products = [
    {'name': 'ল্যাপটপ', 'price': 50000},
    {'name': 'মাউস', 'price': 500},
    {'name': 'কীবোর্ড', 'price': 1000},
    {'name': 'হেডফোন', 'price': 1500},
    {'name': 'মাউসপ্যাড', 'price': 200}
]

k = 2
bundles = product_combinations(products, k)
print("\nপ্রোডাক্ট কম্বিনেশন (ব্যান্ডল):")
for bundle in bundles[:5]:  # প্রথম ৫টি
    print(f"\nব্যান্ডল:")
    for product in bundle['products']:
        print(f"  - {product['name']}: ${product['price']}")
    print(f"  মোট: ${bundle['total_price']}")
    print(f"  ডিসকাউন্টের পর: ${bundle['discounted_price']:.2f}")
```

### ৪. কোর্স সিলেকশন
```python
def select_courses(courses, credits_needed):
    """
    ক্রেডিট প্রয়োজন মেটানো কোর্স কম্বিনেশন।
    """
    result = []
    
    def backtrack(start, path, current_credits):
        if current_credits == credits_needed:
            result.append(path[:])
            return
        
        if current_credits > credits_needed or start >= len(courses):
            return
        
        # বর্তমান কোর্স নিন
        course = courses[start]
        path.append(course['name'])
        backtrack(start + 1, path, current_credits + course['credits'])
        path.pop()
        
        # বর্তমান কোর্স বাদ দিন
        backtrack(start + 1, path, current_credits)
    
    backtrack(0, [], 0)
    return result

# উদাহরণ
courses = [
    {'name': 'গণিত', 'credits': 3},
    {'name': 'পদার্থ', 'credits': 4},
    {'name': 'রসায়ন', 'credits': 4},
    {'name': 'বায়োলজি', 'credits': 3},
    {'name': 'ইংরেজি', 'credits': 2}
]

credits_needed = 7
selected = select_courses(courses, credits_needed)
print(f"\n{credits_needed} ক্রেডিটের কোর্স কম্বিনেশন:")
for combo in selected:
    credits = sum(courses[i]['credits'] for i, course in enumerate(courses) if course['name'] in combo)
    print(f"  {combo} = {credits} ক্রেডিট")
```

### ৫. ইনভেস্টমেন্ট কম্বিনেশন
```python
def investment_portfolios(stocks, budget, k=None):
    """
    বাজেটের মধ্যে স্টকের কম্বিনেশন।
    """
    result = []
    n = len(stocks)
    
    def backtrack(start, path, current_cost):
        # শুধু k টি স্টক লাগলে চেক
        if k is not None and len(path) == k:
            if current_cost <= budget:
                result.append({
                    'stocks': path[:],
                    'total_cost': current_cost,
                    'remaining_budget': budget - current_cost
                })
            return
        
        # বাজেট অতিক্রম করলে থামুন
        if current_cost > budget:
            return
        
        # বর্তমান পথ সংরক্ষণ (কোনো শর্ত না থাকলে)
        if k is None and path:
            result.append({
                'stocks': path[:],
                'total_cost': current_cost,
                'remaining_budget': budget - current_cost
            })
        
        for i in range(start, n):
            stock = stocks[i]
            path.append(stock['symbol'])
            backtrack(i + 1, path, current_cost + stock['price'])
            path.pop()
    
    backtrack(0, [], 0)
    return result

# উদাহরণ
stocks = [
    {'symbol': 'AAPL', 'price': 150},
    {'symbol': 'GOOGL', 'price': 2800},
    {'symbol': 'AMZN', 'price': 3400},
    {'symbol': 'MSFT', 'price': 300},
    {'symbol': 'TSLA', 'price': 700}
]

budget = 1000
print(f"\n${budget} বাজেটে স্টক কম্বিনেশন:")
portfolios = investment_portfolios(stocks, budget, k=2)
for portfolio in portfolios[:10]:  # প্রথম ১০টি
    print(f"  {portfolio['stocks']}: ${portfolio['total_cost']} (বাকি: ${portfolio['remaining_budget']})")
```

## অ্যাডভান্সড কনসেপ্ট

### ১. কম্বিনেশন মেমোইজেশন
```python
from functools import lru_cache

def combination_count_memoized(n, k):
    """
    কম্বিনেশন সংখ্যা গণনা - মেমোইজেশন সহ।
    """
    @lru_cache(maxsize=None)
    def C(n, k):
        if k == 0 or k == n:
            return 1
        return C(n-1, k-1) + C(n-1, k)
    
    return C(n, k)

# উদাহরণ
n, k = 10, 4
count = combination_count_memoized(n, k)
print(f"\nC({n}, {k}) = {count}")
print(f"গাণিতিকভাবে: {math.comb(n, k)}")
```

### ২. কম্বিনেশন ইটারেটর (মেমোরি ইফিসিয়েন্ট)
```python
class CombinationIterator:
    """
    কম্বিনেশন ইটারেটর - মেমোরি ইফিসিয়েন্ট।
    """
    def __init__(self, nums, k):
        self.nums = nums
        self.n = len(nums)
        self.k = k
        self.indices = list(range(k))
        self.first = True
    
    def has_next(self):
        return self.first or self.indices[0] < self.n - self.k
    
    def next(self):
        if self.first:
            self.first = False
        else:
            # পরবর্তী কম্বিনেশন খুঁজুন
            i = self.k - 1
            while i >= 0 and self.indices[i] == self.n - self.k + i:
                i -= 1
            
            if i < 0:
                return None
            
            self.indices[i] += 1
            for j in range(i + 1, self.k):
                self.indices[j] = self.indices[j-1] + 1
        
        return [self.nums[i] for i in self.indices]

# ব্যবহার
nums = ['A', 'B', 'C', 'D', 'E']
k = 3
iterator = CombinationIterator(nums, k)
print("\nকম্বিনেশন ইটারেটর:")
while iterator.has_next():
    print(f"  {iterator.next()}")
```

### ৩. গোল্ডবাখ কনজেকচার (যুগ্ম সংখ্যা)
```python
def goldbach_combinations(even_number, primes):
    """
    গোল্ডবাখ কনজেকচার: যুগ্ম সংখ্যাকে দুটি মৌলিক সংখ্যার যোগফল।
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # মৌলিক সংখ্যা জেনারেট (even_number এর কম)
    if not primes:
        primes = [i for i in range(2, even_number) if is_prime(i)]
    
    # কম্বিনেশন খুঁজুন
    result = []
    seen = set()
    
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] + primes[j] == even_number:
                pair = (primes[i], primes[j])
                if pair not in seen:
                    result.append(pair)
                    seen.add(pair)
    
    return result

# উদাহরণ
even_number = 20
primes = [2, 3, 5, 7, 11, 13, 17, 19]
goldbach_pairs = goldbach_combinations(even_number, primes)
print(f"\nগোল্ডবাখ কম্বিনেশন: {even_number} = ")
for pair in goldbach_pairs:
    print(f"  {pair[0]} + {pair[1]}")
```

### ৪. কম্বিনেশন প্রোবাবিলিটি
```python
def combination_probability(n, k, p_success):
    """
    দ্বিপদী বিন্যাসের সম্ভাব্যতা: C(n,k) * p^k * (1-p)^(n-k)
    """
    import math
    
    combinations = math.comb(n, k)
    probability = combinations * (p_success ** k) * ((1 - p_success) ** (n - k))
    
    return combinations, probability

# উদাহরণ
n, k = 10, 3  # ১০টি টসে ৩টি হেড
p = 0.5  # ফেয়ার কয়েন
combs, prob = combination_probability(n, k, p)
print(f"\nবাইনোমিয়াল ডিস্ট্রিবিউশন:")
print(f"C({n}, {k}) = {combs}")
print(f"P({k} successes in {n} trials) = {prob:.6f}")
print(f"শতকরা: {prob*100:.2f}%")
```

## ভিজ্যুয়ালাইজেশন
```python
def visualize_combinations(nums, k):
    """
    কম্বিনেশন ট্রি ভিজ্যুয়ালাইজেশন।
    """
    def backtrack_tree(start, path, level):
        if len(path) == k:
            print("  " * level + "✓ " + str(path))
            return
        
        for i in range(start, len(nums)):
            print("  " * level + f"→ {nums[i]}")
            path.append(nums[i])
            backtrack_tree(i + 1, path, level + 1)
            path.pop()
    
    print(f"{nums} থেকে {k} টি উপাদানের কম্বিনেশন ট্রি:")
    backtrack_tree(0, [], 0)

# ছোট উদাহরণ ভিজ্যুয়ালাইজ
nums_small = [1, 2, 3, 4]
k = 2
visualize_combinations(nums_small, k)
```

## উপকারিতা ও সীমাবদ্ধতা

### উপকারিতা:
1. অর্ডার বিবেচনা করে না (পারমুটেশনের চেয়ে কম সংখ্যা)
2. অনেক রিয়েল-লাইফ সমস্যার সাথে মিলে
3. বিভিন্ন অপটিমাইজেশন সম্ভব

### সীমাবদ্ধতা:
1. C(n,k) এক্সপোনেনশিয়াল হতে পারে
2. বড় n,k এর জন্য অনুপযুক্ত
3. মেমোরি ব্যয়বহুল

### অপটিমাইজেশন টিপস:
1. k > n/2 হলে C(n,k) = C(n,n-k) ব্যবহার করুন
2. ডুপ্লিকেট এড়াতে সর্ট করুন
3. জেনারেটর ব্যবহার করে মেমোরি সেভ করুন
4. প্রুনিং করে সার্চ স্পেস কমানো

## গাণিতিক সূত্র
```python
def combination_formulas():
    """কম্বিনেশনের বিভিন্ন গাণিতিক সূত্র"""
    
    print("\nকম্বিনেশনের গাণিতিক সূত্র:")
    print("1. C(n,k) = n! / (k! * (n-k)!)")
    print("2. C(n,k) = C(n,n-k)")
    print("3. C(n,0) = C(n,n) = 1")
    print("4. C(n,1) = n")
    print("5. C(n,k) = C(n-1,k-1) + C(n-1,k) (প্যাসকেলের আইন)")
    print("6. ∑ C(n,k) = 2^n (k=0 থেকে n)")
    
    # প্যাসকেলের ত্রিভুজ
    print("\nপ্যাসকেলের ত্রিভুজ (প্রথম ৫ সারি):")
    for n in range(5):
        row = [math.comb(n, k) for k in range(n+1)]
        print("  " * (5-n), end="")
        for num in row:
            print(f"{num:3}", end=" ")
        print()

combination_formulas()
```

## উপসংহার
কম্বিনেশন জেনারেশন হল কম্বিনেটরিক্সের একটি মৌলিক কনসেপ্ট যার বহু ব্যবহার আছে:
- **স্ট্যাটিসটিক্স**: স্যাম্পলিং, প্রোবাবিলিটি
- **ফাইন্যান্স**: ইনভেস্টমেন্ট পোর্টফোলিও
- **কম্পিউটার সায়েন্স**: অ্যালগরিদম ডিজাইন
- **গেম থিওরি**: কৌশল নির্বাচন
- **বায়োলজি**: জিন কম্বিনেশন

সঠিক পদ্ধতি নির্বাচন এবং অপটিমাইজেশনের মাধ্যমে বড় সমস্যাও দক্ষভাবে সমাধান করা সম্ভব।