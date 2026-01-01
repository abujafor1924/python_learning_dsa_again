# ন্যাপস্যাক সমস্যা (Knapsack Problem) বিস্তারিত বাংলায়

ন্যাপস্যাক সমস্যা হল একটি ক্লাসিক্যাল অপটিমাইজেশন সমস্যা যেখানে **সীমিত ক্ষমতার ব্যাগে** সবচেয়ে **মূল্যবান আইটেমগুলো** নির্বাচন করতে হয়।

## সমস্যার বিবরণ
একটি ব্যাগ (ন্যাপস্যাক) আছে যার **সর্বোচ্চ ভারসাম্য ক্ষমতা W**।
n টি আইটেম আছে, যার প্রতিটির:
- **ওজন**: wᵢ
- **মান**: vᵢ

**লক্ষ্য**: ব্যাগের ক্ষমতার মধ্যে থেকে এমন আইটেম নির্বাচন যাতে **মোট মান সর্বোচ্চ** হয়।

## সমস্যার ধরন
1. **০/১ ন্যাপস্যাক**: প্রতিটি আইটেম নিতে হয় পুরোপুরি (১) বা না নিতে হয় (০)
2. **ফ্র্যাকশনাল ন্যাপস্যাক**: আইটেমের ভগ্নাংশ নেওয়া যায়
3. **আনবাউন্ডেড ন্যাপস্যাক**: প্রতিটি আইটেম অসীম বার নেওয়া যায়
4. **মাল্টিপল ন্যাপস্যাক**: একাধিক ব্যাগ আছে

## ১. ০/১ ন্যাপস্যাক সমস্যা

### ডাইনামিক প্রোগ্রামিং সমাধান
```python
def knapsack_01(weights, values, capacity):
    """
    ০/১ ন্যাপস্যাক - ডাইনামিক প্রোগ্রামিং (বটম-আপ)
    
    Args:
        weights: আইটেমের ওজন তালিকা
        values: আইটেমের মান তালিকা
        capacity: ব্যাগের সর্বোচ্চ ক্ষমতা
        
    Returns:
        সর্বোচ্চ মান, নির্বাচিত আইটেমের তালিকা
    """
    n = len(weights)
    
    # DP টেবিল তৈরি [n+1][capacity+1]
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # টেবিল পপুলেট
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # আইটেম নেওয়া বা না নেওয়া - যে ভাল
                dp[i][w] = max(
                    dp[i-1][w],  # আইটেম না নিলে
                    dp[i-1][w - weights[i-1]] + values[i-1]  # আইটেম নিলে
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    # সর্বোচ্চ মান
    max_value = dp[n][capacity]
    
    # কোন আইটেমগুলো নেওয়া হয়েছে তা খুঁজে বের করা
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)  # আইটেম ইনডেক্স
            w -= weights[i-1]
    
    selected_items.reverse()
    
    return max_value, selected_items

# উদাহরণ
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

max_value, selected = knapsack_01(weights, values, capacity)
print("০/১ ন্যাপস্যাক সমস্যা:")
print(f"ওজন: {weights}")
print(f"মান: {values}")
print(f"ক্ষমতা: {capacity}")
print(f"সর্বোচ্চ মান: {max_value}")
print(f"নির্বাচিত আইটেম ইনডেক্স: {selected}")
print(f"নির্বাচিত ওজন: {[weights[i] for i in selected]}")
print(f"নির্বাচিত মান: {[values[i] for i in selected]}")
```

### স্পেস অপটিমাইজড ভার্সন
```python
def knapsack_01_optimized(weights, values, capacity):
    """
    ০/১ ন্যাপস্যাক - স্পেস অপটিমাইজড (১D অ্যারে)
    """
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # বিপরীত দিকে ইটারেট করুন
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    # সর্বোচ্চ মান
    max_value = dp[capacity]
    
    # নির্বাচিত আইটেম খুঁজে বের করা (অপশনাল)
    selected = []
    w = capacity
    for i in range(n-1, -1, -1):
        # ট্র্যাক করতে হলে মূল ডিপি ব্যবহার করতে হবে
        pass
    
    return max_value

# টেস্ট
print("\nস্পেস অপটিমাইজড ০/১ ন্যাপস্যাক:")
max_val = knapsack_01_optimized(weights, values, capacity)
print(f"সর্বোচ্চ মান: {max_val}")
```

## ২. ফ্র্যাকশনাল ন্যাপস্যাক (গ্রিডি অ্যালগরিদম)
```python
def fractional_knapsack(weights, values, capacity):
    """
    ফ্র্যাকশনাল ন্যাপস্যাক - গ্রিডি অ্যালগরিদম
    আইটেমের ভগ্নাংশ নেওয়া যায়।
    """
    n = len(weights)
    
    # মান/ওজন অনুপাত বের করুন
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append({
            'index': i,
            'weight': weights[i],
            'value': values[i],
            'ratio': ratio
        })
    
    # অনুপাতের ভিত্তিতে সর্ট (উচ্চ থেকে নিম্ন)
    items.sort(key=lambda x: x['ratio'], reverse=True)
    
    total_value = 0
    remaining_capacity = capacity
    selected = []
    
    for item in items:
        if remaining_capacity == 0:
            break
        
        if item['weight'] <= remaining_capacity:
            # পুরো আইটেম নিন
            total_value += item['value']
            remaining_capacity -= item['weight']
            selected.append({
                'index': item['index'],
                'fraction': 1.0,
                'weight_taken': item['weight'],
                'value_taken': item['value']
            })
        else:
            # আংশিক আইটেম নিন
            fraction = remaining_capacity / item['weight']
            value_taken = fraction * item['value']
            total_value += value_taken
            
            selected.append({
                'index': item['index'],
                'fraction': fraction,
                'weight_taken': remaining_capacity,
                'value_taken': value_taken
            })
            remaining_capacity = 0
    
    return total_value, selected

# উদাহরণ
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("\nফ্র্যাকশনাল ন্যাপস্যাক সমস্যা:")
print(f"ওজন: {weights}")
print(f"মান: {values}")
print(f"ক্ষমতা: {capacity}")

max_value, selected = fractional_knapsack(weights, values, capacity)
print(f"\nসর্বোচ্চ মান: {max_value:.2f}")
print("\nনির্বাচিত আইটেম:")
for item in selected:
    print(f"  আইটেম {item['index']}: {item['fraction']*100:.1f}% ({item['weight_taken']} kg, ${item['value_taken']:.2f})")
```

## ৩. আনবাউন্ডেড ন্যাপস্যাক
```python
def unbounded_knapsack(weights, values, capacity):
    """
    আনবাউন্ডেড ন্যাপস্যাক - প্রতিটি আইটেম অসীম বার নেওয়া যায়
    """
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    # প্রতিটি ক্ষমতার জন্য সর্বোচ্চ মান
    for w in range(1, capacity + 1):
        max_val = 0
        for i in range(n):
            if weights[i] <= w:
                # বর্তমান আইটেম নিলে
                current_val = dp[w - weights[i]] + values[i]
                max_val = max(max_val, current_val)
        dp[w] = max_val
    
    # নির্বাচিত আইটেম খুঁজে বের করা
    selected_counts = [0] * n
    w = capacity
    
    while w > 0:
        for i in range(n):
            if weights[i] <= w and dp[w] == dp[w - weights[i]] + values[i]:
                selected_counts[i] += 1
                w -= weights[i]
                break
    
    return dp[capacity], selected_counts

# উদাহরণ
weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 7

print("\nআনবাউন্ডেড ন্যাপস্যাক সমস্যা:")
print(f"ওজন: {weights}")
print(f"মান: {values}")
print(f"ক্ষমতা: {capacity}")

max_value, counts = unbounded_knapsack(weights, values, capacity)
print(f"\nসর্বোচ্চ মান: {max_value}")
print("আইটেম সংখ্যা:")
for i in range(len(counts)):
    if counts[i] > 0:
        print(f"  আইটেম {i}: {counts[i]} বার")
```

## ৪. মাল্টিডাইমেনশনাল ন্যাপস্যাক
```python
def multi_constraint_knapsack(weights1, weights2, values, capacity1, capacity2):
    """
    ২টি কনস্ট্রেইন্ট সহ ন্যাপস্যাক (ওজন + আয়তন)
    """
    n = len(values)
    
    # 3D DP টেবিল
    dp = [[[0] * (capacity2 + 1) for _ in range(capacity1 + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w1 in range(capacity1 + 1):
            for w2 in range(capacity2 + 1):
                if weights1[i-1] <= w1 and weights2[i-1] <= w2:
                    dp[i][w1][w2] = max(
                        dp[i-1][w1][w2],  # না নিলে
                        dp[i-1][w1 - weights1[i-1]][w2 - weights2[i-1]] + values[i-1]  # নিলে
                    )
                else:
                    dp[i][w1][w2] = dp[i-1][w1][w2]
    
    max_value = dp[n][capacity1][capacity2]
    
    # নির্বাচিত আইটেম
    selected = []
    w1, w2 = capacity1, capacity2
    
    for i in range(n, 0, -1):
        if dp[i][w1][w2] != dp[i-1][w1][w2]:
            selected.append(i-1)
            w1 -= weights1[i-1]
            w2 -= weights2[i-1]
    
    selected.reverse()
    return max_value, selected

# উদাহরণ
weights1 = [2, 3, 4]  # ওজন (কেজি)
weights2 = [3, 4, 2]  # আয়তন (m³)
values = [5, 7, 9]
capacity1 = 5  # সর্বোচ্চ ওজন
capacity2 = 6  # সর্বোচ্চ আয়তন

print("\nমাল্টিডাইমেনশনাল ন্যাপস্যাক (২ কনস্ট্রেইন্ট):")
max_value, selected = multi_constraint_knapsack(weights1, weights2, values, capacity1, capacity2)
print(f"সর্বোচ্চ মান: {max_value}")
print(f"নির্বাচিত আইটেম: {selected}")
```

## ৫. ব্যাকট্র্যাকিং পদ্ধতি
```python
def knapsack_backtracking(weights, values, capacity):
    """
    ব্যাকট্র্যাকিং দিয়ে ন্যাপস্যাক সমাধান
    """
    n = len(weights)
    best_value = 0
    best_selection = []
    
    def backtrack(idx, current_weight, current_value, selection):
        nonlocal best_value, best_selection
        
        if idx == n:
            if current_value > best_value:
                best_value = current_value
                best_selection = selection[:]
            return
        
        # বর্তমান আইটেম নেওয়া (যদি সম্ভব)
        if current_weight + weights[idx] <= capacity:
            selection.append(idx)
            backtrack(idx + 1, 
                     current_weight + weights[idx], 
                     current_value + values[idx], 
                     selection)
            selection.pop()
        
        # বর্তমান আইটেম না নেওয়া
        backtrack(idx + 1, current_weight, current_value, selection)
    
    backtrack(0, 0, 0, [])
    return best_value, best_selection

# উদাহরণ
print("\nব্যাকট্র্যাকিং পদ্ধতি:")
weights_small = [2, 3, 4, 5]
values_small = [3, 4, 5, 6]
capacity_small = 8

max_val, selection = knapsack_backtracking(weights_small, values_small, capacity_small)
print(f"সর্বোচ্চ মান: {max_val}")
print(f"নির্বাচিত আইটেম: {selection}")
```

## ৬. ব্রাঞ্চ এন্ড বাউন্ড পদ্ধতি
```python
import heapq

class Node:
    """ব্রাঞ্চ এন্ড বাউন্ড নোড"""
    def __init__(self, level, weight, value, bound, items):
        self.level = level  # বর্তমান লেভেল
        self.weight = weight  # মোট ওজন
        self.value = value  # মোট মান
        self.bound = bound  # আপার বাউন্ড
        self.items = items  # নির্বাচিত আইটেম
    
    def __lt__(self, other):
        # প্রায়োরিটি কিউর জন্য (বাউন্ডের ভিত্তিতে)
        return self.bound > other.bound

def calculate_bound(node, n, capacity, weights, values):
    """নোডের আপার বাউন্ড ক্যালকুলেট"""
    if node.weight >= capacity:
        return 0
    
    bound = node.value
    total_weight = node.weight
    level = node.level + 1
    
    # ফ্র্যাকশনাল ন্যাপস্যাক হিসাবে বাউন্ড ক্যালকুলেট
    while level < n and total_weight + weights[level] <= capacity:
        total_weight += weights[level]
        bound += values[level]
        level += 1
    
    # শেষ আইটেমের ফ্র্যাকশন যোগ
    if level < n:
        bound += (capacity - total_weight) * (values[level] / weights[level])
    
    return bound

def knapsack_branch_bound(weights, values, capacity):
    """ব্রাঞ্চ এন্ড বাউন্ড পদ্ধতি"""
    n = len(weights)
    
    # মান/ওজন অনুপাত অনুযায়ী সর্ট
    items = sorted(range(n), key=lambda i: values[i]/weights[i], reverse=True)
    
    # সর্টেড ওজন ও মান
    sorted_weights = [weights[i] for i in items]
    sorted_values = [values[i] for i in items]
    
    # প্রায়োরিটি কিউ
    pq = []
    
    # রুট নোড
    root = Node(-1, 0, 0, 0, [])
    root.bound = calculate_bound(root, n, capacity, sorted_weights, sorted_values)
    
    heapq.heappush(pq, root)
    
    max_value = 0
    best_items = []
    
    while pq:
        current = heapq.heappop(pq)
        
        if current.bound > max_value:
            # লেফ্ট চাইল্ড (আইটেম নিন)
            level = current.level + 1
            
            if level < n:
                # আইটেম নিন
                left_weight = current.weight + sorted_weights[level]
                left_value = current.value + sorted_values[level]
                left_items = current.items + [items[level]]
                
                if left_weight <= capacity and left_value > max_value:
                    max_value = left_value
                    best_items = left_items[:]
                
                left_bound = calculate_bound(
                    Node(level, left_weight, left_value, 0, left_items),
                    n, capacity, sorted_weights, sorted_values
                )
                
                if left_bound > max_value:
                    left_node = Node(level, left_weight, left_value, left_bound, left_items)
                    heapq.heappush(pq, left_node)
                
                # রাইট চাইল্ড (আইটেম নিন না)
                right_bound = calculate_bound(
                    Node(level, current.weight, current.value, 0, current.items),
                    n, capacity, sorted_weights, sorted_values
                )
                
                if right_bound > max_value:
                    right_node = Node(level, current.weight, current.value, right_bound, current.items)
                    heapq.heappush(pq, right_node)
    
    return max_value, sorted(best_items)

# উদাহরণ
print("\nব্রাঞ্চ এন্ড বাউন্ড পদ্ধতি:")
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_val, items = knapsack_branch_bound(weights, values, capacity)
print(f"সর্বোচ্চ মান: {max_val}")
print(f"নির্বাচিত আইটেম: {items}")
```

## রিয়েল-লাইফ অ্যাপ্লিকেশন

### ১. ইনভেস্টমেন্ট পোর্টফোলিও
```python
def investment_portfolio(funds, returns, risks, max_risk, budget):
    """
    ইনভেস্টমেন্ট পোর্টফোলিও অপটিমাইজেশন
    """
    n = len(funds)
    
    # 2D ন্যাপস্যাক: বাজেট + রিস্ক
    dp = [[0] * (max_risk + 1) for _ in range(budget + 1)]
    investment = [[[] for _ in range(max_risk + 1)] for _ in range(budget + 1)]
    
    for i in range(n):
        for b in range(budget, funds[i] - 1, -1):
            for r in range(max_risk, risks[i] - 1, -1):
                if dp[b][r] < dp[b - funds[i]][r - risks[i]] + returns[i]:
                    dp[b][r] = dp[b - funds[i]][r - risks[i]] + returns[i]
                    investment[b][r] = investment[b - funds[i]][r - risks[i]] + [i]
    
    # সর্বোচ্চ রিটার্ন খুঁজুন
    max_return = 0
    best_investment = []
    
    for b in range(budget + 1):
        for r in range(max_risk + 1):
            if dp[b][r] > max_return:
                max_return = dp[b][r]
                best_investment = investment[b][r]
    
    return max_return, best_investment

# উদাহরণ
funds = [1000, 2000, 1500, 3000]  # বিনিয়োগ (টাকা)
returns = [150, 350, 250, 500]  # রিটার্ন (টাকা)
risks = [2, 4, 3, 5]  # রিস্ক লেভেল (1-10)
max_risk = 7  # সর্বোচ্চ রিস্ক
budget = 4000  # বাজেট

print("\nইনভেস্টমেন্ট পোর্টফোলিও অপটিমাইজেশন:")
max_ret, investments = investment_portfolio(funds, returns, risks, max_risk, budget)
print(f"সর্বোচ্চ রিটার্ন: {max_ret} টাকা")
print(f"বিনিয়োগের ফান্ড: {investments}")
print(f"মোট বিনিয়োগ: {sum(funds[i] for i in investments)} টাকা")
```

### ২. শিপিং কনটেইনার অপটিমাইজেশন
```python
def container_loading(items, weights, values, container_capacity):
    """
    কনটেইনার লোডিং সমস্যা
    """
    n = len(items)
    
    # 0/1 ন্যাপস্যাক
    dp = [0] * (container_capacity + 1)
    selection = [[] for _ in range(container_capacity + 1)]
    
    for i in range(n):
        for w in range(container_capacity, weights[i] - 1, -1):
            if dp[w] < dp[w - weights[i]] + values[i]:
                dp[w] = dp[w - weights[i]] + values[i]
                selection[w] = selection[w - weights[i]] + [i]
    
    max_value = dp[container_capacity]
    selected_items = selection[container_capacity]
    
    return max_value, selected_items

# উদাহরণ
items = ['TV', 'ফ্রিজ', 'ওয়াশিং মেশিন', 'সোফা', 'বেড']
weights = [30, 60, 40, 50, 20]  # কেজি
values = [20000, 40000, 25000, 30000, 15000]  # টাকা
capacity = 100  # কেজি

print("\nকনটেইনার লোডিং সমস্যা:")
max_val, selected = container_loading(items, weights, values, capacity)
print(f"সর্বোচ্চ মান: {max_val} টাকা")
print(f"নির্বাচিত আইটেম: {[items[i] for i in selected]}")
print(f"মোট ওজন: {sum(weights[i] for i in selected)} কেজি")
```

### ৩. টাইম ম্যানেজমেন্ট (টাস্ক শিডিউলিং)
```python
def task_scheduling(tasks, durations, values, available_time):
    """
    টাস্ক শিডিউলিং - সময়ের মধ্যে সর্বোচ্চ মানের টাস্ক
    """
    n = len(tasks)
    
    # 0/1 ন্যাপস্যাক
    dp = [0] * (available_time + 1)
    task_selection = [[] for _ in range(available_time + 1)]
    
    for i in range(n):
        for t in range(available_time, durations[i] - 1, -1):
            if dp[t] < dp[t - durations[i]] + values[i]:
                dp[t] = dp[t - durations[i]] + values[i]
                task_selection[t] = task_selection[t - durations[i]] + [i]
    
    max_value = dp[available_time]
    selected_tasks = task_selection[available_time]
    
    return max_value, selected_tasks

# উদাহরণ
tasks = ['প্রজেক্ট A', 'প্রজেক্ট B', 'মিটিং', 'রিপোর্ট লেখা', 'ট্রেনিং']
durations = [3, 2, 1, 2, 3]  # ঘণ্টা
values = [100, 80, 30, 50, 90]  # গুরুত্ব (1-100)
available_time = 5  # ঘণ্টা

print("\nটাইম ম্যানেজমেন্ট (টাস্ক শিডিউলিং):")
max_val, selected = task_scheduling(tasks, durations, values, available_time)
print(f"সর্বোচ্চ মান: {max_val}")
print(f"নির্বাচিত টাস্ক: {[tasks[i] for i in selected]}")
print(f"মোট সময়: {sum(durations[i] for i in selected)} ঘণ্টা")
```

### ৪. স্টাডি প্ল্যানার (পরীক্ষার প্রস্তুতি)
```python
def exam_preparation(subjects, hours_needed, importance, total_hours):
    """
    পরীক্ষার প্রস্তুতির জন্য সাবজেক্ট নির্বাচন
    """
    n = len(subjects)
    
    dp = [0] * (total_hours + 1)
    subject_selection = [[] for _ in range(total_hours + 1)]
    
    for i in range(n):
        for h in range(total_hours, hours_needed[i] - 1, -1):
            if dp[h] < dp[h - hours_needed[i]] + importance[i]:
                dp[h] = dp[h - hours_needed[i]] + importance[i]
                subject_selection[h] = subject_selection[h - hours_needed[i]] + [i]
    
    max_importance = dp[total_hours]
    selected_subjects = subject_selection[total_hours]
    
    return max_importance, selected_subjects

# উদাহরণ
subjects = ['গণিত', 'পদার্থ', 'রসায়ন', 'বায়োলজি', 'ইংরেজি']
hours_needed = [10, 8, 6, 7, 5]  # প্রয়োজনীয় ঘণ্টা
importance = [40, 35, 30, 25, 20]  # গুরুত্ব (পরীক্ষায় মার্ক)
total_hours = 15  # মোট সময়

print("\nপরীক্ষার প্রস্তুতি প্ল্যানার:")
max_imp, selected = exam_preparation(subjects, hours_needed, importance, total_hours)
print(f"সর্বোচ্চ গুরুত্ব: {max_imp}")
print(f"নির্বাচিত সাবজেক্ট: {[subjects[i] for i in selected]}")
print(f"মোট সময়: {sum(hours_needed[i] for i in selected)} ঘণ্টা")
```

## পারফরম্যান্স বিশ্লেষণ
```python
def performance_comparison():
    """বিভিন্ন ন্যাপস্যাক অ্যালগরিদমের পারফরম্যান্স তুলনা"""
    import time
    
    print("\n" + "="*60)
    print("ন্যাপস্যাক অ্যালগরিদম পারফরম্যান্স তুলনা")
    print("="*60)
    
    # বড় ডেটাসেট
    n = 20
    capacity = 100
    
    import random
    weights = [random.randint(1, 20) for _ in range(n)]
    values = [random.randint(10, 100) for _ in range(n)]
    
    algorithms = [
        ("ডিপি (0/1)", knapsack_01),
        ("অপ্টিমাইজড ডিপি", knapsack_01_optimized),
        ("ব্যাকট্র্যাকিং", knapsack_backtracking),
    ]
    
    for name, func in algorithms:
        start = time.time()
        if name == "ব্যাকট্র্যাকিং":
            result = func(weights[:15], values[:15], capacity)  # ছোট ডেটা
        else:
            result = func(weights, values, capacity)
        end = time.time()
        
        print(f"{name}:")
        print(f"  সময়: {end-start:.6f} সেকেন্ড")
        print(f"  সর্বোচ্চ মান: {result[0] if isinstance(result, tuple) else result}")
        print()

performance_comparison()
```

## টাইম কমপ্লেক্সিটি বিশ্লেষণ
```python
def complexity_analysis():
    """ন্যাপস্যাক অ্যালগরিদমের টাইম কমপ্লেক্সিটি"""
    
    print("\n" + "="*60)
    print("ন্যাপস্যাক অ্যালগরিদম - টাইম কমপ্লেক্সিটি")
    print("="*60)
    
    complexities = {
        "০/১ ন্যাপস্যাক (ডিপি)": "O(n*W)",
        "ফ্র্যাকশনাল ন্যাপস্যাক": "O(n log n)",
        "আনবাউন্ডেড ন্যাপস্যাক": "O(n*W)",
        "মাল্টিডাইমেনশনাল ন্যাপস্যাক": "O(n*W₁*W₂*...*Wₖ)",
        "ব্যাকট্র্যাকিং": "O(2ⁿ)",
        "ব্রাঞ্চ এন্ড বাউন্ড": "O(2ⁿ) (ওয়ার্স্ট কেস)",
    }
    
    for algo, complexity in complexities.items():
        print(f"{algo:30} -> {complexity}")
    
    print("\nযেখানে:")
    print("n = আইটেম সংখ্যা")
    print("W = ব্যাগের ক্ষমতা")
    print("Wᵢ = i-তম কনস্ট্রেইন্টের ক্ষমতা")

complexity_analysis()
```

## ভিজ্যুয়ালাইজেশন
```python
def visualize_knapsack_solution(weights, values, selected_items, capacity):
    """ন্যাপস্যাক সমাধান ভিজ্যুয়ালাইজেশন"""
    
    print("\n" + "="*60)
    print("ন্যাপস্যাক সমাধান ভিজ্যুয়ালাইজেশন")
    print("="*60)
    
    n = len(weights)
    total_weight = sum(weights[i] for i in selected_items)
    total_value = sum(values[i] for i in selected_items)
    
    print(f"\nব্যাগের ক্ষমতা: {capacity}")
    print(f"ব্যবহৃত ক্ষমতা: {total_weight}/{capacity} ({total_weight/capacity*100:.1f}%)")
    print(f"সর্বোচ্চ মান: {total_value}")
    
    # গ্রাফিক্যাল রিপ্রেজেন্টেশন
    print("\nব্যাগ ভিজ্যুয়ালাইজেশন:")
    print("[" + "-" * capacity + "]")
    
    filled = 0
    for i in selected_items:
        segment = "█" * weights[i]
        print(f"  আইটেম {i} ({weights[i]}kg): {' ' * filled}{segment}")
        filled += weights[i]
    
    # আইটেম টেবিল
    print("\nআইটেম ডিটেইলস:")
    print(f"{'Index':<6} {'Weight':<8} {'Value':<8} {'Value/Weight':<12} {'Selected':<10}")
    print("-" * 50)
    
    for i in range(n):
        selected = "✓" if i in selected_items else "✗"
        ratio = values[i] / weights[i]
        print(f"{i:<6} {weights[i]:<8} {values[i]:<8} {ratio:<12.2f} {selected:<10}")
    
    # পারফরম্যান্স মেট্রিক্স
    print("\nপারফরম্যান্স মেট্রিক্স:")
    print(f"ব্যাগ ইউটিলাইজেশন: {total_weight/capacity*100:.1f}%")
    print(f"ভ্যালু ডেনসিটি: {total_value/total_weight if total_weight > 0 else 0:.2f} মান/কেজি")
    
    if total_weight < capacity:
        unused = capacity - total_weight
        print(f"\n⚠️  সতর্কতা: {unused} কেজি ক্ষমতা অব্যবহৃত")

# ভিজ্যুয়ালাইজেশন উদাহরণ
weights_viz = [3, 4, 2, 5]
values_viz = [4, 5, 3, 6]
capacity_viz = 8
selected_viz = [0, 2]  # 3kg + 2kg = 5kg, মান: 4 + 3 = 7

visualize_knapsack_solution(weights_viz, values_viz, selected_viz, capacity_viz)
```

## চ্যালেঞ্জিং প্রবলেমস
```python
def challenging_problems():
    """ন্যাপস্যাকের চ্যালেঞ্জিং ভ্যারিয়েন্ট"""
    
    print("\n" + "="*60)
    print("ন্যাপস্যাকের চ্যালেঞ্জিং ভ্যারিয়েন্ট")
    print("="*60)
    
    problems = [
        {
            'name': 'সাবসেট সাম প্রবলেম',
            'description': 'সেট থেকে এমন সাবসেট বের করুন যার যোগফল টার্গেটের সমান',
            'reduction': 'মান = ওজন, টার্গেট = ক্ষমতা'
        },
        {
            'name': 'পার্টিশন প্রবলেম',
            'description': 'সেটকে দুটি সাবসেটে ভাগ করুন যাদের যোগফল সমান',
            'reduction': 'সাবসেট সাম যেখানে টার্গেট = মোট যোগফল/২'
        },
        {
            'name': 'রড কাটিং প্রবলেম',
            'description': 'রডকে টুকরো করে সর্বোচ্চ মুনাফা',
            'reduction': 'আনবাউন্ডেড ন্যাপস্যাক'
        },
        {
            'name': 'কয়েন চেঞ্জ প্রবলেম',
            'description': 'কয়েন ব্যবহার করে টার্গেট অ্যামাউন্ট',
            'reduction': 'আনবাউন্ডেড ন্যাপস্যাক'
        },
        {
            'name': 'জিরো-ওয়ান ন্যাপস্যাক',
            'description': 'ওজন নেগেটিভ হতে পারে',
            'reduction': 'শিফটেড ইনডেক্স ব্যবহার'
        }
    ]
    
    for i, problem in enumerate(problems, 1):
        print(f"\n{i}. {problem['name']}")
        print(f"   {problem['description']}")
        print(f"   ➤ {problem['reduction']}")
    
    # সাবসেট সাম উদাহরণ
    print("\n\nসাবসেট সাম উদাহরণ:")
    def subset_sum(arr, target):
        """সাবসেট সাম সমস্যা - ন্যাপস্যাক রিডাকশন"""
        n = len(arr)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        # সমাধান পুনরুদ্ধার
        if dp[n][target]:
            subset = []
            j = target
            for i in range(n, 0, -1):
                if not dp[i-1][j]:
                    subset.append(arr[i-1])
                    j -= arr[i-1]
            return True, subset
        
        return False, []
    
    arr = [3, 34, 4, 12, 5, 2]
    target = 9
    exists, subset = subset_sum(arr, target)
    print(f"অ্যারে: {arr}")
    print(f"টার্গেট: {target}")
    print(f"সমাধান আছে: {exists}")
    if exists:
        print(f"সাবসেট: {subset} = {sum(subset)}")

challenging_problems()
```

## উপসংহার

ন্যাপস্যাক সমস্যা কম্পিউটার সায়েন্সের সবচেয়ে গুরুত্বপূর্ণ অপটিমাইজেশন সমস্যা যা নিম্নলিখিত বিষয় শেখায়:

### মূল শিক্ষা:
1. **ডাইনামিক প্রোগ্রামিং**: ওভারল্যাপিং সাবপ্রবলেম অপটিমাইজেশন
2. **গ্রিডি অ্যালগরিদম**: লোকাল অপটিমাইজেশন
3. **ব্রাঞ্চ এন্ড বাউন্ড**: সার্চ স্পেস কম্প্রেশন
4. **প্রবলেম রিডাকশন**: একটি সমস্যাকে অন্য সমস্যায় রূপান্তর

### রিয়েল-লাইফ অ্যাপ্লিকেশন:
1. **রিসোর্স অ্যালোকেশন**: CPU শিডিউলিং, মেমোরি ম্যানেজমেন্ট
2. **ফাইন্যান্স**: ইনভেস্টমেন্ট পোর্টফোলিও অপটিমাইজেশন
3. **লজিস্টিক্স**: কনটেইনার লোডিং, ট্রাক প্যাকিং
4. **নেটওয়ার্কিং**: ব্যান্ডউইথ অ্যালোকেশন
5. **ম্যানুফ্যাকচারিং**: মেটিরিয়াল কাটিং

### কার্যকারিতা:
- **স্ট্রংলি NP-হার্ড**: সঠিক সমাধান বড় ইনপুটের জন্য ব্যয়বহুল
- **পসেডুপলিনোমিয়াল**: ক্ষমতা ছোট হলে ডিপি কার্যকর
- **অ্যাপ্রোক্সিমেশন**: PTAS, FPTAS অ্যালগরিদম আছে

**মনে রাখবেন**: সঠিক অ্যালগরিদম নির্বাচন সমস্যার স্পেসিফিকেশনের উপর নির্ভর করে - কখনো ০/১ ন্যাপস্যাক, কখনো ফ্র্যাকশনাল, কখনো আনবাউন্ডেড!