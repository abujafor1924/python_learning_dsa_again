# রিকার্শন ফাংশন বাংলায় ব্যাখ্যা

## ১. রিকার্শন কী? (Recursion)

**রিকার্শন** হলো এমন একটি প্রক্রিয়া যেখানে একটি ফাংশন নিজেকে নিজে কল করে। রিকার্শনে দুইটি জিনিস গুরুত্বপূর্ণ:
1. **Base Case** - যেখানে রিকার্শন থামে
2. **Recursive Case** - যেখানে ফাংশন নিজেকে কল করে

### সাধারণ স্ট্রাকচার:
```python
def recursive_function(parameters):
    # ১. Base Case (থামার শর্ত)
    if stopping_condition:
        return base_value
    
    # ২. Recursive Case (নিজেকে কল)
    return recursive_function(modified_parameters)
```

## ২. সাধারণ উদাহরণ

### উদাহরণ ১: ফ্যাক্টোরিয়াল বের করা
```
5! = 5 × 4 × 3 × 2 × 1 = 120
n! = n × (n-1)!
```

```python
def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    
    # Recursive Case
    return n * factorial(n - 1)

# টেস্ট
print(factorial(5))  # Output: 120
print(factorial(4))  # Output: 24
```

**কার্যপ্রণালী:**
```
factorial(5)
= 5 × factorial(4)
= 5 × 4 × factorial(3)
= 5 × 4 × 3 × factorial(2)
= 5 × 4 × 3 × 2 × factorial(1)
= 5 × 4 × 3 × 2 × 1
= 120
```

### উদাহরণ ২: ফিবোনাচি সিকোয়েন্স
```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
```

```python
def fibonacci(n):
    # Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive Case
    return fibonacci(n-1) + fibonacci(n-2)

# টেস্ট
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
    
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

## ৩. রিকার্শনের প্রকারভেদ

### ১. ডাইরেক্ট রিকার্শন
ফাংশন সরাসরি নিজেকে কল করে।

```python
# উদাহরণ: সংখ্যার যোগফল ১ থেকে n পর্যন্ত
def sum_n(n):
    if n == 1:  # Base Case
        return 1
    return n + sum_n(n-1)  # Direct Recursion

print(sum_n(5))  # Output: 15 (1+2+3+4+5)
```

### ২. ইন্ডাইরেক্ট রিকার্শন
ফাংশন অন্য ফাংশনের মাধ্যমে নিজেকে কল করে।

```python
def function_A(n):
    if n <= 0:
        return
    print(f"A: {n}")
    function_B(n-1)  # অন্য ফাংশন কল

def function_B(n):
    if n <= 0:
        return
    print(f"B: {n}")
    function_A(n-1)  # আবার প্রথম ফাংশন কল

function_A(5)
# Output: A:5, B:4, A:3, B:2, A:1
```

## ৪. মেমোইজেশন সহ রিকার্শন

রিকার্শন অনেক সময় একই ভ্যালু বারবার ক্যালকুলেট করে। এটা প্রতিরোধ করার জন্য মেমোইজেশন ব্যবহার করা হয়।

```python
# ফিবোনাচি without মেমোইজেশন (Slow)
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n-1) + fib_slow(n-2)

# ফিবোনাচি with মেমোইজেশন (Fast)
def fib_fast(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_fast(n-1, memo) + fib_fast(n-2, memo)
    return memo[n]

# টেস্ট
import time

start = time.time()
print(fib_slow(35))  # অনেক সময় নিবে
end = time.time()
print(f"Slow: {end-start:.2f} seconds")

start = time.time()
print(fib_fast(100))  # খুব দ্রুত
end = time.time()
print(f"Fast: {end-start:.2f} seconds")
```

## ৫. রিয়েল-লাইফ উদাহরণ

### উদাহরণ ১: ফাইল সিস্টেম ট্রাভার্সাল
```python
import os

def list_files(start_path):
    """রিকার্সিভলি সব ফাইল লিস্ট করা"""
    for item in os.listdir(start_path):
        item_path = os.path.join(start_path, item)
        
        if os.path.isdir(item_path):  # যদি ডিরেক্টরি হয়
            print(f"Directory: {item_path}")
            list_files(item_path)  # রিকার্সিভ কল
        else:  # যদি ফাইল হয়
            print(f"File: {item_path}")

# ব্যবহার
list_files(".")
```

### উদাহরণ ২: পাওয়ার ক্যালকুলেশন
```python
def power(base, exp):
    """base^exp রিকার্সিভলি বের করা"""
    # Base Cases
    if exp == 0:
        return 1
    if exp == 1:
        return base
    
    # Recursive Cases
    if exp % 2 == 0:  # Even exponent
        half_power = power(base, exp//2)
        return half_power * half_power
    else:  # Odd exponent
        return base * power(base, exp-1)

print(power(2, 5))  # Output: 32
print(power(3, 4))  # Output: 81
```

### উদাহরণ ৩: প্যালিনড্রোম চেক
```python
def is_palindrome(s):
    """রিকার্সিভলি প্যালিনড্রোম চেক"""
    # Base Cases
    if len(s) <= 1:
        return True
    
    # Recursive Case
    if s[0] == s[-1]:  # প্রথম ও শেষ অক্ষর মিললে
        return is_palindrome(s[1:-1])  # মাঝের অংশ চেক
    else:
        return False

print(is_palindrome("madam"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
```

## ৬. রিকার্শনের সুবিধা ও অসুবিধা

### সুবিধা:
1. **কোড সহজ ও পড়তে সুন্দর** হয়
2. **কমপ্লেক্স প্রোবলেম** সহজে সলভ করা যায়
3. **ট্রি-লাইক স্ট্রাকচার** এর জন্য পারফেক্ট

### অসুবিধা:
1. **স্ট্যাক ওভারফ্লো** হতে পারে
2. **ইটারেটিভ সল্যুশন** থেকে স্লো হতে পারে
3. **ডিবাগ করা** কঠিন হতে পারে

## ৭. রিকার্শন vs ইটারেশন

### রিকার্শন ব্যবহার করবো কখন?
1. যখন প্রোবলেম রিকার্সিভভাবে ডিফাইন করা যায়
2. ট্রি বা গ্রাফ ট্রাভার্সাল করতে
3. ডিভাইড এন্ড কনকোয়ার অ্যালগরিদমে

### ইটারেশন ব্যবহার করবো কখন?
1. যখন সিম্পল লুপ দিয়ে সল্ভ করা যায়
2. যখন মেমোরি কনসার্ন আছে
3. যখন পারফরমেন্স ক্রিটিক্যাল

```python
# রিকার্সিভ vs ইটারেটিভ ফ্যাক্টোরিয়াল
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# দুটোই একই আউটপুট দিবে
print(factorial_recursive(5))  # 120
print(factorial_iterative(5))  # 120
```

## ৮. কমন মিসটেকস ও সল্যুশন

### সমস্যা ১: Base Case ভুলে যাওয়া
```python
# ❌ ভুল: No Base Case
def wrong_recursion(n):
    return n + wrong_recursion(n-1)  # Infinite recursion!

# ✅ সঠিক:
def correct_recursion(n):
    if n <= 0:  # Base Case
        return 0
    return n + correct_recursion(n-1)
```

### সমস্যা ২: স্ট্যাক ওভারফ্লো
```python
# ❌ বড় সংখ্যার জন্য বিপদ
# print(factorial_recursive(10000))  # RecursionError

# ✅ Tail Recursion অপ্টিমাইজেশন
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n-1, n * accumulator)
```

## ৯. প্র্যাকটিস প্রোবলেম

### সহজ প্রোবলেম:
1. **১ থেকে n পর্যন্ত যোগফল** বের করুন
2. **অ্যারে রিভার্স** করুন
3. **বাইনারী সার্চ** ইমপ্লিমেন্ট করুন

### মধ্যম প্রোবলেম:
1. **টাওয়ার অফ হ্যানয়** সল্ভ করুন
2. **সব সাবসেট** জেনারেট করুন
3. **পারমুটেশন** জেনারেট করুন

### কঠিন প্রোবলেম:
1. **N-কুইন্স প্রোবলেম**
2. **সাডোকু সল্ভার**
3. **ম্যাজ ট্রাভার্সাল**

## ১০. টিপস ফর বেগিনার্স

1. **সবসময় Base Case লিখুন প্রথমে**
2. **ছোট ইনপুট দিয়ে টেস্ট করুন**
3. **রিকার্শন ট্রি আঁকতে শিখুন**
4. **প্রিন্ট স্টেটমেন্ট** যোগ করে ডিবাগ করুন

```python
# ডিবাগিং এর জন্য
def factorial_debug(n, depth=0):
    indent = "  " * depth
    print(f"{indent}Calling factorial({n})")
    
    if n <= 1:
        print(f"{indent}Returning 1")
        return 1
    
    result = n * factorial_debug(n-1, depth+1)
    print(f"{indent}Returning {result}")
    return result

print(factorial_debug(4))
```

## সারসংক্ষেপ:
- **রিকার্শন** = নিজেকে কল করা
- **Base Case** = থামার শর্ত
- **Recursive Case** = সমস্যা ছোট করা
- **মেমোইজেশন** = পারফরমেন্স উন্নত করা
- **প্র্যাকটিস** = পারফেক্ট করা

**শুরু করুন ছোট প্রোগ্রাম দিয়ে এবং ধীরে ধীরে কমপ্লেক্স প্রোবলেমে যান!**