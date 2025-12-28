ঠিক আছে 👍
**Competitive Programming**–এর জন্য **Combinations (nCr)** পুরোটা পরিষ্কার করে, **formula + efficient Python code** সহ বুঝিয়ে দিচ্ছি।

---

## 1️⃣ Combination (nCr) কী?

Combination মানে হলো **order matter করে না**—কয়টা উপায়ে নির্বাচন করা যায়।

**Formula:**

[
nCr = \frac{n!}{r!(n-r)!}
]

**Example:**
5 জন থেকে 2 জন বাছাই
👉 (A,B) আর (B,A) একই → order গুরুত্বপূর্ণ না

---

## 2️⃣ Direct factorial ব্যবহার (Small n)

👉 **n ≤ 20–30** হলে ঠিক আছে

```python
import math

def nCr(n, r):
    if r > n:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

print(nCr(5, 2))  # 10
```

❌ Competitive programming এ বড় n এর জন্য ধীর

---

## 3️⃣ Optimized Method (No factorial)

👉 **Time efficient**
👉 Overflow কম

```python
def nCr(n, r):
    if r > n:
        return 0
    r = min(r, n - r)  # optimization
    res = 1
    for i in range(r):
        res = res * (n - i) // (i + 1)
    return res

print(nCr(10, 3))  # 120
```

✅ CP–এর জন্য খুব জনপ্রিয়

---

## 4️⃣ Modulo Combination (MOST IMPORTANT)

Competitive programming এ প্রায় সব সময় থাকে:

[
nCr \bmod (10^9+7)
]

### 🔹 Precompute factorial + inverse

👉 **Multiple queries** থাকলে best

```python
MOD = 10**9 + 7
MAXN = 10**6

fact = [1] * (MAXN + 1)
invfact = [1] * (MAXN + 1)

for i in range(1, MAXN + 1):
    fact[i] = fact[i-1] * i % MOD

invfact[MAXN] = pow(fact[MAXN], MOD-2, MOD)
for i in range(MAXN, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

def nCr(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n-r] % MOD

print(nCr(1000000, 500000))
```

✅ **O(1)** per query
🔥 CP standard solution

---

## 5️⃣ Pascal’s Identity (DP)

👉 ছোট n (≤ 1000)

[
nCr = (n-1)C(r-1) + (n-1)Cr
]

```python
N = 1000
C = [[0]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    C[i][0] = C[i][i] = 1
    for j in range(1, i):
        C[i][j] = C[i-1][j-1] + C[i-1][j]

print(C[5][2])  # 10
```

❌ বড় n এ memory heavy

---

## 6️⃣ কোনটা কখন ব্যবহার করবে?

| Situation             | Best Method          |
| --------------------- | -------------------- |
| Single query, small n | Optimized loop       |
| Multiple queries      | Precompute factorial |
| n ≤ 1000              | DP                   |
| Mod required          | Factorial + inverse  |

---

## 7️⃣ CP Tips 🔥

* সবসময় `r = min(r, n-r)`
* Mod থাকলে `pow(x, MOD-2, MOD)` ব্যবহার করো
* Python এ factorial সরাসরি বড় n এ ব্যবহার কোরো না

---

চাও তো আমি
✔ **Practice problems**
✔ **nCr vs nPr comparison**
✔ **Real CP problem solution**
✔ **Math logic explanation**

যেকোনোটা বললেই দিচ্ছি 😊
