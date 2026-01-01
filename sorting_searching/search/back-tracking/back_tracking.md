# ব্যাকট্র্যাকিং বিস্তারিত বাংলায়

ব্যাকট্র্যাকিং হল একটি অ্যালগরিদমিক টেকনিক যা সমস্যা সমাধানের জন্য **সিস্টেমেটিক ট্রায়াল এন্ড এরর** পদ্ধতি ব্যবহার করে। এটি রিকার্সিভ ডিপ-ফার্স্ট সার্চের উপর ভিত্তি করে।

## মূল ধারণা
- **ট্রায়াল এন্ড এরর**: সম্ভাব্য সব সমাধান চেষ্টা করে দেখা
- **পিছু হটা (Backtrack)**: ভুল পথে এলে ফিরে আসা
- **সমাধান নির্মাণ**: ধাপে ধাপে সমাধান তৈরি করা

## বৈশিষ্ট্য
- **টাইম কমপ্লেক্সিটি**: সাধারণত এক্সপোনেনশিয়াল (O(2^n), O(n!))
- **স্পেস কমপ্লেক্সিটি**: O(ডেপথ অফ রিকার্সন)
- **প্রয়োজনীয়তা**: কনস্ট্রেইন্ট স্যাটিসফ্যাকশন

## সাধারণ টেমপ্লেট
```python
def backtrack(সমস্যা, সমাধান, ধাপ):
    if সমাধান_সম্পূর্ণ(সমাধান):
        ফলাফল_সংরক্ষণ(সমাধান)
        return
    
    সম্ভাব্য_পছন্দ = সম্ভাব্য_পছন্দ_তৈরি(সমস্যা, ধাপ)
    
    for পছন্দ in সম্ভাব্য_পছন্দ:
        if বৈধ_পছন্দ(পছন্দ, সমাধান):
            সমাধান.যুক্ত(পছন্দ)      # পছন্দ যোগ
            backtrack(সমস্যা, সমাধান, ধাপ + 1)
            সমাধান.অপসারণ(পছন্দ)     # ব্যাকট্র্যাক (পছন্দ বাদ)
```

## ১. এন-কুইন সমস্যা (N-Queens)
```python
def solve_n_queens(n):
    """
    N x N চেসবোর্ডে N টি কুইন এমনভাবে বসানো যাতে তারা একে অপরকে আক্রমণ না করে।
    """
    def is_safe(board, row, col):
        """চেক করুন কুইন বসানো নিরাপদ কিনা"""
        # একই কলামে চেক
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # বাম উপরের ডায়াগোনাল চেক
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # ডান উপরের ডায়াগোনাল চেক
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row, board, solutions):
        """ব্যাকট্র্যাকিং ফাংশন"""
        if row == n:
            # সম্পূর্ণ সমাধান
            solutions.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'        # কুইন বসান
                backtrack(row + 1, board, solutions)  # পরের সারিতে যান
                board[row][col] = '.'        # ব্যাকট্র্যাক (কুইন সরান)
    
    # সমাধান শুরু
    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0, board, solutions)
    return solutions

# ব্যবহার
n = 4
solutions = solve_n_queens(n)
print(f"{n}-কুইন সমস্যার সমাধান সংখ্যা: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"\nসমাধান {i+1}:")
    for row in solution:
        print(row)
```

## ২. সুডোকু সলভার
```python
def solve_sudoku(board):
    """
    9x9 সুডোকু বোর্ড সমাধান।
    """
    def find_empty(board):
        """খালি ঘর খোঁজা"""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None
    
    def is_valid(board, num, pos):
        """সংখ্যা বসানো বৈধ কিনা চেক"""
        row, col = pos
        
        # একই সারিতে চেক
        for j in range(9):
            if board[row][j] == num and j != col:
                return False
        
        # একই কলামে চেক
        for i in range(9):
            if board[i][col] == num and i != row:
                return False
        
        # 3x3 বক্সে চেক
        box_row = row // 3
        box_col = col // 3
        
        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False
        
        return True
    
    def backtrack(board):
        """ব্যাকট্র্যাকিং ফাংশন"""
        empty = find_empty(board)
        
        if not empty:
            return True  # সমাধান সম্পূর্ণ
        
        row, col = empty
        
        for num in range(1, 10):
            if is_valid(board, num, (row, col)):
                board[row][col] = num  # সংখ্যা বসান
                
                if backtrack(board):   # রিকার্সিভ কল
                    return True
                
                board[row][col] = 0   # ব্যাকট্র্যাক (সংশোধন)
        
        return False  # কোন সমাধান পাওয়া যায়নি
    
    # মেইন ফাংশন
    return backtrack(board)

# ব্যবহার
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("সুডোকু সমস্যা:")
for row in sudoku_board:
    print(row)

if solve_sudoku(sudoku_board):
    print("\nসমাধান:")
    for row in sudoku_board:
        print(row)
else:
    print("\nকোন সমাধান নেই")
```

## ৩. সেট পার্টিশন সমস্যা
```python
def subset_partition(arr):
    """
    সেটকে দুটি সাবসেটে ভাগ করুন যাদের যোগফল সমান।
    """
    total_sum = sum(arr)
    
    # যোগফল জোড় না হলে সম্ভব না
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(arr)
    
    def backtrack(idx, current_sum, current_set):
        """ব্যাকট্র্যাকিং ফাংশন"""
        if current_sum == target:
            return True
        
        if current_sum > target or idx >= n:
            return False
        
        # বর্তমান এলিমেন্ট নিন
        if backtrack(idx + 1, current_sum + arr[idx], current_set + [arr[idx]]):
            return True
        
        # বর্তমান এলিমেন্ট বাদ দিন
        if backtrack(idx + 1, current_sum, current_set):
            return True
        
        return False
    
    return backtrack(0, 0, [])

# ব্যবহার
numbers = [3, 1, 5, 9, 12]
print(f"অ্যারে: {numbers}")
print(f"সমান যোগফল পার্টিশন সম্ভব: {subset_partition(numbers)}")
```

## ৪. পারমুটেশন জেনারেশন
```python
def generate_permutations(nums):
    """
    সংখ্যার সব পারমুটেশন জেনারেট করা।
    """
    def backtrack(path, used, permutations):
        """ব্যাকট্র্যাকিং ফাংশন"""
        if len(path) == len(nums):
            permutations.append(path[:])  # কপি সংরক্ষণ
            return
        
        for i in range(len(nums)):
            if not used[i]:
                # সংখ্যা ব্যবহার করুন
                used[i] = True
                path.append(nums[i])
                
                backtrack(path, used, permutations)
                
                # ব্যাকট্র্যাক
                path.pop()
                used[i] = False
    
    permutations = []
    used = [False] * len(nums)
    backtrack([], used, permutations)
    return permutations

# ব্যবহার
nums = [1, 2, 3]
permutations = generate_permutations(nums)
print(f"পারমুটেশন সংখ্যা: {len(permutations)}")
for perm in permutations:
    print(perm)
```

## ৫. কম্বিনেশন সুম
```python
def combination_sum(candidates, target):
    """
    সংখ্যার সেট থেকে কম্বিনেশন খুঁজুন যার যোগফল টার্গেট।
    একই সংখ্যা বারবার ব্যবহার করা যাবে।
    """
    def backtrack(start, path, current_sum, result):
        """ব্যাকট্র্যাকিং ফাংশন"""
        if current_sum == target:
            result.append(path[:])
            return
        
        if current_sum > target:
            return
        
        for i in range(start, len(candidates)):
            # পছন্দ যোগ করুন
            path.append(candidates[i])
            backtrack(i, path, current_sum + candidates[i], result)
            # ব্যাকট্র্যাক
            path.pop()
    
    result = []
    backtrack(0, [], 0, result)
    return result

# ব্যবহার
candidates = [2, 3, 6, 7]
target = 7
combinations = combination_sum(candidates, target)
print(f"টার্গেট: {target}")
print(f"ক্যান্ডিডেট: {candidates}")
print(f"কম্বিনেশন:")
for combo in combinations:
    print(combo)
```

## ৬. ম্যাজ পাথ ফাইন্ডার
```python
def solve_maze(maze):
    """
    র্যাট ইন এ ম্যাজ সমস্যা।
    0 = পথ, 1 = দেয়াল
    """
    def is_valid(x, y, visited):
        """ঘর বৈধ কিনা চেক"""
        return (0 <= x < len(maze) and 
                0 <= y < len(maze[0]) and 
                maze[x][y] == 0 and 
                not visited[x][y])
    
    def backtrack(x, y, path, visited):
        """ব্যাকট্র্যাকিং ফাংশন"""
        # গন্তব্যে পৌঁছানো
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            path.append((x, y))
            return True
        
        if is_valid(x, y, visited):
            # মার্ক করুন
            visited[x][y] = True
            path.append((x, y))
            
            # সব দিকে চেষ্টা করুন
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # ডাউন, রাইট, আপ, লেফ্ট
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if backtrack(nx, ny, path, visited):
                    return True
            
            # ব্যাকট্র্যাক
            path.pop()
            visited[x][y] = False
        
        return False
    
    # ইনিশিয়ালাইজেশন
    if not maze or maze[0][0] == 1 or maze[-1][-1] == 1:
        return []
    
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    path = []
    
    if backtrack(0, 0, path, visited):
        return path
    return []

# ব্যবহার
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

print("ম্যাজ:")
for row in maze:
    print(row)

solution_path = solve_maze(maze)
print(f"\nসমাধান পথ: {solution_path}")

# ম্যাজ প্রিন্ট করা
if solution_path:
    print("\nগণিত পথ সহ ম্যাজ:")
    solution_set = set(solution_path)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in solution_set:
                print("◉", end=" ")
            elif maze[i][j] == 1:
                print("█", end=" ")
            else:
                print(".", end=" ")
        print()
```

## ৭. নাইটস ট্যুর সমস্যা
```python
def knights_tour(n):
    """
    n x n চেসবোর্ডে নাইটের ট্যুর।
    """
    # নাইটের চলার দিক
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    def is_valid(x, y, board):
        """ঘর বৈধ কিনা চেক"""
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1
    
    def backtrack(x, y, move_count, board):
        """ব্যাকট্র্যাকিং ফাংশন"""
        if move_count == n * n:
            return True  # ট্যুর সম্পূর্ণ
        
        # সম্ভাব্য সব ঘরে চেষ্টা করুন
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            
            if is_valid(nx, ny, board):
                board[nx][ny] = move_count
                
                if backtrack(nx, ny, move_count + 1, board):
                    return True
                
                # ব্যাকট্র্যাক
                board[nx][ny] = -1
        
        return False
    
    # বোর্ড ইনিশিয়ালাইজেশন
    board = [[-1 for _ in range(n)] for _ in range(n)]
    
    # শুরু করুন (0,0) থেকে
    board[0][0] = 0
    
    if backtrack(0, 0, 1, board):
        return board
    return None

# ব্যবহার
n = 5
tour = knights_tour(n)
if tour:
    print(f"{n}x{n} নাইটস ট্যুর:")
    for row in tour:
        for cell in row:
            print(f"{cell:3d}", end=" ")
        print()
else:
    print(f"{n}x{n} বোর্ডে নাইটস ট্যুর সম্ভব নয়")
```

## অপটিমাইজেশন টেকনিক

### ১. প্রুনিং (Pruning)
```python
def backtrack_with_pruning(path, depth, best_result):
    """প্রুনিং সহ ব্যাকট্র্যাকিং"""
    # আর্লি টার্মিনেশন: যদি বর্তমান পথ ইতিমধ্যেই খারাপ হয়
    if current_cost > best_result:
        return float('inf')
    
    # আরও অপটিমাইজেশন...
    pass
```

### ২. মেমোইজেশন
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def backtrack_memoized(state):
    """মেমোইজেশন সহ ব্যাকট্র্যাকিং"""
    # কম্পিউট করা স্টেট ক্যাশে করা
    pass
```

### ৩. হিউরিস্টিকস
```python
def backtrack_with_heuristic(choices):
    """হিউরিস্টিক অর্ডারিং সহ ব্যাকট্র্যাকিং"""
    # সবচেয়ে সম্ভাব্য পছন্দগুলো আগে চেষ্টা করুন
    sorted_choices = sorted(choices, key=heuristic_function)
    for choice in sorted_choices:
        pass
```

## পারফরম্যান্স বিশ্লেষণ
```python
import time

def performance_test(problem_size):
    """ব্যাকট্র্যাকিং পারফরম্যান্স টেস্ট"""
    
    # পারমুটেশন জেনারেশন টেস্ট
    print(f"পারমুটেশন জেনারেশন ({problem_size} এলিমেন্ট):")
    start = time.time()
    nums = list(range(problem_size))
    perms = generate_permutations(nums)
    end = time.time()
    print(f"সময়: {end-start:.4f} সেকেন্ড")
    print(f"পারমুটেশন সংখ্যা: {len(perms)}")
    print(f"প্রত্যাশিত সংখ্যা: {problem_size}! = {math.factorial(problem_size)}")
    print()
    
    # এন-কুইন টেস্ট
    print("এন-কুইন সমস্যা:")
    for n in range(4, 9):
        start = time.time()
        solutions = solve_n_queens(n)
        end = time.time()
        print(f"N={n}: {len(solutions)} সমাধান, সময়: {end-start:.4f} সেকেন্ড")

# পারফরম্যান্স টেস্ট চালান
performance_test(8)
```

## ব্যবহারের ক্ষেত্র
1. **কনস্ট্রেইন্ট স্যাটিসফ্যাকশন সমস্যা**: সুডোকু, ক্রসওয়ার্ড
2. **কম্বিনেটোরিয়াল অপ্টিমাইজেশন**: ট্রাভেলিং সেলসম্যান
3. **পারমুটেশন/কম্বিনেশন**: পাসওয়ার্ড ক্র্যাকিং
4. **পাথ ফাইন্ডিং**: ম্যাজ, গেমস
5. **রিসোর্স অ্যালোকেশন**: নাপস্যাক সমস্যা

## উপকারিতা
- সবসময় সমাধান খুঁজে পায় (যদি থাকে)
- সমস্যার গঠন বোঝা সহজ
- ফ্লেক্সিবল এবং অ্যাডাপ্টেবল

## সীমাবদ্ধতা
- এক্সপোনেনশিয়াল টাইম কমপ্লেক্সিটি
- বড় সমস্যার জন্য অনুপযুক্ত
- ডুপ্লিকেট কাজ করে

## সমাধানের উপায়
- **প্রুনিং**: অপ্রয়োজনীয় ব্রাঞ্চ কাটা
- **ডাইনামিক প্রোগ্রামিং**: ওভারল্যাপিং সাবপ্রবলেম
- **হিউরিস্টিকস**: ইন্টেলিজেন্ট সার্চ
- **প্যারালালাইজেশন**: একাধিক ব্রাঞ্চ সমান্তরালে

## রিয়েল-লাইফ অ্যাপ্লিকেশন
```python
# ১. টাইম টেবল শিডিউলিং
def schedule_classes(classes, rooms, time_slots):
    """ক্লাস শিডিউলিং সমস্যা"""
    schedule = {}
    
    def backtrack(class_index):
        if class_index == len(classes):
            return True
        
        current_class = classes[class_index]
        
        for room in rooms:
            for time in time_slots:
                if is_available(room, time, current_class):
                    # শিডিউল করুন
                    schedule[current_class] = (room, time)
                    mark_unavailable(room, time, current_class)
                    
                    if backtrack(class_index + 1):
                        return True
                    
                    # ব্যাকট্র্যাক
                    del schedule[current_class]
                    mark_available(room, time, current_class)
        
        return False
    
    return backtrack(0)

# ২. রিসোর্স অ্যালোকেশন
def allocate_resources(tasks, resources):
    """টাস্কে রিসোর্স বরাদ্দ"""
    allocations = {}
    
    def backtrack(task_index):
        if task_index == len(tasks):
            return True
        
        for resource in resources:
            if can_assign(resource, tasks[task_index]):
                allocations[tasks[task_index]] = resource
                resource.capacity -= tasks[task_index].requirement
                
                if backtrack(task_index + 1):
                    return True
                
                # ব্যাকট্র্যাক
                del allocations[tasks[task_index]]
                resource.capacity += tasks[task_index].requirement
        
        return False
    
    return backtrack(0)
```

## উপসংহার
ব্যাকট্র্যাকিং হল একটি শক্তিশালী টেকনিক যা বিভিন্ন ধরনের সমস্যা সমাধানে ব্যবহৃত হয়। যদিও এটি এক্সপোনেনশিয়াল টাইম নেয়, সঠিক প্রুনিং এবং অপটিমাইজেশনের মাধ্যমে অনেক বড় সমস্যাও সমাধান করা সম্ভব। এটি প্রোগ্রামিং ইন্টারভিউ এবং প্রতিযোগিতামূলক প্রোগ্রামিংয়ে খুবই জনপ্রিয়।