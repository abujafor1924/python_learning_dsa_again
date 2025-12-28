ঠিক আছে 😊
এখন আমি **Expectation (Expected Value)** পুরো **theory** বাংলায় step by step বুঝিয়ে দিচ্ছি, beginner থেকে Competitive Programming পর্যন্ত কাজে লাগবে।

---

# 🔹 Expected Value (Expectation) কী?

**Expected Value** মানে হলো:

> কোনো experiment repeated অনেক বার করলে **average outcome** কত হবে।

অর্থাৎ, এটা **সম্ভাবনার weighted average**।

---

## 1️⃣ Formula

### Discrete Random Variable এর জন্য:

[
E[X] = \sum (x_i \cdot P(x_i))
]

* (x_i) = outcome value
* (P(x_i)) = ওই outcome-এর probability
* Summation = সব possible outcome-এর জন্য

---

## 2️⃣ সহজ ভাষায়

* ধরো তুমি 1, 2, 3, 4, 5, 6 লেখা ডাইস ছুড়ছো
* ডাইস repeated অনেক বার ছোড়ার পরে **average number** কি হবে?
* এটা হলো **expected value**।

---

## 3️⃣ Example 1: Simple Dice

* ডাইস outcomes = 1,2,3,4,5,6
* Probability = 1/6 সবগুলোর

[
E[X] = 1\cdot\frac16 + 2\cdot\frac16 + 3\cdot\frac16 + 4\cdot\frac16 + 5\cdot\frac16 + 6\cdot\frac16
]

[
E[X] = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5
]

✅ অর্থাৎ, repeated rolling এ **average number = 3.5**

---

## 4️⃣ Example 2: Coin Toss (0/1 outcome)

* Coin: Head = 1, Tail = 0
* Probability(H) = 0.5, Probability(T) = 0.5

[
E[X] = 1\cdot 0.5 + 0\cdot 0.5 = 0.5
]

---

## 5️⃣ Important Properties of Expected Value

### 1️⃣ Linearity

[
E[aX + bY] = aE[X] + bE[Y]
]

* a,b = constants
* X,Y = random variables
* Independent or dependent হলেও চলে

### Example:

2টা independent dice:

* X = 1st dice, Y = 2nd dice
* E[X+Y] = E[X] + E[Y] = 3.5 + 3.5 = 7

---

### 2️⃣ Constant Multiplier

[
E[aX] = aE[X]
]

---

### 3️⃣ Sum of Independent Events

[
E[X+Y+Z] = E[X] + E[Y] + E[Z]
]

---

## 6️⃣ Competitive Programming Tips

1️⃣ Dice / Coin Problem → Average outcome
2️⃣ At least one success → Multiply probability & value
3️⃣ Linearity ব্যবহার করে quick solution

---

## 7️⃣ Example: CP Level Problem

**Problem:**
2টা coin toss করছো:

* Head = 2 point, Tail = 0 point
* Average score কত হবে?

**Solution:**

* Outcome:

  * HH → 4 points, P = 1/4
  * HT → 2 points, P = 1/4
  * TH → 2 points, P = 1/4
  * TT → 0 points, P = 1/4

[
E[X] = 4*(1/4) + 2*(1/4) + 2*(1/4) + 0*(1/4) = 2
]

---

## 8️⃣ Python Code Example

```python
# Dice expected value
outcomes = [1,2,3,4,5,6]
prob = 1/6

expected_value = sum(x*prob for x in outcomes)
print(expected_value)  # Output: 3.5
```

**Coin toss example:**

```python
outcomes = [0,2]  # Tail=0, Head=2
prob = 0.5

expected_value = sum(x*prob for x in outcomes)
print(expected_value)  # Output: 1.0
```

---

✅ **CP Important Note:**

* Expected value অনেক ক্ষেত্রে **linearity** ব্যবহার করে অনেক সহজে বের করা যায়।
* Fraction, decimal বা modulo–তে answer দিতে হয়, তবে formula একই।

---

যদি চাও, আমি পরের মেসেজে **CP Level Expected Value Problems + Python Solutions** তৈরি করে দেখাতে পারি।

তুমি কি সেটা চাইছো?
