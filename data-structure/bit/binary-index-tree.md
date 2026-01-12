# বাইনারি ইনডেক্সড ট্রি (BIT / Fenwick Tree)

## পরিচিতি
বাইনারি ইনডেক্সড ট্রি বা ফেনউইক ট্রি (Fenwick Tree) হলো একটি দক্ষ ডেটা স্ট্রাকচার যা একটি অ্যারের উপাদানগুলির **প্রিফিক্স যোগফল** (prefix sum) দ্রুত গণনা করতে এবং **পয়েন্ট আপডেট** (point update) করতে ব্যবহৃত হয়।

## কেন BIT ব্যবহার করব?
- **সেগমেন্ট ট্রি**-এর চেয়ে কম মেমোরি ব্যবহার করে (O(n))
- **কোড খুবই সংক্ষিপ্ত** এবং বাস্তবায়ন সহজ
- **দ্রুতগতি** (প্রতিটি অপারেশন O(log n))
- **কম মেমোরি ফুটপ্রিন্ট**

## BIT এর সীমাবদ্ধতা
BIT শুধুমাত্র **বিপরীতমুখী অপারেশন** (invertible operations) সমর্থন করে:
- যোগফল (sum)
- গুণফল (product)
- XOR অপারেশন

## মৌলিক অপারেশন

### ১. read(idx) বা query(idx)
idx পর্যন্ত (১-ভিত্তিক ইনডেক্সিং) প্রিফিক্স যোগফল রিটার্ন করে।

```python
def read(bit, idx):
    """1 থেকে idx পর্যন্ত যোগফল রিটার্ন করে"""
    total = 0
    while idx > 0:
        total += bit[idx]
        idx -= idx & -idx  # সর্বনিম্ন সেট বিট বন্ধ করা
    return total
```

### ২. update(idx, value)
idx অবস্থানে value যোগ করে।

```python
def update(bit, idx, value):
    """idx অবস্থানে value যোগ করে"""
    n = len(bit) - 1
    while idx <= n:
        bit[idx] += value
        idx += idx & -idx  # সর্বনিম্ন সেট বিট যোগ করা
```

## বিস্তারিত ব্যাখ্যা

### BIT কিভাবে কাজ করে?
BIT প্রতিটি ইনডেক্সে নির্দিষ্ট রেঞ্জের যোগফল সংরক্ষণ করে। প্রতিটি ইনডেক্স i এর জন্য:
- tree[i] = arr[i - 2^r + 1] থেকে arr[i] পর্যন্ত যোগফল
- যেখানে r = i-এর সর্বনিম্ন সেট বিটের অবস্থান (LSB)

### LSB (Lowest Set Bit)
- `idx & -idx`: idx-এর সর্বনিম্ন সেট বিট বের করে
- উদাহরণ: 
  - idx = 6 (110₂) → LSB = 2 (10₂)
  - idx = 8 (1000₂) → LSB = 8 (1000₂)

## সম্পূর্ণ Python বাস্তবায়ন

```python
class BinaryIndexedTree:
    def __init__(self, n):
        """n সাইজের BIT তৈরি করুন"""
        self.n = n
        self.bit = [0] * (n + 1)  # 1-ভিত্তিক ইনডেক্সিং
    
    def update(self, idx, delta):
        """idx অবস্থানে delta যোগ করুন"""
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        """1 থেকে idx পর্যন্ত যোগফল"""
        total = 0
        while idx > 0:
            total += self.bit[idx]
            idx -= idx & -idx
        return total
    
    def range_sum(self, l, r):
        """l থেকে r পর্যন্ত যোগফল (l এবং r সহ)"""
        return self.query(r) - self.query(l - 1)
    
    def get_prefix_sum(self, idx):
        """query-এর alias"""
        return self.query(idx)
    
    def get_value(self, idx):
        """একক অবস্থানের মান পেতে"""
        return self.range_sum(idx, idx)
    
    def build_from_array(self, arr):
        """অ্যারে থেকে BIT তৈরি করুন"""
        for i, value in enumerate(arr, 1):
            self.update(i, value)

# বিকল্প: ফাংশন ভিত্তিক বাস্তবায়ন
def create_bit(n):
    """n সাইজের BIT তৈরি করে"""
    return [0] * (n + 1)

def bit_update(bit, idx, delta):
    """BIT আপডেট"""
    n = len(bit) - 1
    while idx <= n:
        bit[idx] += delta
        idx += idx & -idx

def bit_query(bit, idx):
    """BIT থেকে কুয়েরি"""
    total = 0
    while idx > 0:
        total += bit[idx]
        idx -= idx & -idx
    return total
```

## উদাহরণ

### উদাহরণ ১: মৌলিক ব্যবহার
```python
# উদাহরণ অ্যারে: [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]

# BIT তৈরি
bit = BinaryIndexedTree(12)

# মানগুলো যোগ করুন
values = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
for i, val in enumerate(values, 1):
    bit.update(i, val)

print("1 থেকে 5 পর্যন্ত যোগফল:", bit.query(5))  # 2+1+1+3+2 = 9
print("3 থেকে 7 পর্যন্ত যোগফল:", bit.range_sum(3, 7))  # 1+3+2+3+4 = 13

# একটি মান আপডেট
print("\nআপডেটের আগে 1 থেকে 5 পর্যন্ত যোগফল:", bit.query(5))
bit.update(3, 2)  # অবস্থান 3-এ 2 যোগ
print("আপডেটের পরে 1 থেকে 5 পর্যন্ত যোগফল:", bit.query(5))  # 11
```

### উদাহরণ ২: ফ্রিকোয়েন্সি কাউন্টার
```python
class FrequencyCounter:
    def __init__(self, max_value):
        """0 থেকে max_value পর্যন্ত সংখ্যার ফ্রিকোয়েন্সি ট্র্যাক করুন"""
        self.max_val = max_value
        self.bit = BinaryIndexedTree(max_value)
    
    def add(self, value):
        """একটি সংখ্যা যোগ করুন"""
        if 1 <= value <= self.max_val:
            self.bit.update(value, 1)
    
    def remove(self, value):
        """একটি সংখ্যা বাদ দিন"""
        if 1 <= value <= self.max_val:
            self.bit.update(value, -1)
    
    def count_less_equal(self, value):
        """value বা তার চেয়ে ছোট সংখ্যার গণনা"""
        if value < 1:
            return 0
        if value > self.max_val:
            value = self.max_val
        return self.bit.query(value)
    
    def count_in_range(self, l, r):
        """l থেকে r পর্যন্ত সংখ্যার গণনা"""
        if l > r or l < 1 or r > self.max_val:
            return 0
        return self.bit.range_sum(l, r)

# ব্যবহারের উদাহরণ
counter = FrequencyCounter(10)
numbers = [3, 5, 2, 3, 8, 5, 1, 2, 3]

for num in numbers:
    counter.add(num)

print("5 বা তার কম সংখ্যার গণনা:", counter.count_less_equal(5))  # 3,5,2,3,5,1,2,3 = 8
print("3 থেকে 7 পর্যন্ত সংখ্যার গণনা:", counter.count_in_range(3, 7))  # 3,5,3,5,3 = 5
```

## গাণিতিক ব্যাখ্যা

### BIT-এর সূচনা
ধরা যাক, আমাদের অ্যারে arr[1...n] আছে:

```
arr: [a1, a2, a3, a4, a5, a6, a7, a8]
```

BIT-এ প্রতিটি অবস্থানে সংরক্ষিত মান:

```
bit[1] = arr[1]
bit[2] = arr[1] + arr[2]
bit[3] = arr[3]
bit[4] = arr[1] + arr[2] + arr[3] + arr[4]
bit[5] = arr[5]
bit[6] = arr[5] + arr[6]
bit[7] = arr[7]
bit[8] = arr[1] + arr[2] + ... + arr[8]
```

### প্রশ্নের জটিলতা বিশ্লেষণ
- **আপডেট**: O(log n)
- **কুয়েরি**: O(log n)
- **মেমোরি**: O(n)

### 2D BIT (দ্বিমাত্রিক)
```python
class BIT2D:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.bit = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    def update(self, x, y, delta):
        i = x
        while i <= self.rows:
            j = y
            while j <= self.cols:
                self.bit[i][j] += delta
                j += j & -j
            i += i & -i
    
    def query(self, x, y):
        """(1,1) থেকে (x,y) পর্যন্ত যোগফল"""
        total = 0
        i = x
        while i > 0:
            j = y
            while j > 0:
                total += self.bit[i][j]
                j -= j & -j
            i -= i & -i
        return total
    
    def range_sum(self, x1, y1, x2, y2):
        """(x1,y1) থেকে (x2,y2) পর্যন্ত যোগফল"""
        return (self.query(x2, y2) - self.query(x1-1, y2) - 
                self.query(x2, y1-1) + self.query(x1-1, y1-1))
```

## সাধারণ ব্যবহারের ক্ষেত্র
1. **ডায়নামিক প্রিফিক্স যোগফল**
2. **ইনভার্শন কাউন্ট** (Inversion Count)
3. **রেঞ্জ কুয়েরি ও পয়েন্ট আপডেট**
4. **ফ্রিকোয়েন্সি অ্যারে ম্যানিপুলেশন**
5. **অর্ডার স্ট্যাটিস্টিক্স**

## BIT vs সেগমেন্ট ট্রি

| বৈশিষ্ট্য | BIT | সেগমেন্ট ট্রি |
|-----------|-----|---------------|
| মেমোরি | O(n) | O(4n) |
| কোডের দৈর্ঘ্য | ছোট (10-15 লাইন) | বড় (30-40 লাইন) |
| অপারেশন | শুধুমাত্র বিপরীতমুখী | সব ধরনের |
| নমনীয়তা | কম | বেশি |
| গতি | দ্রুত | কিছুটা ধীর |

## উপসংহার
BIT একটি অত্যন্ত কার্যকরী ডেটা স্ট্রাকচার যখন শুধুমাত্র **প্রিফিক্স যোগফল** এবং **পয়েন্ট আপডেট** প্রয়োজন হয়। এর সরল বাস্তবায়ন এবং দক্ষতা এটিকে প্রতিযোগিতামূলক প্রোগ্রামিং-এ জনপ্রিয় করে তুলেছে।