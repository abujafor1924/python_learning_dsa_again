

# 📘 Python Array (List) – Theory Notes

---

## 1️⃣ Array কী? (Definition)

**Array** হলো একটি ডাটা স্ট্রাকচার যেখানে
একই নামের অধীনে **একাধিক ডাটা ধারাবাহিকভাবে (index অনুযায়ী)** সংরক্ষণ করা হয়।

📌 Python-এ Array বলতে সাধারণত **List** বোঝানো হয়।

---

## 2️⃣ Python-এ Array কেন List?

Python-এ built-in array খুব কম ব্যবহার হয়।
কারণ **List** হলো:

* সহজ
* Flexible
* Dynamic size
* Multiple data type support করে

📌 Competitive Programming ও Backend Development-এ List standard।

---

## 3️⃣ Array (List) এর বৈশিষ্ট্য

### ✔ Ordered

Element গুলো যেভাবে রাখা হয়, সেভাবেই থাকে।

```
[10, 20, 30]
```

---

### ✔ Indexed

Index শুরু হয় **0 থেকে**।

```
arr = [5, 10, 15]
Index:  0   1   2
```

---

### ✔ Mutable

Array-এর value পরিবর্তন করা যায়।

```
arr[0] = 100
```

---

### ✔ Multiple Data Type Support

```
[10, 2.5, "Python", True]
```

---

## 4️⃣ Array কেন দরকার?

Array ছাড়া:

* অনেক ভেরিয়েবল লাগে
* Loop ব্যবহার কঠিন
* Data manage করা কঠিন

Array থাকলে:

* Loop দিয়ে সব element access
* Search / Sort সহজ
* Code ছোট ও readable

---

## 5️⃣ Index (Important Concept)

Index হলো array-এর **position number**।

```
arr = [7, 14, 21, 28]
```

| Element | Index |
| ------- | ----- |
| 7       | 0     |
| 14      | 1     |
| 21      | 2     |
| 28      | 3     |

📌 Index Range = `0` থেকে `length - 1`

---

## 6️⃣ Length (দৈর্ঘ্য)

Array-এ কয়টা element আছে।

```
arr = [1, 2, 3, 4]
Length = 4
```

📌 Last index = `length - 1`

---

## 7️⃣ Traversing (Array ঘুরে দেখা)

Traversing মানে:

> একে একে সব element access করা

Concept:

* Loop ব্যবহার হয়
* Index দিয়ে element পাওয়া যায়

📌 প্রায় সব array problem-এ traversing লাগে।

---

## 8️⃣ Array Operations (Theory Only)

| Operation | কাজ              |
| --------- | ---------------- |
| Access    | element দেখা     |
| Update    | element পরিবর্তন |
| Insert    | নতুন element যোগ |
| Delete    | element বাদ      |
| Search    | element খোঁজা    |
| Sort      | element সাজানো   |

---

## 9️⃣ Static vs Dynamic Array

### 🔹 Static Array

* Size fixed
* C / C++-এ বেশি
* Fast but inflexible

### 🔹 Dynamic Array

* Size পরিবর্তনযোগ্য
* Python List
* Flexible but slightly more memory

📌 Python List = Dynamic Array

---

## 🔟 Competitive Programming-এ Array চিনবো কীভাবে?

Problem এ যদি থাকে:

* “N numbers”
* “list of integers”
* “sequence”
* “array elements”

👉 **Array ব্যবহার করতে হবে**

---

## 🔑 Important Points (Exam / Interview)

* Python-এ Array = List
* Index always starts from 0
* List is mutable
* Loop ছাড়া array meaningful না
* 90% problem array + loop দিয়ে শুরু

---

## 🧠 One Line Memory Trick

> **Array = Data + Index + Loop**

---

যদি তুমি চাও, আমি পরের নোটগুলোও **এই একই clean note format** এ দিতে পারি:
1️⃣ Array + Loop notes
2️⃣ Array Problem Thinking
3️⃣ Sorting & Searching theory
4️⃣ Competitive Programming tricks

👉 বলো, **next note কোনটা লাগবে?**
