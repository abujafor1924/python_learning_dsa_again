# 0-1 মেট্রিক্সে সবচেয়ে বড় আয়তক্ষেত্রের এলাকা (Maximum Rectangle in 0-1 Matrix)

## সমস্যার বিবরণ
আমাদের একটি 0 এবং 1 দিয়ে গঠিত 2D ম্যাট্রিক্স দেওয়া হয়েছে। আমাদের এমন বৃহত্তম আয়তক্ষেত্র খুঁজে বের করতে হবে যার সবগুলো সেলের মান 1 হবে।

## উদাহরণ

**ইনপুট:**
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

**আউটপুট:** 6

ব্যাখ্যা:
```
1 0 1 0 0
1 0 1 1 1    ← এই আয়তক্ষেত্রটির আকার = 2 × 3 = 6
1 1 1 1 1
1 0 0 1 0
```

## সমাধানের ধারণা

### ধাপ ১: প্রতি সারির হিস্ট্রোগ্রাম তৈরি করা
প্রতি সারিকে একটি হিস্ট্রোগ্রাম হিসেবে কল্পনা করি, যেখানে প্রতিটি কলামের উচ্চতা হবে উপরের সারিতে কতটি পরপর 1 আছে তার সংখ্যা।

উপরের উদাহরণের জন্য:

**সারি ০:** `[1, 0, 1, 0, 0]`

**সারি ১:** `[2, 0, 2, 1, 1]`

**সারি ২:** `[3, 1, 3, 2, 2]`

**সারি ৩:** `[4, 0, 0, 3, 0]`

### ধাপ ২: হিস্ট্রোগ্রামে সবচেয়ে বড় আয়তক্ষেত্র বের করা
প্রতি সারির হিস্ট্রোগ্রামে আমরা "Largest Rectangle in Histogram" এলগরিদম প্রয়োগ করব।

## বিস্তারিত অ্যালগরিদম

```python
def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # হিস্ট্রোগ্রাম অ্যারেতে কলামের উচ্চতা স্টোর করব
    heights = [0] * cols
    max_area = 0
    
    for i in range(rows):
        # বর্তমান সারির জন্য heights আপডেট করি
        for j in range(cols):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        
        # হিস্ট্রোগ্রামে বৃহত্তম আয়তক্ষেত্র বের করি
        max_area = max(max_area, largestRectangleInHistogram(heights))
    
    return max_area
```

## হিস্ট্রোগ্রামে বৃহত্তম আয়তক্ষেত্র বের করার ফাংশন

```python
def largestRectangleInHistogram(heights):
    stack = []  # মনোটোনিক ইনক্রিসিং স্ট্যাক
    max_area = 0
    n = len(heights)
    
    for i in range(n):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    # স্ট্যাকের বাকি এলিমেন্টগুলোর জন্য
    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area
```

## সম্পূর্ণ কোড উদাহরণ

```python
def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # হিস্ট্রোগ্রামের উচ্চতা স্টোর করার অ্যারে
    heights = [0] * (cols + 1)  # +1 করি শেষের এলিমেন্ট প্রসেস করার জন্য
    max_area = 0
    
    for i in range(rows):
        # বর্তমান সারির জন্য heights আপডেট
        for j in range(cols):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        
        # মনোটোনিক স্ট্যাক ব্যবহার করে সর্বোচ্চ আয়তক্ষেত্র বের করি
        stack = []
        for j in range(cols + 1):
            while stack and heights[j] < heights[stack[-1]]:
                height = heights[stack.pop()]
                # width নির্ধারণ
                width = j if not stack else j - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(j)
    
    return max_area

# উদাহরণ ম্যাট্রিক্স
matrix = [
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]

print("Maximum rectangle area:", maximalRectangle(matrix))  # Output: 6
```

## ভিজুয়ালাইজেশন

ম্যাট্রিক্স:
```
ইন্ডেক্স: 0  1  2  3  4
সারি 0:  1  0  1  0  0
সারি 1:  1  0  1  1  1
সারি 2:  1  1  1  1  1
সারি 3:  1  0  0  1  0
```

**সারি ২ পর্যন্ত হিস্ট্রোগ্রাম:** `[3, 1, 3, 2, 2]`

হিস্ট্রোগ্রাম:
```
    █
    █
█   █
█ █ █ █ █
3 1 3 2 2
```

সবচেয়ে বড় আয়তক্ষেত্র: উচ্চতা = 2, প্রস্থ = 3, এলাকা = 6

## টাইম ও স্পেস কমপ্লেক্সিটি

- **টাইম কমপ্লেক্সিটি:** O(rows × cols)
  - প্রতি সারির জন্য O(cols) হিস্ট্রোগ্রাম আপডেট
  - প্রতি সারির জন্য O(cols) হিস্ট্রোগ্রাম প্রসেস
  
- **স্পেস কমপ্লেক্সিটি:** O(cols)
  - heights অ্যারে স্টোর করার জন্য
  - স্ট্যাক স্টোর করার জন্য

## বিকল্প অ্যাপ্রোচ

### 1. ডাইনামিক প্রোগ্রামিং অ্যাপ্রোচ
```python
def maximalRectangleDP(matrix):
    if not matrix:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    left = [0] * cols
    right = [cols] * cols
    height = [0] * cols
    max_area = 0
    
    for i in range(rows):
        current_left = 0
        current_right = cols
        
        # height আপডেট
        for j in range(cols):
            if matrix[i][j] == '1':
                height[j] += 1
            else:
                height[j] = 0
        
        # left আপডেট
        for j in range(cols):
            if matrix[i][j] == '1':
                left[j] = max(left[j], current_left)
            else:
                left[j] = 0
                current_left = j + 1
        
        # right আপডেট
        for j in range(cols-1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], current_right)
            else:
                right[j] = cols
                current_right = j
        
        # এলাকা ক্যালকুলেট
        for j in range(cols):
            max_area = max(max_area, height[j] * (right[j] - left[j]))
    
    return max_area
```

## প্রাকটিস প্রবলেম

### ছোট উদাহরণ:
```python
matrix1 = [
    ['1', '0'],
    ['1', '1']
]
# আউটপুট: 2

matrix2 = [
    ['1', '1', '1'],
    ['0', '1', '1'],
    ['1', '0', '0']
]
# আউটপুট: 4

matrix3 = [
    ['0', '0', '0'],
    ['0', '0', '0'],
    ['0', '0', '0']
]
# আউটপুট: 0

matrix4 = [
    ['1', '1', '1'],
    ['1', '1', '1'],
    ['1', '1', '1']
]
# আউটপুট: 9
```

## বাংলায় টিপস

1. **স্ট্যাকের ব্যবহার:** মনোটোনিক ইনক্রিসিং স্ট্যাক ব্যবহার করে হিস্ট্রোগ্রামের সমস্যা সমাধান করা যায়
2. **কম্প্রেশন:** প্রতিটি সারিকে আলাদা হিস্ট্রোগ্রাম হিসেবে দেখা যায়
3. **ডাইনামিক প্রোগ্রামিং:** left, right, height অ্যারে বজায় রেখে সমাধান করা যায়
4. **এজ কেস:** খালি ম্যাট্রিক্স, সব 0, সব 1 - এই কেসগুলো মাথায় রাখতে হবে

এই সমস্যাটি অনেক কম্পিটিটিভ প্রোগ্রামিং এবং টেকনিক্যাল ইন্টারভিউতে আসে। হিস্ট্রোগ্রামের ধারণা বুঝলে এই সমস্যা সমাধান করা সহজ হয়ে যায়।