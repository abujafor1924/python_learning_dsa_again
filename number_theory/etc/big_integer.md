# **বিগ ইন্টিজার: বিস্তারিত ও পাইথন বাস্তবায়ন**

## **১. বিগ ইন্টিজার কী?**

**বিগ ইন্টিজার** হলো এমন পূর্ণসংখ্যা যা স্ট্যান্ডার্ড ডাটা টাইপের (যেমন ৩২-বিট বা ৬৪-বিট) সীমা অতিক্রম করে। 

### **সাধারণ সীমা:**
- **৩২-বিট ইন্টিজার**: -২³¹ থেকে ২³¹-১ (-২১৪৭৪৮৩৬৪৮ থেকে ২১৪৭৪৮৩৬৪৭)
- **৬৪-বিট ইন্টিজার**: -২⁶³ থেকে ২⁶³-১ (-৯.২×১০¹⁸ থেকে ৯.২×১০¹৮)

**বিগ ইন্টিজার** এই সীমা ছাড়িয়ে যেতে পারে।

## **২. বিগ ইন্টিজারের প্রয়োজনীয়তা**

```python
# সাধারণ ইন্টিজারের সীমা
import sys
print(f"৩২-বিট ইন্টিজার সর্বোচ্চ: {2**31 - 1:,}")
print(f"৬৪-বিট ইন্টিজার সর্বোচ্চ: {2**63 - 1:,}")

# বিগ ইন্টিজারের উদাহরণ
big_num = 10**100  # 1 followed by 100 zeros
print(f"\nবিগ ইন্টিজার উদাহরণ (10^100):")
print(f"সংখ্যা: {big_num}")
print(f"অঙ্কের সংখ্যা: {len(str(big_num))}")
```

## **৩. বিগ ইন্টিজার প্রকাশের পদ্ধতি**

### **৩.১ অ্যারে ভিত্তিক পদ্ধতি**
```python
class BigInt:
    def __init__(self, num_str="0", base=10):
        self.digits = []  # LSD (Least Significant Digit) first
        self.base = base
        self.is_negative = False
        
        if num_str.startswith('-'):
            self.is_negative = True
            num_str = num_str[1:]
        
        # String থেকে অ্যারে তৈরি
        for char in reversed(num_str):
            if char.isdigit():
                self.digits.append(int(char))
            else:
                # A=10, B=11, ... Z=35
                self.digits.append(ord(char.upper()) - ord('A') + 10)
    
    def __str__(self):
        """বিগ ইন্টিজারকে স্ট্রিং হিসেবে ফেরত দেয়"""
        if not self.digits:
            return "0"
        
        result = []
        for digit in reversed(self.digits):
            if digit < 10:
                result.append(str(digit))
            else:
                result.append(chr(digit - 10 + ord('A')))
        
        num_str = ''.join(result).lstrip('0') or '0'
        return ('-' if self.is_negative else '') + num_str
    
    def __repr__(self):
        return f"BigInt('{self}')"
    
    def normalize(self):
        """অগ্রবর্তী শূন্য অপসারণ"""
        while len(self.digits) > 1 and self.digits[-1] == 0:
            self.digits.pop()
        if not self.digits:
            self.digits.append(0)
            self.is_negative = False
    
    def copy(self):
        """কপি তৈরি"""
        new_bigint = BigInt()
        new_bigint.digits = self.digits.copy()
        new_bigint.base = self.base
        new_bigint.is_negative = self.is_negative
        return new_bigint

# উদাহরণ
num1 = BigInt("123456789012345678901234567890")
print(f"বিগ ইন্টিজার ১: {num1}")
print(f"অঙ্কের তালিকা (LSD first): {num1.digits}")
```

## **৪. গাণিতিক ক্রিয়াকলাপ**

### **৪.১ যোগ**
```python
def bigint_add(a, b):
    """দুইটি বিগ ইন্টিজার যোগ"""
    # চিহ্ন সমান করা
    if a.is_negative == b.is_negative:
        result = _add_absolute(a, b)
        result.is_negative = a.is_negative
    else:
        # বড়টি খুঁজে বের করা
        cmp = _compare_absolute(a, b)
        if cmp >= 0:
            result = _subtract_absolute(a, b)
            result.is_negative = a.is_negative
        else:
            result = _subtract_absolute(b, a)
            result.is_negative = b.is_negative
    
    result.normalize()
    return result

def _add_absolute(a, b):
    """পরম মানের যোগ"""
    result = BigInt()
    result.digits = []
    
    max_len = max(len(a.digits), len(b.digits))
    carry = 0
    
    for i in range(max_len):
        digit_a = a.digits[i] if i < len(a.digits) else 0
        digit_b = b.digits[i] if i < len(b.digits) else 0
        
        total = digit_a + digit_b + carry
        result.digits.append(total % a.base)
        carry = total // a.base
    
    if carry:
        result.digits.append(carry)
    
    return result

# যোগের উদাহরণ
num1 = BigInt("99999999999999999999")
num2 = BigInt("1")
sum_result = bigint_add(num1, num2)
print(f"{num1} + {num2} = {sum_result}")
```

### **৪.২ বিয়োগ**
```python
def _subtract_absolute(a, b):
    """পরম মানের বিয়োগ (a >= b ধরে)"""
    result = BigInt()
    result.digits = []
    
    borrow = 0
    
    for i in range(len(a.digits)):
        digit_a = a.digits[i]
        digit_b = b.digits[i] if i < len(b.digits) else 0
        
        # ধার বাবদ বিয়োগ
        digit_a -= borrow
        borrow = 0
        
        if digit_a < digit_b:
            digit_a += a.base
            borrow = 1
        
        result.digits.append(digit_a - digit_b)
    
    result.normalize()
    return result

def bigint_subtract(a, b):
    """বিগ ইন্টিজার বিয়োগ"""
    # b এর চিহ্ন পরিবর্তন করে যোগের মতো করা
    b_copy = b.copy()
    b_copy.is_negative = not b_copy.is_negative
    return bigint_add(a, b_copy)

# বিয়োগের উদাহরণ
num1 = BigInt("100000000000000000000")
num2 = BigInt("1")
diff_result = bigint_subtract(num1, num2)
print(f"{num1} - {num2} = {diff_result}")
```

### **৪.৩ গুণ**
```python
def bigint_multiply(a, b):
    """বিগ ইন্টিজার গুণ (বেসিক স্কুল পদ্ধতি)"""
    result = BigInt("0")
    result.digits = [0] * (len(a.digits) + len(b.digits) + 1)
    
    for i in range(len(a.digits)):
        carry = 0
        for j in range(len(b.digits)):
            product = a.digits[i] * b.digits[j] + result.digits[i+j] + carry
            result.digits[i+j] = product % a.base
            carry = product // a.base
        
        # শেষ ক্যারি
        if carry:
            result.digits[i + len(b.digits)] += carry
    
    # চিহ্ন নির্ধারণ
    result.is_negative = a.is_negative ^ b.is_negative  # XOR
    result.normalize()
    return result

# গুণের উদাহরণ
num1 = BigInt("123456789")
num2 = BigInt("987654321")
prod_result = bigint_multiply(num1, num2)
print(f"{num1} × {num2} = {prod_result}")
```

## **৫. উন্নত গুণের অ্যালগোরিদম**

### **৫.১ কারাতসুবা অ্যালগোরিদম**
```python
def karatsuba_multiply(x, y, base=10):
    """কারাতসুবা অ্যালগোরিদম - O(n^log2(3))"""
    
    def split_number(num, m):
        """সংখ্যাকে দুই ভাগে ভাগ"""
        high = num // (base ** m)
        low = num % (base ** m)
        return high, low
    
    # Base case
    if x < 1000 or y < 1000:
        return x * y
    
    # n = max(digits(x), digits(y))
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    x_high, x_low = split_number(x, m)
    y_high, y_low = split_number(y, m)
    
    # তিনটি রিকার্সিভ গুণ
    z0 = karatsuba_multiply(x_low, y_low, base)
    z1 = karatsuba_multiply((x_low + x_high), (y_low + y_high), base)
    z2 = karatsuba_multiply(x_high, y_high, base)
    
    # কারাতসুবা সূত্র প্রয়োগ
    return (z2 * (base ** (2*m)) + 
            (z1 - z2 - z0) * (base ** m) + 
            z0)

# কারাতসুবা ব্যবহারের উদাহরণ
import time

x = 12345678901234567890
y = 98765432109876543210

start = time.time()
result_karatsuba = karatsuba_multiply(x, y)
time_karatsuba = time.time() - start

start = time.time()
result_normal = x * y
time_normal = time.time() - start

print(f"কারাতসুবা সময়: {time_karatsuba:.6f} সেকেন্ড")
print(f"সাধারণ গুণের সময়: {time_normal:.6f} সেকেন্ড")
print(f"ফলাফল মিলছে: {result_karatsuba == result_normal}")
```

## **৬. ভাগ এবং মডুলো**

```python
def bigint_divide(dividend, divisor):
    """বিগ ইন্টিজার ভাগ (বেসিক লং ডিভিশন)"""
    if all(d == 0 for d in divisor.digits):
        raise ZeroDivisionError("শূন্য দ্বারা ভাগ")
    
    # পরম মান নেওয়া
    abs_dividend = dividend.copy()
    abs_dividend.is_negative = False
    abs_divisor = divisor.copy()
    abs_divisor.is_negative = False
    
    quotient = BigInt("0")
    remainder = BigInt("0")
    
    # LSD থেকে MSD এ যাওয়া (উল্টা দিকে)
    for i in range(len(abs_dividend.digits)-1, -1, -1):
        # remainder কে shift left করা
        remainder.digits.insert(0, abs_dividend.digits[i])
        remainder.normalize()
        
        # quotient digit খোঁজা
        q_digit = 0
        while _compare_absolute(remainder, abs_divisor) >= 0:
            remainder = _subtract_absolute(remainder, abs_divisor)
            q_digit += 1
        
        # quotient update
        quotient.digits.insert(0, q_digit)
    
    quotient.normalize()
    
    # চিহ্ন নির্ধারণ
    quotient.is_negative = dividend.is_negative ^ divisor.is_negative
    remainder.is_negative = dividend.is_negative
    
    return quotient, remainder

# ভাগের উদাহরণ
dividend = BigInt("12345678901234567890")
divisor = BigInt("12345")
quotient, remainder = bigint_divide(dividend, divisor)
print(f"{dividend} ÷ {divisor} = {quotient}")
print(f"ভাগশেষ: {remainder}")
```

## **৭. পাওয়ার এবং মডুলার এক্সপোনেন্টিয়েশন**

```python
def bigint_pow(base, exponent):
    """বিগ ইন্টিজার পাওয়ার (বাইনারি এক্সপোনেন্টিয়েশন)"""
    result = BigInt("1")
    current = base.copy()
    exp = exponent.copy()
    
    while not all(d == 0 for d in exp.digits):
        # যদি LSB 1 হয়
        if exp.digits[0] % 2 == 1:
            result = bigint_multiply(result, current)
        
        # current = current * current
        current = bigint_multiply(current, current)
        
        # exponent = exponent // 2
        exp, _ = bigint_divide(exp, BigInt("2"))
    
    return result

def modular_exponentiation(base, exponent, modulus):
    """মডুলার এক্সপোনেন্টিয়েশন"""
    result = BigInt("1")
    base = base.copy()
    exp = exponent.copy()
    
    base, _ = bigint_divide(base, modulus)
    
    while not all(d == 0 for d in exp.digits):
        if exp.digits[0] % 2 == 1:
            temp = bigint_multiply(result, base)
            result, _ = bigint_divide(temp, modulus)
        
        temp = bigint_multiply(base, base)
        base, _ = bigint_divide(temp, modulus)
        
        exp, _ = bigint_divide(exp, BigInt("2"))
    
    return result

# মডুলার এক্সপোনেন্টিয়েশন উদাহরণ
base = BigInt("3")
exponent = BigInt("100")
modulus = BigInt("7")
result = modular_exponentiation(base, exponent, modulus)
print(f"{base}^{exponent} mod {modulus} = {result}")
```

## **৮. পাইথনে বিল্ট-ইন বিগ ইন্টিজার**

```python
# পাইথন স্বয়ংক্রিয়ভাবে বিগ ইন্টিজার সাপোর্ট করে
print("\nপাইথনের বিল্ট-ইন বিগ ইন্টিজার:")
print("=" * 50)

# বড় সংখ্যার উদাহরণ
huge_number = 2**1000
print(f"2^1000 = {huge_number}")
print(f"অঙ্কের সংখ্যা: {len(str(huge_number))}")

# অপারেশন
a = 10**100  # 1 followed by 100 zeros
b = 10**50   # 1 followed by 50 zeros

print(f"\n10^100 + 10^50 = {a + b}")
print(f"10^100 × 10^50 = {a * b}")
print(f"10^100 ÷ 10^50 = {a // b}")
print(f"10^100 mod 10^50 = {a % b}")
```

## **৯. প্রাইম টেস্টিং (বিগ ইন্টিজারের জন্য)**

```python
def is_probable_prime(n, k=5):
    """মিলার-রবিন প্রাইমালিটি টেস্ট"""
    import random
    
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    
    # n-1 = d * 2^s
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    
    # k বার টেস্ট
    for _ in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)  # মডুলার এক্সপোনেন্টিয়েশন
        
        if x == 1 or x == n-1:
            continue
        
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    
    return True

# প্রাইম টেস্টিং উদাহরণ
test_numbers = [
    2**31 - 1,          # একটি মার্সেন প্রাইম
    10**50 + 235,       # ৫০ অঙ্কের সংখ্যা
    99999999999999999999999999999999999999999999999991  # একটি বড় প্রাইম
]

print("\nপ্রাইমালিটি টেস্ট:")
for num in test_numbers:
    prime = is_probable_prime(num)
    print(f"{num}\n→ প্রাইম? {prime}\n")
```

## **১০. RSA এনক্রিপশনে বিগ ইন্টিজার**

```python
def simple_rsa_demo():
    """সরল RSA এনক্রিপশন ডেমো"""
    import random
    import math
    
    # দুটি বড় মৌলিক সংখ্যা
    p = 61  # বাস্তবে অনেক বড় হবে (১০০+ অঙ্ক)
    q = 53
    
    n = p * q
    phi = (p-1) * (q-1)
    
    # e বাছাই (1 < e < phi, gcd(e, phi) = 1)
    e = 17
    
    # d বাছাই (e*d ≡ 1 mod phi)
    d = pow(e, -1, phi)  # Python 3.8+
    
    print(f"RSA প্যারামিটার:")
    print(f"p = {p}, q = {q}")
    print(f"n = p*q = {n}")
    print(f"φ(n) = (p-1)*(q-1) = {phi}")
    print(f"e = {e}")
    print(f"d = {d}")
    
    # মেসেজ এনক্রিপ্ট/ডিক্রিপ্ট
    message = 42
    encrypted = pow(message, e, n)
    decrypted = pow(encrypted, d, n)
    
    print(f"\nমেসেজ: {message}")
    print(f"এনক্রিপ্টেড: {encrypted}")
    print(f"ডিক্রিপ্টেড: {decrypted}")
    print(f"মিলছে? {message == decrypted}")

simple_rsa_demo()
```

## **১১. পারফরম্যান্স অপটিমাইজেশন**

```python
def benchmark_bigint_operations():
    """বিগ ইন্টিজার অপারেশনের বেঞ্চমার্ক"""
    import time
    
    # বিভিন্ন সাইজের সংখ্যা
    sizes = [10, 100, 1000, 5000]  # অঙ্কের সংখ্যা
    base = 10
    
    print("\nবেঞ্চমার্ক রেজাল্ট:")
    print("অঙ্ক সংখ্যা | গুণের সময় | ভাগের সময়")
    print("-" * 45)
    
    for size in sizes:
        # এলোমেলো সংখ্যা তৈরি
        num1_str = ''.join(str(random.randint(0, 9)) for _ in range(size))
        num2_str = ''.join(str(random.randint(0, 9)) for _ in range(size//2))
        
        num1 = BigInt(num1_str, base)
        num2 = BigInt(num2_str, base)
        
        # গুণের সময়
        start = time.time()
        _ = bigint_multiply(num1, num2)
        mul_time = time.time() - start
        
        # ভাগের সময়
        start = time.time()
        _, _ = bigint_divide(num1, num2)
        div_time = time.time() - start
        
        print(f"{size:10} | {mul_time:8.4f}s | {div_time:8.4f}s")

# benchmark_bigint_operations()
```

## **১২. ব্যবহারিক প্রয়োগ**

```python
def factorial_bigint(n):
    """বিগ ইন্টিজার ব্যবহার করে ফ্যাক্টোরিয়াল"""
    result = BigInt("1")
    for i in range(2, n+1):
        result = bigint_multiply(result, BigInt(str(i)))
    return result

def fibonacci_bigint(n):
    """বিগ ইন্টিজার ব্যবহার করে ফিবোনাচি"""
    if n <= 0:
        return BigInt("0")
    elif n == 1:
        return BigInt("1")
    
    a, b = BigInt("0"), BigInt("1")
    for _ in range(2, n+1):
        a, b = b, bigint_add(a, b)
    return b

# ব্যবহারিক উদাহরণ
print("\nব্যবহারিক উদাহরণ:")
print("100! এর শেষ ২০টি অঙ্ক:", str(factorial_bigint(100))[-20:])
print("1000তম ফিবোনাচি সংখ্যার অঙ্ক সংখ্যা:", len(str(fibonacci_bigint(1000))))
```

## **১৩. গুরুত্বপূর্ণ টিপস**

1. **মেমরি ম্যানেজমেন্ট**: বিগ ইন্টিজার বড় হলে মেমরি ব্যবহার বেশি হয়
2. **অপারেশন কমপ্লেক্সিটি**:
   - যোগ/বিয়োগ: O(n)
   - গুণ (সাধারণ): O(n²)
   - গুণ (কারাতসুবা): O(n^log₂3) ≈ O(n¹.⁵⁸)
   - ভাগ: O(n²)
3. **অপটিমাইজেশন**:
   - বেস বড় করলে মেমরি কম লাগে কিন্তু অপারেশন জটিল হয়
   - বিট-লেভেল অপারেশন দ্রুততর
4. **লাইব্রেরি ব্যবহার**: বাস্তব প্রয়োগে GMP (GNU Multiple Precision) বা Python's built-in bigint ব্যবহার করুন

## **১৪. চ্যালেঞ্জ সমস্যা**

```python
def challenge_problems():
    """বিগ ইন্টিজার সম্পর্কিত চ্যালেঞ্জ"""
    
    # 1. Collatz conjecture for big numbers
    def collatz_steps(n):
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            steps += 1
        return steps
    
    # 2. Perfect number check
    def is_perfect_number(n):
        # Only works for smallish numbers
        divisors_sum = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors_sum += i
                if i != n // i:
                    divisors_sum += n // i
        return divisors_sum == n
    
    print("চ্যালেঞ্জ:")
    print("1. Collatz(2^100):", collatz_steps(2**100))
    print("2. Perfect number check (28):", is_perfect_number(28))

challenge_problems()
```

এই বিস্তারিত গাইডে বিগ ইন্টিজারের মৌলিক ধারণা থেকে শুরু করে উন্নত অ্যালগোরিদম এবং ব্যবহারিক প্রয়োগ সবই কভার করা হয়েছে। পাইথনে এটি বিল্ট-ইন ফিচার হলেও বোঝার জন্য কাস্টম ইমপ্লিমেন্টেশন গুরুত্বপূর্ণ।