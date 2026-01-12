# সেগমেন্ট ট্রি (Segment Tree) - সম্পূর্ণ গাইড

## সেগমেন্ট ট্রি কি?
সেগমেন্ট ট্রি হল একটি **বাইনারি ট্রি ডেটা স্ট্রাকচার** যা একটি অ্যারের উপরে বিভিন্ন রেঞ্জ কুয়েরি (range queries) দ্রুত প্রসেস করতে ব্যবহৃত হয়। এটি:
- **O(log n)** সময়ে রেঞ্জ কুয়েরি করে
- **O(log n)** সময়ে সিঙ্গেল এলিমেন্ট আপডেট করে
- **O(n)** স্পেস ব্যবহার করে

## কেন সেগমেন্ট ট্রি ব্যবহার করব?
- বাইনারি সার্চ/বিএসটি এর চেয়ে সহজ
- অ্যারে এলিমেন্ট আপডেট করা যায়
- বিভিন্ন ধরনের রেঞ্জ কুয়েরি (যোগফল, সর্বোচ্চ, সর্বনিম্ন ইত্যাদি)

## বেসিক কনসেপ্ট

### উদাহরণ অ্যারে: [1, 2, 3, 4, 5, 6, 7, 8]
```
ইনডেক্স:   0  1  2  3  4  5  6  7
মান:      [1, 2, 3, 4, 5, 6, 7, 8]
```

### সেগমেন্ট ট্রি গঠন (যোগফলের জন্য):
```
লেভেল 0:               [0-7: 36]
                      /           \
লেভেল 1:        [0-3: 10]         [4-7: 26]
                /      \           /      \
লেভেল 2:   [0-1: 3]  [2-3: 7]  [4-5: 11]  [6-7: 15]
           /   \     /   \     /   \     /   \
লেভেল 3: [0:1][1:2][2:3][3:4][4:5][5:6][6:7][7:8]
```

## পাইথনে ইমপ্লিমেন্টেশন

### ১. বেসিক সেগমেন্ট ট্রি (যোগফল)

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        # সেগমেন্ট ট্রি এর সাইজ: 4 * n (সর্বোচ্চ প্রয়োজন)
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)
    
    def build(self, node, start, end):
        """বিল্ড ফাংশন: O(n)"""
        if start == end:
            # লিফ নোড
            self.tree[node] = self.arr[start]
            return
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        # বাম ও ডান সাবট্রি বিল্ড
        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)
        
        # বর্তমান নোড = বাম + ডান সাবট্রি
        self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def query(self, l, r, node=0, start=0, end=None):
        """রেঞ্জ কুয়েরি: O(log n)"""
        if end is None:
            end = self.n - 1
        
        # ৩টি কেস:
        # ১. সম্পূর্ণ বাইরে
        if r < start or l > end:
            return 0
        
        # ২. সম্পূর্ণ ভিতরে
        if l <= start and end <= r:
            return self.tree[node]
        
        # ৩. আংশিকভাবে ওভারল্যাপ
        mid = (start + end) // 2
        left_sum = self.query(l, r, 2 * node + 1, start, mid)
        right_sum = self.query(l, r, 2 * node + 2, mid + 1, end)
        
        return left_sum + right_sum
    
    def update(self, idx, value, node=0, start=0, end=None):
        """সিঙ্গেল এলিমেন্ট আপডেট: O(log n)"""
        if end is None:
            end = self.n - 1
        
        if start == end:
            # লিফ নোড আপডেট
            self.arr[idx] = value
            self.tree[node] = value
            return
        
        mid = (start + end) // 2
        if start <= idx <= mid:
            # বাম সাবট্রিতে
            self.update(idx, value, 2 * node + 1, start, mid)
        else:
            # ডান সাবট্রিতে
            self.update(idx, value, 2 * node + 2, mid + 1, end)
        
        # বর্তমান নোড আপডেট
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

# উদাহরণ ব্যবহার
arr = [1, 2, 3, 4, 5, 6, 7, 8]
st = SegmentTree(arr)

print("মূল অ্যারে:", arr)
print("0 থেকে 3 যোগফল:", st.query(0, 3))  # 1+2+3+4 = 10
print("2 থেকে 5 যোগফল:", st.query(2, 5))  # 3+4+5+6 = 18

# আপডেট
st.update(3, 10)  # ইনডেক্স 3 এ মান 10
print("\nআপডেট পর 0 থেকে 3 যোগফল:", st.query(0, 3))  # 1+2+3+10 = 16
```

### ২. সর্বোচ্চ মানের জন্য সেগমেন্ট ট্রি

```python
class SegmentTreeMax:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return
        
        mid = (start + end) // 2
        self.build(2 * node + 1, start, mid)
        self.build(2 * node + 2, mid + 1, end)
        
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def query_max(self, l, r, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        
        if r < start or l > end:
            return float('-inf')
        
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_max = self.query_max(l, r, 2 * node + 1, start, mid)
        right_max = self.query_max(l, r, 2 * node + 2, mid + 1, end)
        
        return max(left_max, right_max)
    
    def update(self, idx, value, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        
        if start == end:
            self.arr[idx] = value
            self.tree[node] = value
            return
        
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(idx, value, 2 * node + 1, start, mid)
        else:
            self.update(idx, value, 2 * node + 2, mid + 1, end)
        
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

# উদাহরণ
arr = [1, 5, 3, 7, 2, 9, 4, 6]
st_max = SegmentTreeMax(arr)

print("মূল অ্যারে:", arr)
print("0 থেকে 3 সর্বোচ্চ:", st_max.query_max(0, 3))  # max(1,5,3,7) = 7
print("2 থেকে 5 সর্বোচ্চ:", st_max.query_max(2, 5))  # max(3,7,2,9) = 9

st_max.update(4, 10)
print("\nআপডেট পর 2 থেকে 5 সর্বোচ্চ:", st_max.query_max(2, 5))  # max(3,7,10,9) = 10
```

### ৩. লেজি প্রোপাগেশন সহ সেগমেন্ট ট্রি (রেঞ্জ আপডেট)

```python
class SegmentTreeLazy:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return
        
        mid = (start + end) // 2
        self.build(2 * node + 1, start, mid)
        self.build(2 * node + 2, mid + 1, end)
        
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def update_range(self, l, r, value, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        
        # লেজি ভ্যালু প্রয়োগ
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                # লেজি ভ্যালু চাইল্ডে পাঠানো
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0
        
        # বাইরের রেঞ্জ
        if start > end or start > r or end < l:
            return
        
        # সম্পূর্ণ ওভারল্যাপ
        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * value
            if start != end:
                self.lazy[2 * node + 1] += value
                self.lazy[2 * node + 2] += value
            return
        
        # আংশিক ওভারল্যাপ
        mid = (start + end) // 2
        self.update_range(l, r, value, 2 * node + 1, start, mid)
        self.update_range(l, r, value, 2 * node + 2, mid + 1, end)
        
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query_range(self, l, r, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        
        # লেজি ভ্যালু প্রয়োগ
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0
        
        # বাইরের রেঞ্জ
        if start > end or start > r or end < l:
            return 0
        
        # সম্পূর্ণ ওভারল্যাপ
        if start >= l and end <= r:
            return self.tree[node]
        
        # আংশিক ওভারল্যাপ
        mid = (start + end) // 2
        left_sum = self.query_range(l, r, 2 * node + 1, start, mid)
        right_sum = self.query_range(l, r, 2 * node + 2, mid + 1, end)
        
        return left_sum + right_sum

# উদাহরণ
arr = [1, 2, 3, 4, 5]
st_lazy = SegmentTreeLazy(arr)

print("মূল অ্যারে:", arr)
print("0 থেকে 2 যোগফল:", st_lazy.query_range(0, 2))  # 1+2+3 = 6

# রেঞ্জ আপডেট: ইন্ডেক্স 1 থেকে 3 পর্যন্ত সবাইকে 2 যোগ করো
st_lazy.update_range(1, 3, 2)
print("\nরেঞ্জ আপডেট পর:")
print("0 থেকে 2 যোগফল:", st_lazy.query_range(0, 2))  # 1+4+5 = 10
print("1 থেকে 4 যোগফল:", st_lazy.query_range(1, 4))  # 4+5+6+5 = 20
```

## সমস্যা সমাধানের উদাহরণ

### সমস্যা ১: রেঞ্জ যোগফল কুয়েরি
```python
def range_sum_queries(arr, queries):
    """
    arr: ইনপুট অ্যারে
    queries: লিস্ট অফ (type, params)
             type=1: query(l, r)
             type=2: update(idx, value)
    """
    st = SegmentTree(arr)
    results = []
    
    for query_type, *params in queries:
        if query_type == 1:
            l, r = params
            results.append(st.query(l, r))
        elif query_type == 2:
            idx, value = params
            st.update(idx, value)
    
    return results

# টেস্ট
arr = [1, 3, 5, 7, 9, 11]
queries = [
    (1, 1, 3),   # ইনডেক্স 1 থেকে 3 যোগফল
    (2, 1, 10),  # ইনডেক্স 1 আপডেট করে 10
    (1, 1, 3)    # আবার ইনডেক্স 1 থেকে 3 যোগফল
]

print(range_sum_queries(arr, queries))  # [15, 22]
```

### সমস্যা ২: সর্বোচ্চ রেঞ্জ কুয়েরি
```python
def range_max_queries(arr, queries):
    st = SegmentTreeMax(arr)
    results = []
    
    for query_type, *params in queries:
        if query_type == 1:
            l, r = params
            results.append(st.query_max(l, r))
        elif query_type == 2:
            idx, value = params
            st.update(idx, value)
    
    return results

# টেস্ট
arr = [2, 8, 3, 7, 1, 9]
queries = [
    (1, 0, 2),   # 0-2 সর্বোচ্চ
    (1, 2, 5),   # 2-5 সর্বোচ্চ
    (2, 3, 12),  # ইনডেক্স 3 আপডেট 12
    (1, 1, 4)    # 1-4 সর্বোচ্চ
]

print(range_max_queries(arr, queries))  # [8, 9, 12]
```

## সময় জটিলতা বিশ্লেষণ

| অপারেশন | সাধারণ অ্যারে | সেগমেন্ট ট্রি |
|---------|--------------|---------------|
| রেঞ্জ কুয়েরি | O(n) | O(log n) |
| সিঙ্গেল আপডেট | O(1) | O(log n) |
| রেঞ্জ আপডেট | O(n) | O(log n) (লেজি সহ) |
| স্পেস | O(n) | O(4n) ≈ O(n) |

## উপসংহার
সেগমেন্ট ট্রি খুব শক্তিশালী ডেটা স্ট্রাকচার। যদিও শুরুতে একটু জটিল মনে হতে পারে, কিন্তু একবার বুঝে গেলে অনেক জটিল সমস্যা সহজেই সমাধান করা যায়। লেজি প্রোপাগেশন শিখলে আরও এডভান্সড অপটিমাইজেশন সম্ভব।