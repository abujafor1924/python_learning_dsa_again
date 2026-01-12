# Square Root Decomposition - সম্পূর্ণ বাংলা টিউটোরিয়াল

## 📚 থিওরি ডিটেইলস (বাংলায়)

### **মৌলিক ধারণা**
Square Root Decomposition একটি "সহজ কিন্তু শক্তিশালী" ডেটা স্ট্রাকচার। এটা মূলত **ট্রেড-অফ** এর উপর ভিত্তি করে তৈরি:
- **Segment Tree/Fenwick Tree**: O(log n) টাইম, কিন্তু বাস্তবায়ন জটিল
- **Square Root Decomposition**: O(√n) টাইম, কিন্তু বাস্তবায়ন সহজ

### **গাণিতিক ব্যাখ্যা**
ধরা যাক:
- n = অ্যারের সাইজ
- b = ব্লক সাইজ
- k = মোট ব্লক সংখ্যা = ⌈n/b⌉

**কোয়েরি কমপ্লেক্সিটি**:
```
কোয়েরি = O(b + k)
```
যদি b = √n হয়:
```
k ≈ n/√n = √n
তাই কোয়েরি = O(√n + √n) = O(√n)
```

### **ব্লক সাইজ কেন √n?**
ব্লক সাইজ b হলে:
1. আংশিক ব্লকের এলিমেন্ট ≤ 2b
2. পূর্ণ ব্লকের সংখ্যা ≤ n/b

মোট অপারেশন: **O(b + n/b)**
b = √n নিলে মিনিমাম হয় (ক্যালকুলাসের মিনিমাইজেশন থিওরেম অনুসারে)

---

## 🐍 পাইথন ইমপ্লিমেন্টেশন (সম্পূর্ণ ভার্সন)

```python
import math

class SqrtDecomposition:
    """
    Square Root Decomposition for Range Sum Query with Point Updates
    """
    
    def __init__(self, arr):
        """
        Initialize with given array
        Time Complexity: O(n)
        """
        self.arr = arr[:]  # কপি করছি
        self.n = len(arr)
        self.block_size = int(math.sqrt(self.n)) + 1
        self.block_sum = [0] * self.block_size
        
        # প্রিপ্রোসেসিং: ব্লক ভাগ করে যোগফল বের করি
        self._build()
    
    def _build(self):
        """ব্লকগুলো তৈরি করি"""
        for i in range(self.n):
            block_idx = i // self.block_size
            self.block_sum[block_idx] += self.arr[i]
    
    def update(self, index, value):
        """
        Point Update: arr[index] = value
        Time Complexity: O(1)
        """
        if 0 <= index < self.n:
            block_idx = index // self.block_size
            old_value = self.arr[index]
            self.block_sum[block_idx] += (value - old_value)
            self.arr[index] = value
        else:
            raise IndexError("Index out of range")
    
    def query(self, l, r):
        """
        Range Sum Query: sum(arr[l] to arr[r])
        Time Complexity: O(√n)
        """
        if l < 0 or r >= self.n or l > r:
            raise ValueError("Invalid range")
        
        sum_val = 0
        
        # বামের আংশিক ব্লক
        while l <= r and l % self.block_size != 0:
            sum_val += self.arr[l]
            l += 1
        
        # মাঝের পূর্ণ ব্লকগুলো
        while l + self.block_size <= r:
            block_idx = l // self.block_size
            sum_val += self.block_sum[block_idx]
            l += self.block_size
        
        # ডানের আংশিক ব্লক
        while l <= r:
            sum_val += self.arr[l]
            l += 1
        
        return sum_val
    
    def print_state(self):
        """ডিবাগিং এর জন্য স্টেট প্রিন্ট"""
        print("=" * 50)
        print(f"Array Size: {self.n}")
        print(f"Block Size: {self.block_size}")
        print(f"Number of Blocks: {len(self.block_sum)}")
        print()
        
        print("Array with block boundaries:")
        for i in range(self.n):
            if i % self.block_size == 0:
                print(f"\nBlock {i//self.block_size}: ", end="")
            print(f"{self.arr[i]:3}", end=" ")
        print()
        
        print("\nBlock Sums:")
        for i, s in enumerate(self.block_sum):
            print(f"Block {i}: {s}")
        print("=" * 50)


# ব্যবহারের উদাহরণ
def main():
    # উদাহরণ ১: সাধারণ অ্যারে
    print("উদাহরণ ১: সাধারণ রেঞ্জ কোয়েরি")
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sd1 = SqrtDecomposition(arr1)
    sd1.print_state()
    
    print(f"\nQuery(2, 7): {sd1.query(2, 7)}")  # 3+4+5+6+7+8 = 33
    
    print("\nUpdating index 3 to 100...")
    sd1.update(3, 100)
    print(f"Query(2, 7): {sd1.query(2, 7)}")  # 3+100+5+6+7+8 = 129
    
    # উদাহরণ ২: ২টি কোয়েরির মধ্যে আপডেট
    print("\n\nউদাহরণ ২: মাল্টিপল অপারেশন")
    arr2 = list(range(1, 21))  # [1, 2, ..., 20]
    sd2 = SqrtDecomposition(arr2)
    
    queries = [(0, 19), (5, 15), (10, 19)]
    for l, r in queries:
        result = sd2.query(l, r)
        print(f"Sum({l}, {r}) = {result}")
    
    print("\nMultiple updates...")
    updates = [(0, 100), (10, 200), (19, 300)]
    for idx, val in updates:
        sd2.update(idx, val)
    
    print("\nAfter updates:")
    for l, r in queries:
        result = sd2.query(l, r)
        print(f"Sum({l}, {r}) = {result}")


if __name__ == "__main__":
    main()
```

## 🔧 অ্যাডভান্সড ফিচার (আরও কিছু অপারেশন)

```python
class AdvancedSqrtDecomposition:
    """
    আরও ফিচার সহ Sqrt Decomposition
    - Range Minimum Query
    - Range Update (Lazy Propagation ভাবনা)
    """
    
    def __init__(self, arr):
        self.arr = arr[:]
        self.n = len(arr)
        self.block_size = int(math.sqrt(self.n)) + 1
        self.block_min = [float('inf')] * self.block_size
        self.block_sum = [0] * self.block_size
        
        self._build()
    
    def _build(self):
        for i in range(self.n):
            block_idx = i // self.block_size
            self.block_sum[block_idx] += self.arr[i]
            self.block_min[block_idx] = min(self.block_min[block_idx], self.arr[i])
    
    def range_min_query(self, l, r):
        """রেঞ্জ মিনিমাম কোয়েরি"""
        min_val = float('inf')
        
        # বামের আংশিক ব্লক
        while l <= r and l % self.block_size != 0:
            min_val = min(min_val, self.arr[l])
            l += 1
        
        # মাঝের পূর্ণ ব্লকগুলো
        while l + self.block_size <= r:
            block_idx = l // self.block_size
            min_val = min(min_val, self.block_min[block_idx])
            l += self.block_size
        
        # ডানের আংশিক ব্লক
        while l <= r:
            min_val = min(min_val, self.arr[l])
            l += 1
        
        return min_val
    
    def range_sum_query(self, l, r):
        """রেঞ্জ সাম কোয়েরি"""
        return self._query_sum(l, r)
    
    def _query_sum(self, l, r):
        """প্রাইভেট সাম কোয়েরি মেথড"""
        sum_val = 0
        
        while l <= r and l % self.block_size != 0:
            sum_val += self.arr[l]
            l += 1
        
        while l + self.block_size <= r:
            block_idx = l // self.block_size
            sum_val += self.block_sum[block_idx]
            l += self.block_size
        
        while l <= r:
            sum_val += self.arr[l]
            l += 1
        
        return sum_val


# টেস্ট কোড
def test_advanced_features():
    print("অ্যাডভান্সড ফিচার টেস্ট")
    arr = [5, 2, 8, 1, 9, 3, 7, 4, 6, 0]
    adv = AdvancedSqrtDecomposition(arr)
    
    print(f"Array: {arr}")
    print(f"Range Min(2, 7): {adv.range_min_query(2, 7)}")  # min(8,1,9,3,7,4) = 1
    print(f"Range Sum(2, 7): {adv.range_sum_query(2, 7)}")  # sum(8,1,9,3,7,4) = 32
```

## 📊 Segment Tree vs Sqrt Decomposition তুলনা

| বিষয় | Square Root Decomposition | Segment Tree |
|------|--------------------------|--------------|
| **টাইম কমপ্লেক্সিটি** | O(√n) কোয়েরি, O(1) আপডেট | O(log n) উভয় |
| **স্পেস কমপ্লেক্সিটি** | O(√n) এক্সট্রা | O(4n) এক্সট্রা |
| **বাস্তবায়ন সহজতা** | খুব সহজ | মাঝারি-কঠিন |
| **লার্নিং কার্ভ** | ন্যূনতম | মাঝারি |
| **ফ্লেক্সিবিলিটি** | সীমিত | খুব ফ্লেক্সিবল |
| **মেমরি অ্যাক্সেস** | ক্যাশে ফ্রেন্ডলি | রিকার্সিভ সমস্যা |

## 🎯 কখন ব্যবহার করবো?

### **হ্যাঁ, ব্যবহার করবো যখন:**
1. ইন্টারভিউতে জিজ্ঞেস করলে (সহজ ইমপ্লিমেন্টেশন)
2. n ≤ 10^5 (√n ≈ 316 অপারেশন, যা গ্রহণযোগ্য)
3. আপডেট বেশি, কোয়েরি কম এমন প্রবলেম
4. কোডিং কনটেস্টে দ্রুত ইমপ্লিমেন্ট করতে চাইলে

### **না, ব্যবহার করবো না যখন:**
1. n ≥ 10^6 (√n ≈ 1000, যা অনেক)
2. রিয়েল-টাইম সিস্টেম যেখানে O(log n) চাই
3. কমপ্লেক্স অপারেশন (range update, gcd, ইত্যাদি)

## 💡 ইন্টারভিউ প্রশ্ন (প্র্যাকটিস)

1. **সোজা প্রশ্ন**: 10^5 সাইজের অ্যারে, 10^5 টি কুয়েরি। প্রতিটি কুয়েরিতে l থেকে r যোগফল বের করতে হবে, আর মধ্যে মধ্যে আপডেটও আছে।
   
2. **মাঝারি প্রশ্ন**: অ্যারের যেকোন রেঞ্জে মিনিমাম এবং যোগফল বের করার ডেটা স্ট্রাকচার ডিজাইন করো।

3. **কঠিন প্রশ্ন**: Square Root Decomposition দিয়ে Range Update (লেজি প্রোপাগেশন) কিভাবে ইমপ্লিমেন্ট করবে?

## 📝 মনে রাখার টিপস

1. **"ভাগ করো, শাসন করো"** - অ্যারেকে ব্লকে ভাগ করো
2. **ব্লক সাইজ = √n** - এটাই সেরা ট্রেড-অফ
3. **৩টা পার্ট** - Left partial + Middle full + Right partial
4. **আপডেট O(1)** - শুধু ব্লক সাম আপডেট করো

## 🚀 চ্যালেঞ্জ প্রবলেমস (প্র্যাকটিস করার জন্য)

1. **Mo's Algorithm**: Square Root Decomposition এর উপর ভিত্তি করে বিখ্যাত অ্যালগোরিদম
2. **Range GCD Query**: GCD অপারেশনের জন্য অ্যাডাপ্ট করো
3. **Frequency Array**: ব্লকভিত্তিক ফ্রিকুয়েন্সি কাউন্ট

---

## ✅ শেষ কথাঃ

Square Root Decomposition **সহজবোধ্যতা এবং কার্যকারিতার** মাঝামাঝি একটি সুন্দর ডেটা স্ট্রাকচার। 

**মূল মন্ত্র**: 
> "যখন Segment Tree মনে জটিল লাগে, তখন Square Root Decomposition তোমার বন্ধু!"

এটা শেখার পর তুমি:
- √n কমপ্লেক্সিটি বুঝতে পারবে
- ট্রেড-অফ অ্যানালাইসিস করতে পারবে
- অনেক কোডিং ইন্টারভিউ প্রবলেম সলভ করতে পারবে

কোন প্রশ্ন থাকলে বলো! 😊