# **সাইকেল থিওরি সরল ব্যাখ্যা ও পাইথন উদাহরণ**

## **সাইকেল কী?**
**সাইকেল** মানে হলো "চক্র" বা "লূপ"। যখন কোনো জিনিস আবার তার শুরুর কাছে ফিরে আসে, তখন সাইকেল তৈরি হয়।

### **রিয়েল লাইফ উদাহরণ:**
1. **ঘড়ির কাঁটা** - ১২টা থেকে শুরু করে আবার ১২তায় ফিরে আসে
2. **গোল চাকার ঘূর্ণন** - একই পয়েন্টে ফিরে আসে
3. **লিফটের উঠানামা** - একই ফ্লোরে ফিরে আসা

## **কম্পিউটার সাইন্সে সাইকেলের উদাহরণ:**

### **১. লিংকড লিস্ট সাইকেল**
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# সাইকেল ছাড়া লিংকড লিস্ট তৈরি
def create_list_no_cycle():
    """1 → 2 → 3 → 4 → 5 → None"""
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    # n5.next = None (ডিফল্ট)
    return n1

# সাইকেল সহ লিংকড লিস্ট তৈরি
def create_list_with_cycle():
    """1 → 2 → 3 → 4 → 5 → 3 (সাইকেল)"""
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n3  # এখানে সাইকেল! ৫ আবার ৩-এ ফিরে গেল
    return n1

# সহজ সাইকেল চেক
def has_cycle_simple(head):
    """
    সাইকেল আছে কিনা চেক করার সহজ উপায়
    ট্র্যাক রাখি কোন নোডগুলো দেখা হয়েছে
    """
    visited = set()  # দেখা নোডগুলো রাখব
    current = head
    
    while current:
        if current in visited:
            return True  # সাইকেল পাওয়া গেছে!
        visited.add(current)
        current = current.next
    
    return False  # সাইকেল নেই

# টেস্ট করি
print("সাইকেল ছাড়া লিস্ট:")
list1 = create_list_no_cycle()
print(f"সাইকেল আছে? {has_cycle_simple(list1)}")  # False

print("\nসাইকেল সহ লিস্ট:")
list2 = create_list_with_cycle()
print(f"সাইকেল আছে? {has_cycle_simple(list2)}")  # True
```

### **২. টরটোইজ অ্যান্ড হেয়ার (ফ্লয়েড) অ্যালগোরিদম**
```python
def has_cycle_floyd(head):
    """
    ফ্লয়েডের টরটোইজ অ্যান্ড হেয়ার অ্যালগোরিদম
    - ২টি পয়েন্টার ব্যবহার করে: slow (ধীর) এবং fast (দ্রুত)
    - slow ১ ধাপ করে যায়, fast ২ ধাপ করে যায়
    - যদি সাইকেল থাকে, তাহলে fast ও slow কখনো না কখনো মিলে যাবে
    """
    if not head or not head.next:
        return False
    
    slow = head  # কচ্ছপ (ধীর)
    fast = head  # খরগোশ (দ্রুত)
    
    while fast and fast.next:
        slow = slow.next        # ১ ধাপ
        fast = fast.next.next   # ২ ধাপ
        
        if slow == fast:        # মিলে গেছে = সাইকেল আছে!
            return True
    
    return False  # fast শেষে পৌঁছাল = সাইকেল নেই

# আরেকটা উদাহরণ দেখি
def detect_cycle_details(head):
    """
    শুধু সাইকেল আছে কিনা না, সাইকেলের শুরুও খুঁজে বের করে
    """
    if not head or not head.next:
        return None
    
    # প্রথমে সাইকেল আছে কিনা চেক
    slow = head
    fast = head
    has_cycle = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            has_cycle = True
            break
    
    if not has_cycle:
        return None
    
    # সাইকেলের শুরু খুঁজে বের করা
    # slow কে শুরুতে নিয়ে আসি, fast সাইকেলে রাখি
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow  # সাইকেল যেখান থেকে শুরু

# টেস্ট
print("\n=== টরটোইজ অ্যান্ড হেয়ার অ্যালগোরিদম ===")
list_with_cycle = create_list_with_cycle()
cycle_start = detect_cycle_details(list_with_cycle)

if cycle_start:
    print(f"সাইকেল আছে!")
    print(f"সাইকেল শুরু হয় নোড: {cycle_start.value}")  # 3
else:
    print("সাইকেল নেই")
```

### **৩. সংখ্যার সাইকেল উদাহরণ**
```python
def number_cycle_example():
    """
    সংখ্যার সাইকেল: একটি ফাংশন বারবার অ্যাপ্লাই করলে
    একই সংখ্যায় ফিরে আসে কিনা
    """
    def happy_number_cycle(n):
        """
        হ্যাপি নাম্বার প্রোব্লেম: 
        একটি সংখ্যার প্রতিটি ডিজিটের বর্গের যোগফল বারবার করলে
        ১ পাওয়া যায় = হ্যাপি নাম্বার
        সাইকেলে পড়ে = আনহ্যাপি নাম্বার
        """
        def sum_of_squares(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        slow = n
        fast = n
        
        while True:
            slow = sum_of_squares(slow)          # ১ ধাপ
            fast = sum_of_squares(sum_of_squares(fast))  # ২ ধাপ
            
            if fast == 1:
                return True  # হ্যাপি নাম্বার
            if slow == fast:
                return False  # সাইকেলে পড়েছে = আনহ্যাপি
    
    # টেস্ট
    test_numbers = [19, 4, 7, 13]
    for num in test_numbers:
        if happy_number_cycle(num):
            print(f"{num} হল হ্যাপি নাম্বার")
        else:
            print(f"{num} আনহ্যাপি (সাইকেলে পড়েছে)")

print("\n=== হ্যাপি নাম্বার সাইকেল ===")
number_cycle_example()
```

## **প্র্যাকটিস করার জন্য কোড:**
```python
# নিজে চেষ্টা করার জন্য সহজ প্র্যাকটিস
def practice_cycle_detection():
    """
    নিজে হাতে কলমে প্র্যাকটিস করুন
    """
    # ১. নোড ক্লাস
    class SimpleNode:
        def __init__(self, val):
            self.val = val
            self.next = None
    
    # ২. সাইকেল ছাড়া লিস্ট
    a = SimpleNode('A')
    b = SimpleNode('B')
    c = SimpleNode('C')
    d = SimpleNode('D')
    
    a.next = b
    b.next = c
    c.next = d
    # d.next = None (ডিফল্ট)
    
    # ৩. সাইকেল সহ লিস্ট
    x = SimpleNode('X')
    y = SimpleNode('Y')
    z = SimpleNode('Z')
    
    x.next = y
    y.next = z
    z.next = x  # সাইকেল! Z → X
    
    # ৪. সহজ চেক ফাংশন
    def check_cycle(start_node):
        seen = []
        current = start_node
        
        while current:
            if current in seen:
                return True
            seen.append(current)
            current = current.next
        
        return False
    
    # ৫. রেজাল্ট চেক
    print("সাইকেল ছাড়া লিস্ট (A→B→C→D):")
    print(f"সাইকেল আছে? {check_cycle(a)}")  # False
    
    print("\nসাইকেল সহ লিস্ট (X→Y→Z→X):")
    print(f"সাইকেল আছে? {check_cycle(x)}")  # True

print("\n=== প্র্যাকটিস সেকশন ===")
practice_cycle_detection()
```

## **কেন সাইকেল গুরুত্বপূর্ণ?**

### **প্রথমিক সমস্যাগুলো:**
1. **ডেডলক** - দুটি প্রোগ্রাম একে অপরের জন্য অপেক্ষা করছে
2. **ইনফিনিট লুপ** - প্রোগ্রাম কখনো থামছে না
3. **মেমরি লিক** - একই জিনিস বারবার তৈরি হচ্ছে

### **রিয়েল লাইফ উদাহরণ:**
```python
# ডেডলক উদাহরণ
def deadlock_example():
    """
    রেস্টুরেন্টের উদাহরণ:
    - টেবিল A: চপস্টিক ১ ও ২ লাগে
    - টেবিল B: চপস্টিক ২ ও ৩ লাগে
    - টেবিল C: চপস্টিক ৩ ও ১ লাগে
    
    সবাই একই সময়ে প্রথম চপস্টিক নিলে:
    A: চপস্টিক ১ নিল, ২ এর জন্য অপেক্ষা
    B: চপস্টিক ২ নিল, ৩ এর জন্য অপেক্ষা  
    C: চপস্টিক ৩ নিল, ১ এর জন্য অপেক্ষা
    
    কেউই খেতে পারবে না! এটাই ডেডলক (সাইকেল)
    """
    resources = {
        'চপস্টিক_১': 'A এর কাছে',
        'চপস্টিক_২': 'B এর কাছে',
        'চপস্টিক_৩': 'C এর কাছে'
    }
    
    waiting_for = {
        'A': 'চপস্টিক_২',
        'B': 'চপস্টিক_৩', 
        'C': 'চপস্টিক_১'
    }
    
    print("ডেডলক সৃষ্টি হয়েছে!")
    print("সবাই অন্যজনের কাছে থাকা জিনিসের জন্য অপেক্ষা করছে")
    print("কেউই এগোতে পারছে না - এটাই সাইকেল/ডেডলক")

print("\n=== ডেডলক উদাহরণ ===")
deadlock_example()
```

## **সারসংক্ষেপ:**

### **সাইকেল ডিটেকশনের মূল আইডিয়া:**
1. **ট্র্যাক রাখো** - কোন জিনিসগুলো দেখেছ সেটা মনে রাখ
2. **দুই পয়েন্টার** - ধীর ও দ্রুত পয়েন্টার ব্যবহার কর
3. **যদি ফিরে আসো** - একই জায়গায় ফিরে এলে সাইকেল আছে

### **সহজ ২টি নিয়ম:**
1. **লিংকড লিস্টে**: fast ও slow পয়েন্টার মিলে গেলে = সাইকেল আছে
2. **সাধারণত**: আগে দেখা জিনিস আবার দেখলে = সাইকেল আছে

### **সবচেয়ে সহজ কোড:**
```python
def easiest_cycle_check(head):
    seen = set()
    current = head
    
    while current:
        if current in seen:  # আগে দেখেছি!
            return True
        seen.add(current)
        current = current.next
    
    return False
```

**মনে রাখবেন**: সাইকেল মানেই সমস্যা নয়, অনেক অ্যালগোরিদমে (যেমন পোলার্ড'স রো) সাইকেল ব্যবহার করে দ্রুত রেজাল্ট বের করা হয়!