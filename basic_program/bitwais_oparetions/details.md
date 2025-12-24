# বিটওয়াইজ অপারেশন বাংলায় বিস্তারিত ব্যাখ্যা

## ১. বিটওয়াইজ অপারেশন কী?

**বিটওয়াইজ অপারেশন** হলো এমন অপারেশন যেগুলো ডাটার বিট লেভেলে কাজ করে। প্রতিটি ইন্টিজার কম্পিউটারে **বাইনারি ফরম্যাটে** সংরক্ষিত থাকে এবং বিটওয়াইজ অপারেশন সরাসরি সেই বিটগুলোর উপর কাজ করে।

### বাইনারি রিপ্রেজেন্টেশন:
```python
# ডেসিমেল থেকে বাইনারি
print(bin(5))      # 0b101
print(bin(3))      # 0b011
print(bin(10))     # 0b1010
```

## ২. বিটওয়াইজ অপারেটরদের তালিকা

| অপারেটর | নাম | বর্ণনা | উদাহরণ |
|---------|------|---------|---------|
| `&` | AND | দুটি বিটই 1 হলে 1 | `5 & 3 = 1` |
| `|` | OR | যেকোনো একটি বিট 1 হলে 1 | `5 | 3 = 7` |
| `^` | XOR | দুটি বিট ভিন্ন হলে 1 | `5 ^ 3 = 6` |
| `~` | NOT | বিট উল্টিয়ে দেয় | `~5 = -6` |
| `<<` | Left Shift | বিট বামে শিফট | `5 << 1 = 10` |
| `>>` | Right Shift | বিট ডানে শিফট | `5 >> 1 = 2` |

## ৩. বিস্তারিত ব্যাখ্যা উদাহরণ সহ

### ১. AND অপারেটর (`&`)
**Rule:** দুটি বিটই 1 হলে 1, নাহলে 0

```python
# 5 = 101 (বাইনারি)
# 3 = 011 (বাইনারি)
# -------------
#     001 = 1 (ডেসিমেল)

a = 5    # 0101
b = 3    # 0011
result = a & b  # 0001 = 1
print(f"5 & 3 = {result}")  # Output: 1
print(f"Binary: {bin(a)} & {bin(b)} = {bin(result)}")
```

**Truth Table:**
```
A | B | A & B
0   0     0
0   1     0
1   0     0
1   1     1
```

**প্র্যাকটিক্যাল ইউস:**
- নির্দিষ্ট বিট চেক করা
- প্যারিটি চেক
- ফ্লাগ চেক করা

```python
# নির্দিষ্ট বিট চেক
def check_bit(num, bit_position):
    mask = 1 << bit_position
    return (num & mask) != 0

num = 13  # 1101
print(f"Is bit 0 set in {num}? {check_bit(num, 0)}")  # True (1)
print(f"Is bit 1 set in {num}? {check_bit(num, 1)}")  # False (0)
print(f"Is bit 2 set in {num}? {check_bit(num, 2)}")  # True (4)
print(f"Is bit 3 set in {num}? {check_bit(num, 3)}")  # True (8)
```

### ২. OR অপারেটর (`|`)
**Rule:** যেকোনো একটি বিট 1 হলে 1

```python
# 5 = 101
# 3 = 011
# -------------
#     111 = 7

a = 5    # 0101
b = 3    # 0011
result = a | b  # 0111 = 7
print(f"5 | 3 = {result}")  # Output: 7
```

**Truth Table:**
```
A | B | A | B
0   0     0
0   1     1
1   0     1
1   1     1
```

**প্র্যাকটিক্যাল ইউস:**
- বিট সেট করা
- মাল্টিপল ফ্লাগ কম্বাইন করা

```python
# বিট সেট করা
def set_bit(num, bit_position):
    mask = 1 << bit_position
    return num | mask

num = 8  # 1000
print(f"Set bit 1: {set_bit(num, 1)}")  # 1010 = 10
print(f"Set bit 2: {set_bit(num, 2)}")  # 1100 = 12
```

### ৩. XOR অপারেটর (`^`)
**Rule:** দুটি বিট ভিন্ন হলে 1, সমান হলে 0

```python
# 5 = 101
# 3 = 011
# -------------
#     110 = 6

a = 5    # 0101
b = 3    # 0011
result = a ^ b  # 0110 = 6
print(f"5 ^ 3 = {result}")  # Output: 6
```

**Truth Table:**
```
A | B | A ^ B
0   0     0
0   1     1
1   0     1
1   1     0
```

**প্র্যাকটিক্যাল ইউস:**
- দুটি সংখ্যা swap করা
- এনক্রিপশন
- প্যারিটি চেক

```python
# দুটি ভেরিয়েবল swap (বিনা থার্ড ভেরিয়েবলের)
a = 5
b = 3
print(f"Before swap: a={a}, b={b}")

a = a ^ b
b = a ^ b
a = a ^ b

print(f"After swap: a={a}, b={b}")  # a=3, b=5

# XOR এর মজার বৈশিষ্ট্য
x = 7
print(f"x ^ x = {x ^ x}")  # 0
print(f"x ^ 0 = {x ^ 0}")  # x
print(f"x ^ y ^ y = {x ^ 5 ^ 5}")  # x
```

### ৪. NOT অপারেটর (`~`)
**Rule:** প্রতিটি বিট উল্টিয়ে দেয় (1→0, 0→1)

```python
# 5 = 00000101
# ~5 = 11111010 = -6 (Two's complement)

a = 5
result = ~a
print(f"~5 = {result}")  # Output: -6
print(f"Binary 5: {bin(a)}")
print(f"Binary ~5: {bin(result & 0b1111)}")  # Mask for 4 bits
```

**টু'স কমপ্লিমেন্ট বোঝা:**
```python
# Positive to Negative (8-bit example)
# 5 = 00000101
# One's complement: 11111010
# Two's complement (add 1): 11111011 = -5

def show_twos_complement(num, bits=8):
    if num >= 0:
        return bin(num)
    else:
        # Calculate two's complement
        positive = -num
        complement = ((1 << bits) - positive) & ((1 << bits) - 1)
        return bin(complement)

print(show_twos_complement(5, 8))   # 0b101
print(show_twos_complement(-5, 8))  # 0b11111011
```

### ৫. Left Shift অপারেটর (`<<`)
**Rule:** বিটগুলো বামে শিফট করে, ডানে ০ যোগ করে

```python
# 5 = 101
# 5 << 1 = 1010 = 10
# 5 << 2 = 10100 = 20

a = 5
print(f"5 << 1 = {a << 1}")  # 10
print(f"5 << 2 = {a << 2}")  # 20
print(f"5 << 3 = {a << 3}")  # 40

# গাণিতিকভাবে: n << m = n × 2^m
print(f"7 << 3 = {7 << 3}")  # 7 × 8 = 56
```

**প্র্যাকটিক্যাল ইউস:**
- দ্রুত ২ এর পাওয়ার দিয়ে গুণ
- নির্দিষ্ট বিটে সেট করা

```python
# পাওয়ার অফ টু চেক
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(16))  # True
print(is_power_of_two(15))  # False

# দ্রুত গুণ
def multiply_by_power_of_two(num, power):
    return num << power

print(f"7 × 8 = {multiply_by_power_of_two(7, 3)}")  # 56
print(f"3 × 16 = {multiply_by_power_of_two(3, 4)}")  # 48
```

### ৬. Right Shift অপারেটর (`>>`)
**Rule:** বিটগুলো ডানে শিফট করে

```python
# 5 = 101
# 5 >> 1 = 010 = 2
# 5 >> 2 = 001 = 1

a = 16
print(f"16 >> 1 = {a >> 1}")  # 8
print(f"16 >> 2 = {a >> 2}")  # 4
print(f"16 >> 3 = {a >> 3}")  # 2

# গাণিতিকভাবে: n >> m = n // 2^m
print(f"29 >> 2 = {29 >> 2}")  # 29 // 4 = 7
```

**প্র্যাকটিক্যাল ইউস:**
- দ্রুত ২ এর পাওয়ার দিয়ে ভাগ
- বিট রিমুভ করা

```python
# দ্রুত ভাগ (ইন্টিজার ডিভিশন)
def divide_by_power_of_two(num, power):
    return num >> power

print(f"29 / 4 = {divide_by_power_of_two(29, 2)}")  # 7
print(f"64 / 8 = {divide_by_power_of_two(64, 3)}")  # 8

# বিট এক্সট্রাক্ট করা
def extract_bits(num, start_bit, num_bits):
    mask = ((1 << num_bits) - 1) << start_bit
    return (num & mask) >> start_bit

num = 0b11011010  # 218
print(f"Bits 2-4: {extract_bits(num, 2, 3)}")  # 110 = 6
```

## ৪. রিয়েল-লাইফ অ্যাপ্লিকেশন

### ১. ফ্লাগ ম্যানেজমেন্ট
```python
# ফ্লাগ ডেফাইন
READ_PERMISSION = 1    # 0001
WRITE_PERMISSION = 2   # 0010
EXECUTE_PERMISSION = 4 # 0100
DELETE_PERMISSION = 8  # 1000

class FilePermissions:
    def __init__(self):
        self.permissions = 0
    
    def add_permission(self, permission):
        self.permissions |= permission
    
    def remove_permission(self, permission):
        self.permissions &= ~permission
    
    def has_permission(self, permission):
        return (self.permissions & permission) != 0
    
    def toggle_permission(self, permission):
        self.permissions ^= permission
    
    def __str__(self):
        perms = []
        if self.has_permission(READ_PERMISSION):
            perms.append("Read")
        if self.has_permission(WRITE_PERMISSION):
            perms.append("Write")
        if self.has_permission(EXECUTE_PERMISSION):
            perms.append("Execute")
        if self.has_permission(DELETE_PERMISSION):
            perms.append("Delete")
        return f"Permissions: {', '.join(perms)}"

# টেস্ট
file = FilePermissions()
file.add_permission(READ_PERMISSION)
file.add_permission(WRITE_PERMISSION)
print(file)  # Permissions: Read, Write

file.toggle_permission(WRITE_PERMISSION)
print(file)  # Permissions: Read

file.add_permission(EXECUTE_PERMISSION | DELETE_PERMISSION)
print(file)  # Permissions: Read, Execute, Delete
```

### ২. কোলর রিপ্রেজেন্টেশন (RGB)
```python
def rgb_to_int(red, green, blue, alpha=255):
    """RGB থেকে 32-bit integer"""
    return (alpha << 24) | (red << 16) | (green << 8) | blue

def int_to_rgb(color_int):
    """32-bit integer থেকে RGB"""
    alpha = (color_int >> 24) & 0xFF
    red = (color_int >> 16) & 0xFF
    green = (color_int >> 8) & 0xFF
    blue = color_int & 0xFF
    return red, green, blue, alpha

# টেস্ট
color = rgb_to_int(255, 0, 128)  # Red=255, Green=0, Blue=128
print(f"Color as integer: {color}")
print(f"Color as hex: {hex(color)}")

r, g, b, a = int_to_rgb(color)
print(f"RGB from integer: R={r}, G={g}, B={b}, A={a}")
```

### ৩. এনক্রিপশন
```python
def simple_xor_encrypt(text, key):
    """সিম্পল XOR এনক্রিপশন"""
    encrypted = []
    for char in text:
        encrypted.append(ord(char) ^ key)
    return encrypted

def simple_xor_decrypt(encrypted, key):
    """সিম্পল XOR ডিক্রিপশন"""
    decrypted = []
    for num in encrypted:
        decrypted.append(chr(num ^ key))
    return ''.join(decrypted)

# টেস্ট
message = "Hello"
key = 42
encrypted = simple_xor_encrypt(message, key)
print(f"Encrypted: {encrypted}")

decrypted = simple_xor_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
```

## ৫. বিট ম্যানিপুলেশন টেকনিক

### ১. বিট সেট/ক্লিয়ার/টগল
```python
class BitManipulation:
    @staticmethod
    def set_bit(num, pos):
        """নির্দিষ্ট পজিশনে বিট সেট করা"""
        return num | (1 << pos)
    
    @staticmethod
    def clear_bit(num, pos):
        """নির্দিষ্ট পজিশনে বিট ক্লিয়ার করা"""
        return num & ~(1 << pos)
    
    @staticmethod
    def toggle_bit(num, pos):
        """নির্দিষ্ট পজিশনে বিট টগল করা"""
        return num ^ (1 << pos)
    
    @staticmethod
    def check_bit(num, pos):
        """নির্দিষ্ট পজিশনে বিট চেক করা"""
        return (num >> pos) & 1
    
    @staticmethod
    def update_bit(num, pos, value):
        """নির্দিষ্ট পজিশনে বিট আপডেট করা"""
        mask = ~(1 << pos)
        return (num & mask) | (value << pos)

# টেস্ট
bm = BitManipulation()
num = 0b1010  # 10

print(f"Original: {bin(num)}")
print(f"Set bit 1: {bin(bm.set_bit(num, 1))}")      # 1010 -> 1010 (already set)
print(f"Clear bit 3: {bin(bm.clear_bit(num, 3))}")  # 1010 -> 0010
print(f"Toggle bit 0: {bin(bm.toggle_bit(num, 0))}") # 1010 -> 1011
print(f"Check bit 2: {bm.check_bit(num, 2)}")       # 1
print(f"Update bit 1 to 0: {bin(bm.update_bit(num, 1, 0))}") # 1010 -> 1000
```

### ২. পাওয়ার অফ টু অপারেশন
```python
def next_power_of_two(n):
    """n এর পরের পাওয়ার অফ টু বের করা"""
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n + 1

def count_set_bits(n):
    """সংখ্যায় কতগুলো 1 বিট আছে গণনা"""
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

# টেস্ট
print(f"Next power of two after 13: {next_power_of_two(13)}")  # 16
print(f"Next power of two after 31: {next_power_of_two(31)}")  # 32

print(f"Set bits in 15: {count_set_bits(15)}")  # 4 (1111)
print(f"Set bits in 10: {count_set_bits(10)}")  # 2 (1010)
```

## ৬. কম্পিটিটিভ প্রোগ্রামিং সমস্যা

### সমস্যা ১: জোড়/বিজোড় চেক
```python
def is_even(n):
    """বিটওয়াইজে জোড় চেক"""
    return (n & 1) == 0

print(f"Is 5 even? {is_even(5)}")   # False
print(f"Is 8 even? {is_even(8)}")   # True
```

### সমস্যা ২: একবার আসা সংখ্যা খুঁজে বের করা
```python
def find_single_number(arr):
    """যে সংখ্যাটি একবার আসে (বাকিগুলো দুইবার)"""
    result = 0
    for num in arr:
        result ^= num
    return result

# টেস্ট
arr = [4, 2, 3, 2, 4, 3, 1]
print(f"Single number: {find_single_number(arr)}")  # 1
```

### সমস্যা ৩: বিট রিভার্স
```python
def reverse_bits(n, bits=32):
    """বিটগুলো উল্টানো"""
    result = 0
    for i in range(bits):
        if n & (1 << i):
            result |= (1 << (bits - 1 - i))
    return result

# টেস্ট (4-bit example)
num = 0b1010  # 10
reversed_num = reverse_bits(num, 4)
print(f"Original: {bin(num)} -> {num}")
print(f"Reversed: {bin(reversed_num)} -> {reversed_num}")  # 0101 = 5
```

## ৭. পারফরমেন্স বেনিফিট

```python
import time

# গুণের পারফরমেন্স তুলনা
def test_performance():
    n = 1000000
    
    # Normal multiplication
    start = time.time()
    for i in range(n):
        result = i * 8
    normal_time = time.time() - start
    
    # Bit shift multiplication
    start = time.time()
    for i in range(n):
        result = i << 3
    shift_time = time.time() - start
    
    print(f"Normal multiplication: {normal_time:.6f} seconds")
    print(f"Bit shift multiplication: {shift_time:.6f} seconds")
    print(f"Speedup: {normal_time/shift_time:.2f}x")

test_performance()
```

## ৮. সতর্কতা ও সীমাবদ্ধতা

### সতর্কতা:
1. **নেগেটিভ সংখ্যা** নিয়ে কাজ করার সময় সাবধান
2. **শিফটের সীমা** চেক করুন
3. **পাইথনে বিট লেন্থ** অসীম (arbitrary precision)

### কমন মিসটেকস:
```python
# ❌ ভুল: Priority issues
result = 5 & 3 == 1  # False (because: 5 & (3 == 1))
# ✅ সঠিক:
result = (5 & 3) == 1  # True

# ❌ ভুল: Sign extension with right shift
num = -8
result = num >> 1  # -4 (sign extended)
# ✅ সঠিক (unsigned shift):
result = (num & 0xFFFFFFFF) >> 1  # Logical shift
```

## ৯. প্র্যাকটিস সমস্যা

### সহজ:
1. জোড়/বিজোড় চেক
2. সংখ্যার সাইন চেক
3. ২ এর পাওয়ার চেক

### মধ্যম:
1. দুটি সংখ্যা swap
2. বিট কাউন্ট
3. বিট প্যালিনড্রোম

### কঠিন:
1. বিট রিভার্স
2. সাবসেট জেনারেশন
3. N-কুইন্স বিটওয়াইজ সল্যুশন

## ১০. চেকলিস্ট ফর বিটওয়াইজ

1. **অপারেটর প্রায়োরিটি** মনে রাখুন
2. **মাস্ক তৈরি** করতে শিখুন
3. **টু'স কমপ্লিমেন্ট** বুঝুন
4. **শিফটের** সীমা জানুন
5. **পারফরমেন্স ট্রেড-অফ** বিবেচনা করুন

## সারসংক্ষেপ:
- **`&`** = AND (দুইটিই 1)
- **`|`** = OR (যেকোনোটি 1)
- **`^`** = XOR (ভিন্ন হলে 1)
- **`~`** = NOT (বিট উল্টানো)
- **`<<`** = Left Shift (×2)
- **`>>`** = Right Shift (÷2)

**মনে রাখবেন:** বিটওয়াইজ অপারেশন শেখার জন্য প্রচুর প্র্যাকটিস দরকার। ছোট ছোট সমস্যা দিয়ে শুরু করুন এবং ধীরে ধীরে কমপ্লেক্স সমস্যায় যান!