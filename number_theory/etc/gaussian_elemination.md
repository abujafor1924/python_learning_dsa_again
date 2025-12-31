# **গাউসিয়ান ইলিমিনেশন: সহজ বাংলায় ব্যাখ্যা**

## **গাউসিয়ান ইলিমিনেশন কী?**

**গাউসিয়ান ইলিমিনেশন** হলো অনেকগুলো সমীকরণ একসাথে সমাধান করার একটি পদ্ধতি। এটিকে "**রো রিডাকশন**" বা "**সিম্পল অ্যালগোরিদম**"ও বলা হয়।

### **সরল উদাহরণ:**
ধরি, আপনার কাছে ২টি সমীকরণ আছে:
```
2x +  y = 5   ... (1)
 x + 2y = 4   ... (2)
```

## **মৌলিক ধারণা: ৩টি সহজ অপারেশন**

### **১. রো সুইচ (Row Swap)**
দুইটি সমীকরণের স্থান বিনিময়
```python
# আগে:     পরে:
# Eq1: a   Eq1: b  
# Eq2: b   Eq2: a
```

### **২. রো মাল্টিপ্লিকেশন (Row Multiply)**
একটি সমীকরণকে একটি সংখ্যা দিয়ে গুণ করা
```python
# 2x + y = 5 কে ২ দিয়ে গুণ করলে:
# 4x + 2y = 10
```

### **৩. রো অ্যাডিশন (Row Addition)**
একটি সমীকরণকে অন্য সমীকরণের সাথে যোগ করা
```python
# Eq1: 2x + y = 5
# Eq2: x + 2y = 4
# Eq2 + Eq1: (2x+x) + (y+2y) = (5+4)
#         3x + 3y = 9
```

## **হাতে-কলমে উদাহরণ**

### **সমস্যা:**
```
1)  2x +  y +  z =  5
2)  4x - 6y      = -2
3) -2x + 7y + 2z =  9
```

### **ধাপে ধাপে সমাধান:**

**ধাপ ১:** প্রথম সমীকরণকে এমনভাবে তৈরি করি যেন প্রথম চলক (x) সহগ = 1 হয়
```
2x + y + z = 5  → (1) ÷ 2
x + 0.5y + 0.5z = 2.5  ... নতুন (1)
```

**ধাপ ২:** দ্বিতীয় ও তৃতীয় সমীকরণ থেকে x বাদ দেই
```
(2) - 4×(1): (4x-6y) - 4(x+0.5y+0.5z) = -2 - 4×2.5
→ -8y - 2z = -12  ... নতুন (2)

(3) + 2×(1): (-2x+7y+2z) + 2(x+0.5y+0.5z) = 9 + 2×2.5
→ 8y + 3z = 14  ... নতুন (3)
```

**ধাপ ৩:** এখন সমীকরণগুলো:
```
(1) x + 0.5y + 0.5z = 2.5
(2) -8y - 2z = -12
(3) 8y + 3z = 14
```

**ধাপ ৪:** (2) এবং (3) যোগ করি y বাদ দিতে:
```
(2) + (3): (-8y-2z) + (8y+3z) = -12 + 14
→ z = 2
```

**ধাপ ৫:** z=2 (2) তে বসাই:
```
-8y - 2×2 = -12
-8y - 4 = -12
-8y = -8
y = 1
```

**ধাপ ৬:** y=1, z=2 (1) তে বসাই:
```
x + 0.5×1 + 0.5×2 = 2.5
x + 0.5 + 1 = 2.5
x + 1.5 = 2.5
x = 1
```

**উত্তর:** x=1, y=1, z=2 ✅

## **পাইথন কোড - ৩×৩ ম্যাট্রিক্সের জন্য**

```python
def gaussian_elimination_3x3():
    """
    ৩টি সমীকরণের জন্য গাউসিয়ান ইলিমিনেশন
    সমীকরণগুলো:
    2x + y + z = 5
    4x - 6y = -2
    -2x + 7y + 2z = 9
    """
    # ম্যাট্রিক্স আকারে সমীকরণগুলো
    # [a, b, c, d] মানে: a*x + b*y + c*z = d
    matrix = [
        [2, 1, 1, 5],    # সমীকরণ ১
        [4, -6, 0, -2],  # সমীকরণ ২
        [-2, 7, 2, 9]    # সমীকরণ ৩
    ]
    
    # ধাপ ১: ফরওয়ার্ড ইলিমিনেশন
    n = 3  # চলকের সংখ্যা
    
    print("মূল ম্যাট্রিক্স:")
    for row in matrix:
        print(f"{row[0]}x + {row[1]}y + {row[2]}z = {row[3]}")
    print()
    
    # প্রতিটি চলকের জন্য
    for i in range(n):
        # পিভট এলিমেন্ট শূন্য হলে রো সুইচ
        if matrix[i][i] == 0:
            for j in range(i+1, n):
                if matrix[j][i] != 0:
                    # রো সুইচ
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    print(f"রো {i+1} এবং {j+1} সুইচ করা হয়েছে")
                    break
        
        # পিভট এলিমেন্টকে 1 বানানো
        pivot = matrix[i][i]
        if pivot != 0:
            for k in range(i, n+1):
                matrix[i][k] /= pivot
        
        # নিচের রোগুলোর জন্য ইলিমিনেশন
        for j in range(i+1, n):
            factor = matrix[j][i]
            for k in range(i, n+1):
                matrix[j][k] -= factor * matrix[i][k]
        
        print(f"\nধাপ {i+1} পর:")
        for row in matrix:
            print(f"[{row[0]:.1f}, {row[1]:.1f}, {row[2]:.1f} | {row[3]:.1f}]")
    
    # ধাপ ২: ব্যাকওয়ার্ড সাবস্টিটিউশন
    solution = [0, 0, 0]
    
    for i in range(n-1, -1, -1):
        solution[i] = matrix[i][n]
        for j in range(i+1, n):
            solution[i] -= matrix[i][j] * solution[j]
    
    print(f"\nসমাধান:")
    print(f"x = {solution[0]:.2f}")
    print(f"y = {solution[1]:.2f}")
    print(f"z = {solution[2]:.2f}")
    
    return solution

# কোড রান করুন
print("=== গাউসিয়ান ইলিমিনেশন (৩×৩) ===")
result = gaussian_elimination_3x3()
```

## **সাধারণ ম্যাট্রিক্সের জন্য পাইথন কোড**

```python
def gaussian_elimination(A, b):
    """
    সাধারণ গাউসিয়ান ইলিমিনেশন
    A: সহগ ম্যাট্রিক্স (n x n)
    b: ধ্রুবক ভেক্টর (n)
    """
    n = len(A)
    
    # অগমেন্টেড ম্যাট্রিক্স তৈরি [A | b]
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    
    # ফরওয়ার্ড ইলিমিনেশন
    for i in range(n):
        # পিভট নির্বাচন
        max_row = i
        for j in range(i+1, n):
            if abs(M[j][i]) > abs(M[max_row][i]):
                max_row = j
        
        # রো সুইচ
        M[i], M[max_row] = M[max_row], M[i]
        
        # পিভট শূন্য হলে সমাধান নেই
        if abs(M[i][i]) < 1e-10:
            return None
        
        # বর্তমান রোকে নরমালাইজ
        pivot = M[i][i]
        for j in range(i, n+1):
            M[i][j] /= pivot
        
        # নিচের রো থেকে চলক বাদ
        for j in range(i+1, n):
            factor = M[j][i]
            for k in range(i, n+1):
                M[j][k] -= factor * M[i][k]
    
    # ব্যাকওয়ার্ড সাবস্টিটিউশন
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = M[i][n]
        for j in range(i+1, n):
            x[i] -= M[i][j] * x[j]
    
    return x

# উদাহরণ: ৩টি সমীকরণ
A = [
    [2, 1, 1],
    [4, -6, 0],
    [-2, 7, 2]
]
b = [5, -2, 9]

print("\n=== সাধারণ ম্যাট্রিক্সের জন্য ===")
solution = gaussian_elimination(A, b)
if solution:
    print(f"সমাধান: x={solution[0]:.2f}, y={solution[1]:.2f}, z={solution[2]:.2f}")
else:
    print("সমাধান নেই")
```

## **২×২ ম্যাট্রিক্সের জন্য সহজ কোড**

```python
def solve_2x2(a1, b1, c1, a2, b2, c2):
    """
    ২টি সমীকরণ সমাধান:
    a1*x + b1*y = c1
    a2*x + b2*y = c2
    """
    # ক্রেমার'স রুল ব্যবহার (সরল পদ্ধতি)
    det = a1*b2 - a2*b1
    
    if abs(det) < 0.000001:
        return None  # সমাধান নেই বা অসংখ্য সমাধান
    
    x = (c1*b2 - c2*b1) / det
    y = (a1*c2 - a2*c1) / det
    
    return x, y

# উদাহরণ
print("\n=== ২টি সমীকরণের সহজ সমাধান ===")
eq1 = "2x + 3y = 8"
eq2 = "4x - y = 2"

# সহজে চোখে দেখা সমাধান
x, y = solve_2x2(2, 3, 8, 4, -1, 2)
print(f"সমীকরণ: {eq1}")
print(f"          {eq2}")
print(f"সমাধান: x = {x}, y = {y}")

# যাচাই
print(f"\nযাচাই:")
print(f"{eq1}: 2*{x} + 3*{y} = {2*x + 3*y} (আসল: 8)")
print(f"{eq2}: 4*{x} - {y} = {4*x - y} (আসল: 2)")
```

## **গাউস-জর্ডান মেথড (সরল সংস্করণ)**

```python
def gauss_jordan_simple(A, b):
    """
    গাউস-জর্ডান মেথড - আরও সরল
    """
    n = len(A)
    
    # অগমেন্টেড ম্যাট্রিক্স
    M = [A[i] + [b[i]] for i in range(n)]
    
    print("শুরুতে:")
    for row in M:
        print(row)
    
    # প্রতিটি কলামের জন্য
    for col in range(n):
        # পিভট সারি খুঁজা
        pivot_row = col
        for row in range(col+1, n):
            if abs(M[row][col]) > abs(M[pivot_row][col]):
                pivot_row = row
        
        # পিভট সারি নিয়ে আসা
        M[col], M[pivot_row] = M[pivot_row], M[col]
        
        # পিভট সারি নরমালাইজ
        pivot = M[col][col]
        for j in range(col, n+1):
            M[col][j] /= pivot
        
        # অন্য সব সারি থেকে চলক বাদ
        for row in range(n):
            if row != col:
                factor = M[row][col]
                for j in range(col, n+1):
                    M[row][j] -= factor * M[col][j]
        
        print(f"\nকলাম {col+1} পর:")
        for r in M:
            print([round(val, 2) for val in r])
    
    # সমাধান
    solution = [M[i][n] for i in range(n)]
    return solution

# টেস্ট
print("\n=== গাউস-জর্ডান মেথড ===")
A_simple = [[1, 2], [3, 4]]
b_simple = [5, 6]

sol = gauss_jordan_simple(A_simple, b_simple)
print(f"\nসমাধান: x={sol[0]}, y={sol[1]}")
```

## **প্র্যাকটিসের জন্য সমস্যা**

```python
def practice_problems():
    """
    প্র্যাকটিস করার জন্য সমস্যা
    """
    print("=== প্র্যাকটিস সমস্যা ===\n")
    
    # সমস্যা ১: সহজ
    print("১. নিচের সমীকরণগুলো সমাধান কর:")
    print("   3x + 2y = 7")
    print("   2x - y = 1")
    
    # সমাধান চেক
    def check_solution_1(x, y):
        eq1 = 3*x + 2*y
        eq2 = 2*x - y
        return abs(eq1-7) < 0.001 and abs(eq2-1) < 0.001
    
    # সমস্যা ২: ৩ চলক
    print("\n২. সমাধান কর:")
    print("   x + y + z = 6")
    print("   2x + y + 3z = 14")
    print("   x + 3y + z = 10")
    
    # সমস্যা ৩: বাস্তব জীবনের সমস্যা
    print("\n৩. রিয়েল লাইফ সমস্যা:")
    print("   আপেলের দাম x, কমলার দাম y, আঙুরের দাম z")
    print("   2 আপেল + 3 কমলা = 170 টাকা")
    print("   1 আপেল + 2 আঙুর = 150 টাকা")
    print("   3 কমলা + 1 আঙুর = 130 টাকা")
    print("   প্রতিটির দাম কত?")

practice_problems()

# সমস্যা ১ এর সমাধান
print("\n=== সমস্যা ১ এর সমাধান ===")
solution1 = solve_2x2(3, 2, 7, 2, -1, 1)
if solution1:
    x, y = solution1
    print(f"x = {x}, y = {y}")
    print(f"যাচাই: 3*{x} + 2*{y} = {3*x + 2*y} (আসল 7)")
    print(f"       2*{x} - {y} = {2*x - y} (আসল 1)")
```

## **গাউসিয়ান ইলিমিনেশনের গুরুত্বপূর্ণ বিষয়**

### **কখন কাজ করবে না?**
1. **পিভট শূন্য হলে** - রো সুইচ করে দেখতে হবে
2. **সকল পিভট শূন্য হলে** - সমাধান নেই বা অসংখ্য সমাধান
3. **সমীকরণ কম/বেশি হলে** - অনন্য সমাধান নাও থাকতে পারে

### **যেভাবে কাজ করে:**
```
ধাপ ১: 
[2, 1, 1 | 5]
[4,-6, 0 |-2]
[-2,7, 2 | 9]

ধাপ ২: (ইলিমিনেশন পর)
[1, 0.5, 0.5 | 2.5]
[0,  -8,  -2 |-12]
[0,   8,   3 | 14]

ধাপ ৩: (আরও ইলিমিনেশন)
[1, 0, 0 | 1]
[0, 1, 0 | 1]
[0, 0, 1 | 2]
```

### **সহজ সূত্র মনে রাখুন:**
1. **সরল করো** - প্রতিটি সমীকরণ সরল করো
2. **একঘাত করো** - একই চলকের সহগ এক করো
3. **বাতিল করো** - যোগ/বিয়োগ করে চলক কমাও
4. **সমাধান করো** - পিছন থেকে মান বের করো

## **চোখে দেখার জন্য গ্রাফিকাল উদাহরণ**

```python
def visual_example():
    """
    গ্রাফিকাল উদাহরণ
    2x + y = 5
    x + 2y = 4
    """
    import matplotlib.pyplot as plt
    import numpy as np
    
    # প্রথম সমীকরণ: 2x + y = 5 → y = 5 - 2x
    x = np.linspace(0, 3, 100)
    y1 = 5 - 2*x
    
    # দ্বিতীয় সমীকরণ: x + 2y = 4 → y = (4 - x)/2
    y2 = (4 - x)/2
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label='2x + y = 5', linewidth=2)
    plt.plot(x, y2, label='x + 2y = 4', linewidth=2)
    
    # ছেদ বিন্দু (সমাধান)
    # সমাধান: x=2, y=1
    plt.plot(2, 1, 'ro', markersize=10, label=f'সমাধান: (2, 1)')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('গাউসিয়ান ইলিমিনেশন: দুইটি সরলরেখার ছেদ')
    plt.grid(True)
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

# গ্রাফ দেখতে চাইলে (যদি matplotlib থাকে)
try:
    # visual_example()  # এটা আনকমেন্ট করলে গ্রাফ দেখাবে
    print("গ্রাফ দেখাতে matplotlib ব্যবহার করুন")
except:
    print("গ্রাফ দেখাতে matplotlib ইনস্টল করুন")
```

## **সারসংক্ষেপ:**

### **৩টি সহজ ধাপ:**
1. **আগের দিকে কমাও (Forward Elimination)**
   - উপর থেকে নিচে চলক বাদ দাও
   - ম্যাট্রিক্সকে ত্রিভুজ আকারে আনো

2. **পিছনের দিকে বের করো (Back Substitution)**
   - নিচ থেকে উপর দিকে মান বের করো

3. **যাচাই করো (Verify)**
   - সমাধানটি মূল সমীকরণে বসিয়ে দেখো

### **মনে রাখার টিপস:**
- **পিভট** = কর্নারের সংখ্যা (শূন্য হলে সমস্যা)
- **রো অপারেশন** = সমীকরণে পরিবর্তন
- **ত্রিভুজ আকার** = লক্ষ্য অর্জন

**সবচেয়ে সহজ কোড (২×২):**
```python
def simple_solve(a, b, c, d, e, f):
    """ax + by = e, cx + dy = f"""
    det = a*d - b*c
    if det == 0:
        return None
    x = (e*d - b*f) / det
    y = (a*f - e*c) / det
    return x, y
```