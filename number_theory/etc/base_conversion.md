# সংখ্যা তত্ত্ব: বেস রূপান্তর - বিস্তারিত ও পাইথন উদাহরণ

## **১. মৌলিক ধারণা**

সংখ্যা তত্ত্বে, **বেস** বলতে সংখ্যা প্রকাশ করতে ব্যবহৃত স্বতন্ত্র অঙ্কের সংখ্যা বোঝায়।

- **দশমিক (বেস ১০)**: ০-৯ পর্যন্ত অঙ্ক ব্যবহার করে
- **বাইনারি (বেস ২)**: ০ এবং ১ অঙ্ক ব্যবহার করে
- **অক্টাল (বেস ৮)**: ০-৭ পর্যন্ত অঙ্ক ব্যবহার করে
- **হেক্সাডেসিমাল (বেস ১৬)**: ০-৯ এবং A-F অক্ষর ব্যবহার করে

## **২. গাণিতিক ভিত্তি**

যেকোনো সংখ্যা \( N \) বেস \( b \)-তে নিম্নোক্তভাবে প্রকাশ করা যায়:
\[
N = d_n b^n + d_{n-1} b^{n-1} + ... + d_1 b^1 + d_0 b^0
\]
যেখানে \( d_i \) হলো \( b \) এর থেকে ছোট অঙ্ক।

## **৩. বেস রূপান্তরের পদ্ধতি**

### **৩.১ দশমিক থেকে অন্য বেসে রূপান্তর**
**পদ্ধতি**: ক্রমাগত ভাগ এবং ভাগশেষ সংরক্ষণ
```python
def decimal_to_base(n, base):
    """দশমিক সংখ্যাকে নির্দিষ্ট বেসে রূপান্তর"""
    if n == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    is_negative = n < 0
    n = abs(n)
    
    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n = n // base
    
    return "-" + result if is_negative else result

# উদাহরণ
print(decimal_to_base(42, 2))   # 101010
print(decimal_to_base(42, 8))   # 52
print(decimal_to_base(42, 16))  # 2A
```

### **৩.২ যেকোনো বেস থেকে দশমিকে রূপান্তর**
**পদ্ধতি**: অবস্থানগত মানের সমষ্টি
```python
def base_to_decimal(number_str, base):
    """যেকোনো বেস থেকে দশমিকে রূপান্তর"""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_str = number_str.upper()
    
    # ঋণাত্মক সংখ্যা চেক
    is_negative = number_str.startswith('-')
    if is_negative:
        number_str = number_str[1:]
    
    result = 0
    power = len(number_str) - 1
    
    for char in number_str:
        digit_value = digits.index(char)
        result += digit_value * (base ** power)
        power -= 1
    
    return -result if is_negative else result

# উদাহরণ
print(base_to_decimal("101010", 2))   # 42
print(base_to_decimal("52", 8))       # 42
print(base_to_decimal("2A", 16))      # 42
```

## **৪. পাইথনে বিল্ট-ইন ফাংশন**

```python
# বাইনারি, অক্টাল, হেক্সাডেসিমাল রূপান্তর
num = 42

# দশমিক থেকে অন্যান্য বেস
print(bin(num))      # 0b101010
print(oct(num))      # 0o52
print(hex(num))      # 0x2a

# অন্যান্য বেস থেকে দশমিক
print(int('101010', 2))   # 42
print(int('52', 8))       # 42
print(int('2A', 16))      # 42
```

## **৫. উন্নত উদাহরণ: যেকোনো বেস থেকে যেকোনো বেসে**

```python
def base_converter(number_str, from_base, to_base):
    """যেকোনো বেস থেকে যেকোনো বেসে রূপান্তর"""
    # প্রথমে দশমিকে রূপান্তর
    decimal_val = base_to_decimal(number_str, from_base)
    
    # তারপর লক্ষ্য বেসে রূপান্তর
    return decimal_to_base(decimal_val, to_base)

# উদাহরণ
print(base_converter("101010", 2, 16))   # 2A
print(base_converter("2A", 16, 8))       # 52
print(base_converter("52", 8, 2))        # 101010
```

## **৬. বিশেষ ক্ষেত্র: ৩৬ পর্যন্ত বেসের জন্য**

```python
def validate_base(base):
    """বেস ভ্যালিডেশন"""
    if base < 2 or base > 36:
        raise ValueError("বেস ২ থেকে ৩৬ এর মধ্যে হতে হবে")
    return base

def full_base_converter(number, from_base, to_base):
    """সম্পূর্ণ বেস রূপান্তর ফাংশন"""
    validate_base(from_base)
    validate_base(to_base)
    
    # দশমিকে রূপান্তর
    decimal_val = base_to_decimal(str(number), from_base)
    
    # লক্ষ্য বেসে রূপান্তর
    return decimal_to_base(decimal_val, to_base)

# ব্যবহার
try:
    result = full_base_converter("Z3F", 36, 10)
    print(f"Z3F (বেস 36) = {result} (বেস 10)")
except ValueError as e:
    print(f"ত্রুটি: {e}")
```

## **৭. ব্যবহারিক প্রয়োগ**

### **৭.১ কম্পিউটার বিজ্ঞানে**
```python
# IP অ্যাড্রেস বাইনারিতে রূপান্তর
def ip_to_binary(ip_address):
    parts = ip_address.split('.')
    binary_parts = [bin(int(part))[2:].zfill(8) for part in parts]
    return '.'.join(binary_parts)

print(ip_to_binary("192.168.1.1"))  # 11000000.10101000.00000001.00000001
```

### **৭.২ ক্রিপ্টোগ্রাফিতে**
```python
# টেক্সট এনকোডিং
def text_to_base64(text, base=64):
    """টেক্সটকে ৬৪ বেসে এনকোড"""
    import string
    digits = string.digits + string.ascii_letters + "+/"
    
    result = ""
    for char in text:
        result += decimal_to_base(ord(char), base)
    return result

text = "Hello"
encoded = text_to_base64(text, 64)
print(f"'{text}' → বেস 64: {encoded}")
```

## **৮. সাধারণ বেসের বৈশিষ্ট্য**

| বেস | নাম | ব্যবহার | অঙ্ক |
|------|------|----------|------|
| 2 | বাইনারি | কম্পিউটার | 0-1 |
| 8 | অক্টাল | ইউনিক্স পারমিশন | 0-7 |
| 10 | দশমিক | দৈনন্দিন গণিত | 0-9 |
| 16 | হেক্সাডেসিমাল | ওয়েব কালার, মেমরি অ্যাড্রেস | 0-9, A-F |
| 32 | বেস-৩২ | ডেটা এনকোডিং | 0-9, A-V |
| 64 | বেস-৬৪ | এনক্রিপশন, এমবেডেড ডেটা | A-Z, a-z, 0-9, +, / |

## **৯. অনুশীলনের জন্য সমস্যা**

```python
# সমস্যা ১: সংখ্যা প্যালিনড্রোম চেক
def is_palindrome_in_base(n, base):
    num_in_base = decimal_to_base(n, base)
    return num_in_base == num_in_base[::-1]

print(is_palindrome_in_base(585, 2))  # True (585 = 1001001001 in binary)

# সমস্যা ২: বেস যোগ
def add_in_base(num1, num2, base):
    """দুইটি সংখ্যা প্রদত্ত বেসে যোগ"""
    dec1 = base_to_decimal(num1, base)
    dec2 = base_to_decimal(num2, base)
    sum_dec = dec1 + dec2
    return decimal_to_base(sum_dec, base)

print(add_in_base("101", "110", 2))  # 1011
```

## **১০. গুরুত্বপূর্ণ বিষয়**

1. **বেসের সীমা**: সাধারণত বেস ২-৩৬ পর্যন্ত (০-৯ এবং A-Z)
2. **ঋণাত্মক সংখ্যা**: টু'স কমপ্লিমেন্ট বা সাইন বিট ব্যবহার
3. **ভগ্নাংশ**: বেস পয়েন্টের পরেও রূপান্তর সম্ভব
4. **ত্রুটি হ্যান্ডলিং**: অবৈধ অঙ্ক বা বেসের জন্য

এই নোটটি সংখ্যা তত্ত্বে বেস রূপান্তরের মৌলিক ধারণা থেকে উন্নত প্রয়োগ পর্যন্ত কভার করে। পাইথন কোডের মাধ্যমে প্রতিটি ধারণা বাস্তবায়ন দেখানো হয়েছে।