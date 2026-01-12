# **Static Query + Square Root Decomposition: বিস্তারিত বাংলা গাইড**

## 📌 **মূল ধারণা**
আমাদের একটা **এ্যারে (Array)** দেওয়া থাকবে এবং বারবার **রেঞ্জ কুয়েরি (Range Query)** আসবে — যেমন "L থেকে R ইনডেক্সের মধ্যে সবচেয়ে বড় সংখ্যা/যোগফল/সর্বনিম্ন সংখ্যা কত?"

**সমস্যা:** প্রতিবার কুয়েরি আসলে পুরো রেঞ্জ স্ক্যান করলে সময় লাগে O(n), যা কুয়েরি বেশি হলে অত্যন্ত ধীর।

**সমাধান:** Square Root Decomposition — এ্যারেটিকে √n সাইজের ব্লকে ভাগ করে প্রতিটা ব্লকের তথ্য আগে থেকে হিসাব করে রাখি।

---

## 🔢 **গাণিতিক ভিত্তি**

- এ্যারে সাইজ = `n`
- ব্লক সাইজ = `block_size = ceil(sqrt(n))`
- মোট ব্লক সংখ্যা = `num_blocks = ceil(n / block_size)`

**উদাহরণ:** n = 10 হলে:
```
sqrt(10) ≈ 3.16
block_size = 4 (ceil করলে)
num_blocks = ceil(10/4) = 3
```

---

## 🧩 **ব্লক তৈরি পদ্ধতি**

### **এ্যারে:** 
```
ইনডেক্স:  0   1   2   3   4   5   6   7   8   9
মান:     2   4   7   1   8   3   9   5   6   2
```

### **ব্লক ভাগ (block_size = 4):**
```
ব্লক 0: [2, 4, 7, 1]   → sum = 14, max = 7
ব্লক 1: [8, 3, 9, 5]   → sum = 25, max = 9  
ব্লক 2: [6, 2]         → sum = 8,  max = 6
```

**ব্লক ইনফো স্ট্রাকচার:** 
```
block_sum = [14, 25, 8]
block_max = [7, 9, 6]
```

---

## 🔍 **কুয়েরি প্রক্রিয়া**

### **কুয়েরি:** L=2 থেকে R=7 (মান: 7,1,8,3,9,5)

**ধাপ ১:** L এবং R কোন ব্লকে আছে?
```
ব্লক 0: ইনডেক্স 0-3
ব্লক 1: ইনডেক্স 4-7  
ব্লক 2: ইনডেক্স 8-9

L=2 → ব্লক 0
R=7 → ব্লক 1
```

**ধাপ ২:** তিন অংশে ভাগ করে কাজ:
1. **বাম অংশ (ব্লক 0):** ইনডেক্স 2-3 → manually calculate
2. **মধ্যম অংশ (পুরো ব্লক):** ব্লক 1 (ইনডেক্স 4-7) → block_sum[1] use
3. **ডান অংশ (ব্লক 2):** নেই এখানে

**ধাপ ৩:** যোগফল বের করি:
```
বাম অংশ (2-3): arr[2] + arr[3] = 7 + 1 = 8
মধ্যম অংশ (4-7): block_sum[1] = 25
ডান অংশ: নেই
মোট = 8 + 25 = 33 ✅
```

---

## 🐍 **পাইথন ইমপ্লিমেন্টেশন**

### **1. যোগফলের জন্য (Sum Query):**

```python
import math

class SqrtDecomposition:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr.copy()
        
        # ব্লক সাইজ ও সংখ্যা
        self.block_size = int(math.ceil(math.sqrt(self.n)))
        self.num_blocks = (self.n + self.block_size - 1) // self.block_size
        
        # ব্লক যোগফল আগে থেকে হিসাব
        self.block_sum = [0] * self.num_blocks
        
        for i in range(self.n):
            block_idx = i // self.block_size
            self.block_sum[block_idx] += arr[i]
    
    def query_sum(self, l, r):
        total = 0
        
        # বাম থেকে শুরু
        while l <= r and l % self.block_size != 0:
            total += self.arr[l]
            l += 1
        
        # পুরো ব্লক যতগুলো আছে
        while l + self.block_size <= r:
            block_idx = l // self.block_size
            total += self.block_sum[block_idx]
            l += self.block_size
        
        # ডানের অংশ
        while l <= r:
            total += self.arr[l]
            l += 1
        
        return total

# ব্যবহার
arr = [2, 4, 7, 1, 8, 3, 9, 5, 6, 2]
sq = SqrtDecomposition(arr)
print(f"যোগফল (2 থেকে 7): {sq.query_sum(2, 7)}")  # Output: 33
print(f"যোগফল (0 থেকে 9): {sq.query_sum(0, 9)}")  # Output: 47
```

### **2. সর্বোচ্চ মানের জন্য (Max Query):**

```python
import math

class SqrtDecompositionMax:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr.copy()
        
        self.block_size = int(math.ceil(math.sqrt(self.n)))
        self.num_blocks = (self.n + self.block_size - 1) // self.block_size
        
        # প্রতিটি ব্লকের সর্বোচ্চ মান
        self.block_max = [-float('inf')] * self.num_blocks
        
        for i in range(self.n):
            block_idx = i // self.block_size
            self.block_max[block_idx] = max(self.block_max[block_idx], arr[i])
    
    def query_max(self, l, r):
        max_val = -float('inf')
        
        # বাম অংশ
        while l <= r and l % self.block_size != 0:
            max_val = max(max_val, self.arr[l])
            l += 1
        
        # পুরো ব্লক
        while l + self.block_size <= r:
            block_idx = l // self.block_size
            max_val = max(max_val, self.block_max[block_idx])
            l += self.block_size
        
        # ডান অংশ
        while l <= r:
            max_val = max(max_val, self.arr[l])
            l += 1
        
        return max_val

# ব্যবহার
arr = [2, 4, 7, 1, 8, 3, 9, 5, 6, 2]
sq_max = SqrtDecompositionMax(arr)
print(f"সর্বোচ্চ (2 থেকে 7): {sq_max.query_max(2, 7)}")  # Output: 9
print(f"সর্বোচ্চ (0 থেকে 3): {sq_max.query_max(0, 3)}")  # Output: 7
```

---

## ⚡ **টাইম কমপ্লেক্সিটি বিশ্লেষণ**

| অপারেশন | Brute Force | Square Root Decomposition |
|---------|-------------|---------------------------|
| প্রিপ্রোসেসিং | O(1) | **O(n)** |
| প্রতি কুয়েরি | **O(n)** | **O(√n)** |
| Qটি কুয়েরি | O(Q × n) | O(n + Q × √n) |
| মেমরি | O(n) | O(n + √n) ≈ O(n) |

**উদাহরণ:**
- n = 100,000
- Q = 100,000
- Brute Force: 100,000 × 100,000 ≈ 10¹⁰ অপারেশন
- Sqrt Decomp: 100,000 + 100,000 × 316 ≈ 3.16 × 10⁷ অপারেশন
- **৩১৬ গুণ দ্রুত!** ⚡

---

## 🎯 **কোড অপ্টিমাইজেশন (সহজ সংস্করণ)**

```python
import math

def sqrt_decomposition_simple(arr, queries):
    n = len(arr)
    block_size = int(math.sqrt(n)) + 1
    num_blocks = (n + block_size - 1) // block_size
    
    # ব্লক যোগফল
    block_sum = [0] * num_blocks
    for i in range(n):
        block_idx = i // block_size
        block_sum[block_idx] += arr[i]
    
    results = []
    
    for l, r in queries:
        total = 0
        
        # বাম কিনারা
        while l <= r and l % block_size != 0:
            total += arr[l]
            l += 1
        
        # পুরো ব্লক
        while l + block_size <= r:
            total += block_sum[l // block_size]
            l += block_size
        
        # ডান কিনারা
        while l <= r:
            total += arr[l]
            l += 1
        
        results.append(total)
    
    return results

# টেস্ট
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
queries = [(0, 4), (2, 7), (1, 9), (3, 3)]
print("কুয়েরি ফলাফল:", sqrt_decomposition_simple(arr, queries))
# Output: [15, 33, 54, 4]
```

---

## 🔄 **Segment Tree vs Sqrt Decomposition**

| বিষয় | Square Root Decomposition | Segment Tree |
|------|--------------------------|--------------|
| **কোড জটিলতা** | সহজ (এমনকি contest-এও লিখা যায়) | জটিল (মনে রাখা কঠিন) |
| **কুয়েরি টাইম** | O(√n) | O(log n) |
| **আপডেট টাইম** | O(√n) | O(log n) |
| **মেমরি** | O(n) | O(4n) ≈ বেশি |
| **স্ট্যাটিক কুয়েরি** | ভালো | ভালো |
| **ডাইনামিক আপডেট** | ধীর | দ্রুত |
| **বুঝতে সুবিধা** | সহজ | অপেক্ষাকৃত কঠিন |

---

## 🚀 **কখন কোনটার ব্যবহার?**

### **√ Decomposition ব্যবহার করব যখন:**
1. কোড সহজ রাখতে চাই
2. n ≤ 2×10⁵ (√n ≈ 450 অপারেশন, যা গ্রহণযোগ্য)
3. আপডেট কম বা static ডেটা
4. কনটেস্টে দ্রুত ইমপ্লিমেন্ট করতে হবে

### **Segment Tree ব্যবহার করব যখন:**
1. n বড় (≥ 10⁶)
2. আপডেট বেশি
3. জটিল অপারেশন (range update + query)
4. টাইম লিমিট কঠিন

---

## 💡 **প্র্যাকটিস প্রবলেমস**

1. **মৌলিক:** SPOJ - RMQSQ (Range Minimum Query)
2. **মাঝারি:** Codeforces - D. Powerful Array (Mo's Algorithm-এর ভিত্তি)
3. **উন্নত:** লাইটজই - 1082 - Array Queries

---

## ❓ **প্রশ্নোত্তর**

**Q: কেন এটাকে "Static Query" বলে?**  
A: কারণ এখানে এ্যারে পরিবর্তন হয় না। শুধু query-র উত্তর দিতে হবে। যদি আপডেট চাওয়া হয়, তবে Segment Tree বা Fenwick Tree ভালো।

**Q: √n কেন, অন্য সাইজ হলে কী সমস্যা?**  
A: √n-এ কুয়েরি টাইম এবং ব্লক সংখ্যা ব্যালেন্স থাকে। যদি ব্লক সাইজ খুব ছোট বা বড় হয়, তবে পারফরম্যান্স খারাপ হয়।

**Q: Real-life এ কোথায় ব্যবহার হয়?**  
A: ডাটাবেসে large data query, ইমেজ প্রসেসিং (block-wise operation), ডিস্ট্রিবিউটেড সিস্টেমে ডেটা পার্টিশন।

---

## 📝 **সংক্ষিপ্ত টেকনিক**

> **"এ্যারে কেটে বানাও ব্লক,  
> ব্লকের হিসাব আগে রাখ,  
> কুয়েরি এলে তিন ভাগে ভাগ,  
> সময় বাঁচাও √n ম্যাজিক!"**

---

**চর্চার জন্য:** নিচের এ্যারে নিয়ে ব্লক তৈরি করে দেখুন:
```
এ্যারে: [5, 8, 3, 2, 9, 4, 7, 1, 6]
ব্লক সাইজ: 3
কুয়েরি: (1,6), (0,8), (3,5)
```

**প্রতিটা কুয়েরির জন্য:** 
1. ব্লক ডিভিশন করো
2. block_sum/block_max বের করো  
3. ম্যানুয়ালি কুয়েরি এনসার করো
4. কোড লিখে চেক করো