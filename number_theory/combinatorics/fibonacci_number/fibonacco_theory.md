ঠিক আছে 🙂 আমি **Fibonacci Number** খুব সহজভাবে **theory + Python code**—দুটাই বুঝিয়ে দিচ্ছি। ধীরে ধীরে পড়ো।

---

## 🔢 Fibonacci Number কী?

**Fibonacci sequence** হলো এমন একটি সংখ্যা ধারা যেখানে
প্রতিটি সংখ্যা = তার আগের **দুটি সংখ্যার যোগফল**।

### 📌 নিয়ম (Definition)

* প্রথম দুইটি সংখ্যা:

  * F(0) = 0
  * F(1) = 1
* এরপর:

  * **F(n) = F(n−1) + F(n−2)**

---

## 🧮 উদাহরণ (Example)

প্রথম কয়েকটি Fibonacci সংখ্যা:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

ব্যাখ্যা:

* 1 = 0 + 1
* 2 = 1 + 1
* 3 = 1 + 2
* 5 = 2 + 3

---

## 🧠 কোথায় ব্যবহার হয়?

* Competitive Programming
* Dynamic Programming শেখার জন্য
* Tree, Recursion বোঝার জন্য
* Mathematics & Algorithm Design

---

## 🐍 Python এ Fibonacci (৩ ভাবে)

---

### ✅ 1️⃣ Iterative (সবচেয়ে Efficient)

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)
```

📤 Output:

```
0 1 1 2 3 5 8 13 21 34
```

⏱ Time Complexity: **O(n)**
💾 Space Complexity: **O(1)**

👉 Competitive programming-এ এইটা বেশি ব্যবহার হয়।

---

### ✅ 2️⃣ Recursive (Theory বোঝার জন্য)

```python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(6))
```

📤 Output:

```
8
```

⚠️ এটা বড় `n` এর জন্য ধীর (slow)।

⏱ Time Complexity: **O(2ⁿ)** ❌

---

### ✅ 3️⃣ Dynamic Programming (Memoization)

```python
dp = {}

def fib(n):
    if n in dp:
        return dp[n]
    if n <= 1:
        return n
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]

print(fib(10))
```

⏱ Time Complexity: **O(n)**
💾 Space: **O(n)**

---

## 🏁 Summary (সহজ করে)

| Method    | Speed | Use                     |
| --------- | ----- | ----------------------- |
| Iterative | ⭐⭐⭐   | Best for CP             |
| Recursive | ⭐     | Learning recursion      |
| DP        | ⭐⭐    | Optimization শেখার জন্য |

---

চাও তো আমি পরের ধাপে দেখাতে পারি:

* Fibonacci দিয়ে **DP problem**
* **n-th Fibonacci mod 10⁹+7**
* Competitive programming tricks

বললেই হবে 👍
