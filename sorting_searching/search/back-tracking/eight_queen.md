# এইট কুইন প্রবলেম বিস্তারিত বাংলায়

এইট কুইন প্রবলেম হল একটি ক্লাসিক্যাল কম্বিনেটোরিয়াল ও ব্যাকট্র্যাকিং সমস্যা যেখানে **৮x৮ চেসবোর্ডে ৮টি কুইন** এমনভাবে বসাতে হবে যাতে তারা একে অপরকে **আক্রমণ না করে**।

## সমস্যার বিবরণ
- **চেসবোর্ড**: ৮x৮ গ্রিড
- **কুইন সংখ্যা**: ৮টি
- **কনস্ট্রেইন্ট**: কোনো কুইন অন্যটিকে আক্রমণ করতে পারবে না
- **আক্রমণের নিয়ম**: 
  - একই সারিতে
  - একই কলামে
  - একই ডায়াগোনালে

## মোট সমাধান সংখ্যা
- **বেসিক সমাধান**: ৯২টি
- **ইউনিক সমাধান** (রোটেশন/রিফ্লেকশন বাদে): ১২টি

## সমাধানের পদ্ধতি

### ১. ব্যাকট্র্যাকিং পদ্ধতি (ক্লাসিক্যাল)
```python
def solve_n_queens_8x8():
    """
    এইট কুইন সমস্যার ব্যাকট্র্যাকিং সমাধান।
    """
    N = 8
    solutions = []
    
    def is_safe(board, row, col):
        """কুইন বসানো নিরাপদ কিনা চেক করুন"""
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
        while i >= 0 and j < N:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row, board):
        """ব্যাকট্র্যাকিং ফাংশন"""
        if row == N:
            # সমাধান সংরক্ষণ
            solutions.append([''.join(row) for row in board])
            return
        
        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 'Q'        # কুইন বসান
                backtrack(row + 1, board)    # পরের সারি
                board[row][col] = '.'        # ব্যাকট্র্যাক
    
    # বোর্ড ইনিশিয়ালাইজেশন
    board = [['.' for _ in range(N)] for _ in range(N)]
    backtrack(0, board)
    
    return solutions

# সমাধান বের করুন
solutions = solve_n_queens_8x8()
print(f"মোট সমাধান সংখ্যা: {len(solutions)}")
print("\nপ্রথম ৩টি সমাধান:")
for i in range(min(3, len(solutions))):
    print(f"\nসমাধান {i+1}:")
    for row in solutions[i]:
        print(row)
```

### ২. অপটিমাইজড ব্যাকট্র্যাকিং (কলাম অ্যারে ব্যবহার)
```python
def solve_n_queens_optimized(N=8):
    """
    অপটিমাইজড ব্যাকট্র্যাকিং - শুধু কলাম অ্যারে ব্যবহার।
    """
    solutions = []
    cols = [0] * N          # কলামে কুইন আছে কিনা
    diag1 = [0] * (2*N-1)   # মূল ডায়াগোনাল (row+col)
    diag2 = [0] * (2*N-1)   # বিপরীত ডায়াগোনাল (row-col+N-1)
    
    def backtrack(row, positions):
        if row == N:
            solutions.append(positions[:])
            return
        
        for col in range(N):
            # চেক করুন কুইন বসানো নিরাপদ কিনা
            if not cols[col] and not diag1[row+col] and not diag2[row-col+N-1]:
                # কুইন বসান
                cols[col] = diag1[row+col] = diag2[row-col+N-1] = 1
                positions.append((row, col))
                
                # পরবর্তী সারিতে যান
                backtrack(row + 1, positions)
                
                # ব্যাকট্র্যাক
                cols[col] = diag1[row+col] = diag2[row-col+N-1] = 0
                positions.pop()
    
    backtrack(0, [])
    return solutions

def print_solution_board(positions):
    """সমাধান বোর্ড প্রিন্ট করুন"""
    N = 8
    board = [['.' for _ in range(N)] for _ in range(N)]
    
    for row, col in positions:
        board[row][col] = 'Q'
    
    for row in board:
        print(' '.join(row))

# সমাধান বের করুন
solutions = solve_n_queens_optimized(8)
print(f"অপটিমাইজড পদ্ধতিতে সমাধান সংখ্যা: {len(solutions)}")
print("\nপ্রথম ২টি সমাধান:")
for i in range(min(2, len(solutions))):
    print(f"\nসমাধান {i+1}:")
    print_solution_board(solutions[i])
```

### ৩. সিম্পলিফাইড অ্যাপ্রোচ (1D অ্যারে)
```python
def solve_n_queens_simple(N=8):
    """
    সিম্পলিফাইড পদ্ধতি - 1D অ্যারে ব্যবহার করে।
    """
    solutions = []
    
    def is_safe(col_placement, row, col):
        """চেক করুন নতুন কুইন নিরাপদ কিনা"""
        for prev_row in range(row):
            prev_col = col_placement[prev_row]
            
            # একই কলাম
            if prev_col == col:
                return False
            
            # একই ডায়াগোনাল
            if abs(prev_col - col) == abs(prev_row - row):
                return False
        
        return True
    
    def backtrack(row, col_placement):
        if row == N:
            solutions.append(col_placement[:])
            return
        
        for col in range(N):
            if is_safe(col_placement, row, col):
                col_placement[row] = col
                backtrack(row + 1, col_placement)
    
    col_placement = [-1] * N
    backtrack(0, col_placement)
    return solutions

# সমাধান বের করুন
solutions = solve_n_queens_simple(8)
print(f"সিম্পল পদ্ধতিতে সমাধান সংখ্যা: {len(solutions)}")
print("\nসমাধানগুলো (কলাম পজিশন):")
for i in range(min(5, len(solutions))):
    print(f"সমাধান {i+1}: {solutions[i]}")
```

## ভিজ্যুয়ালাইজেশন সহ সমাধান
```python
def visualize_all_solutions():
    """সমস্ত সমাধান ভিজ্যুয়ালাইজ করুন"""
    N = 8
    solutions = solve_n_queens_optimized(N)
    
    print(f"৮x৮ চেসবোর্ডে ৮ কুইন সমস্যা")
    print(f"মোট সমাধান: {len(solutions)}")
    print("=" * 50)
    
    # প্রতিটি সমাধান দেখান
    for sol_num, positions in enumerate(solutions[:5], 1):
        print(f"\nসমাধান #{sol_num}:")
        print(f"পজিশন: {positions}")
        
        # বোর্ড প্রিন্ট
        board = [['◻' for _ in range(N)] for _ in range(N)]
        
        # চেসবোর্ড প্যাটার্ন
        for i in range(N):
            for j in range(N):
                if (i + j) % 2 == 0:
                    board[i][j] = '◻'
                else:
                    board[i][j] = '◼'
        
        # কুইন বসান
        for row, col in positions:
            board[row][col] = '♕'  # কুইন চিহ্ন
        
        # বোর্ড প্রিন্ট
        print("  " + " ".join(str(i) for i in range(N)))
        for i in range(N):
            print(f"{i} ", end="")
            for j in range(N):
                print(f"{board[i][j]} ", end="")
            print()
    
    # শুধু সংখ্যা দেখান
    print(f"\nসমস্ত {len(solutions)}টি সমাধানের প্রথম সারির কলাম পজিশন:")
    col_positions = [sol[0][1] for sol in solutions]
    for i in range(0, len(col_positions), 10):
        print(f"  {col_positions[i:i+10]}")

visualize_all_solutions()
```

## ইন্টারেক্টিভ ডেমো
```python
def interactive_8_queens():
    """ইন্টারেক্টিভ এইট কুইন ডেমো"""
    N = 8
    
    def print_guide():
        print("\n" + "="*60)
        print("এইট কুইন সমস্যা - ইন্টারেক্টিভ ডেমো")
        print("="*60)
        print("কুইন বসানোর নিয়ম:")
        print("1. কোনো সারিতে শুধু ১টি কুইন")
        print("2. কোনো কলামে শুধু ১টি কুইন")
        print("3. কোনো ডায়াগোনালে শুধু ১টি কুইন")
        print("="*60)
    
    def get_user_solution():
        """ইউজার থেকে সমাধান নিন"""
        print("\nআপনার সমাধান ইনপুট দিন:")
        print("প্রতিটি কুইনের জন্য (row, col) ইনপুট দিন (0-7)")
        
        positions = []
        for queen in range(8):
            while True:
                try:
                    row = int(input(f"কুইন {queen+1} এর সারি (0-7): "))
                    col = int(input(f"কুইন {queen+1} এর কলাম (0-7): "))
                    
                    if 0 <= row < 8 and 0 <= col < 8:
                        positions.append((row, col))
                        break
                    else:
                        print("দয়া করে 0-7 এর মধ্যে সংখ্যা দিন!")
                except ValueError:
                    print("দয়া করে সঠিক সংখ্যা ইনপুট দিন!")
        
        return positions
    
    def check_solution(positions):
        """সমাধান চেক করুন"""
        if len(positions) != 8:
            return False, "৮টি কুইন বসাতে হবে!"
        
        rows = [0] * 8
        cols = [0] * 8
        diag1 = [0] * 15  # row+col (0-14)
        diag2 = [0] * 15  # row-col+7 (-7 থেকে 7)
        
        for row, col in positions:
            # সারি চেক
            if rows[row]:
                return False, f"সারি {row} এ একাধিক কুইন!"
            rows[row] = 1
            
            # কলাম চেক
            if cols[col]:
                return False, f"কলাম {col} এ একাধিক কুইন!"
            cols[col] = 1
            
            # ডায়াগোনাল চেক
            d1 = row + col
            if diag1[d1]:
                return False, f"ডায়াগোনাল {d1} এ একাধিক কুইন!"
            diag1[d1] = 1
            
            d2 = row - col + 7
            if diag2[d2]:
                return False, f"ডায়াগোনাল {d2} এ একাধিক কুইন!"
            diag2[d2] = 1
        
        return True, "সমাধান সঠিক! 🎉"
    
    # গাইড প্রিন্ট
    print_guide()
    
    while True:
        print("\n1. সমাধান চেক করুন")
        print("2. একটি সমাধান দেখুন")
        print("3. সব সমাধানের সংখ্যা দেখুন")
        print("4. প্রস্থান")
        
        choice = input("\nআপনার পছন্দ (1-4): ")
        
        if choice == '1':
            positions = get_user_solution()
            is_valid, message = check_solution(positions)
            
            if is_valid:
                print("\n✅ " + message)
                # সমাধান প্রিন্ট
                board = [['.' for _ in range(8)] for _ in range(8)]
                for row, col in positions:
                    board[row][col] = 'Q'
                
                print("\nআপনার সমাধান:")
                for i, row in enumerate(board):
                    print(f"{i}: {' '.join(row)}")
            else:
                print(f"\n❌ {message}")
        
        elif choice == '2':
            solutions = solve_n_queens_optimized(8)
            import random
            sol = random.choice(solutions)
            
            print("\nএকটি এলোমেলো সমাধান:")
            print_solution_board(sol)
            
            # পজিশন তালিকা
            print(f"\nকুইন পজিশন: {sol}")
        
        elif choice == '3':
            solutions = solve_n_queens_optimized(8)
            print(f"\nমোট সমাধান সংখ্যা: {len(solutions)}")
            
            # প্রথম কয়েকটি সমাধানের কলাম পজিশন
            print("প্রথম ১০টি সমাধানের কলাম পজিশন:")
            for i in range(min(10, len(solutions))):
                cols = [col for _, col in solutions[i]]
                print(f"  {i+1}: {cols}")
        
        elif choice == '4':
            print("\nধন্যবাদ! প্রস্থান করা হচ্ছে...")
            break
        
        else:
            print("\n❌ দয়া করে 1-4 এর মধ্যে পছন্দ দিন!")

# ইন্টারেক্টিভ ডেমো চালান (কমেন্ট আউট করুন যদি চান না)
# interactive_8_queens()
```

## অ্যানিমেশন/স্টেপ বাই স্টেপ সল্যুশন
```python
def step_by_step_solution():
    """স্টেপ বাই স্টেপ সমাধান প্রদর্শন"""
    N = 8
    
    print("\n" + "="*60)
    print("এইট কুইন - স্টেপ বাই স্টেপ সমাধান")
    print("="*60)
    
    # ব্যাকট্র্যাকিং প্রক্রিয়া দেখান
    board = [['.' for _ in range(N)] for _ in range(N)]
    step = 1
    
    def show_step(row, col, action):
        nonlocal step
        print(f"\n📝 স্টেপ {step}: {action}")
        print(f"   সারি: {row}, কলাম: {col}")
        
        # বোর্ড প্রিন্ট
        temp_board = [row[:] for row in board]
        if action == "বসানো":
            temp_board[row][col] = 'Q'
        else:
            temp_board[row][col] = '.'
        
        print("   " + " ".join(str(i) for i in range(N)))
        for i in range(N):
            print(f"  {i} ", end="")
            for j in range(N):
                symbol = 'Q' if temp_board[i][j] == 'Q' else '.'
                print(f"{symbol} ", end="")
            print()
        
        step += 1
    
    # সিমুলেশন
    # একটি সমাধানের জন্য পদক্ষেপ
    solution_positions = [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)]
    
    print("\nব্যাকট্র্যাকিং প্রক্রিয়া:")
    print("আমরা প্রথম সারি থেকে শুরু করছি...")
    
    for row in range(N):
        found = False
        for col in range(N):
            # ইম্যাজিনারি চেক
            if col == solution_positions[row][1]:
                board[row][col] = 'Q'
                show_step(row, col, "বসানো")
                found = True
                break
            else:
                show_step(row, col, "চেষ্টা (ব্যর্থ)")
        
        if not found:
            show_step(row, -1, "ব্যাকট্র্যাক")
            # সিমুলেট ব্যাকট্র্যাক
    
    print("\n✅ সমাধান সম্পূর্ণ!")
    print("সমস্ত ৮টি কুইন বসানো হয়েছে!")

step_by_step_solution()
```

## পারফরম্যান্স বিশ্লেষণ
```python
def performance_analysis():
    """বিভিন্ন N-Queens এর পারফরম্যান্স বিশ্লেষণ"""
    import time
    
    print("\n" + "="*60)
    print("N-Queens পারফরম্যান্স বিশ্লেষণ")
    print("="*60)
    
    n_values = [4, 5, 6, 7, 8, 9, 10]
    
    print(f"{'N':<5} {'সমাধান সংখ্যা':<15} {'সময় (সেকেন্ড)':<15}")
    print("-" * 40)
    
    for n in n_values:
        start_time = time.time()
        solutions = solve_n_queens_optimized(n)
        end_time = time.time()
        
        print(f"{n:<5} {len(solutions):<15} {end_time-start_time:<15.6f}")
    
    # 8-Queens এর বিস্তারিত
    print("\n৮-কুইন সমস্যা সম্পর্কে কিছু মজার তথ্য:")
    solutions = solve_n_queens_optimized(8)
    
    # বিভিন্ন ধরনের প্রথম সারির পজিশন
    first_col_counts = {}
    for sol in solutions:
        first_col = sol[0][1]
        first_col_counts[first_col] = first_col_counts.get(first_col, 0) + 1
    
    print(f"\nপ্রথম সারিতে কুইন বসানোর সম্ভাবনা:")
    for col in range(8):
        count = first_col_counts.get(col, 0)
        percentage = (count / len(solutions)) * 100
        print(f"  কলাম {col}: {count:2d} বার ({percentage:5.1f}%)")

performance_analysis()
```

## গাণিতিক বিশ্লেষণ
```python
def mathematical_analysis():
    """এইট কুইন সমস্যার গাণিতিক বিশ্লেষণ"""
    
    print("\n" + "="*60)
    print("এইট কুইন সমস্যা - গাণিতিক বিশ্লেষণ")
    print("="*60)
    
    # সম্ভাব্যতা
    total_arrangements = 64 * 63 * 62 * 61 * 60 * 59 * 58 * 57  # 8টি কুইন বসানোর সব উপায়
    successful_arrangements = 92  # প্রকৃত সমাধান
    
    probability = successful_arrangements / total_arrangements
    
    print(f"সম্ভাব্য সমাধানের সংখ্যা: {total_arrangements:,}")
    print(f"প্রকৃত সমাধানের সংখ্যা: {successful_arrangements}")
    print(f"এলোমেলোভাবে সঠিক সমাধান পাওয়ার সম্ভাবনা: {probability:.15f}")
    print(f"বা 1 in {1/probability:,.0f}")
    
    # সমাধান গ্রুপিং
    print("\nসমাধানগুলোর গ্রুপিং (সিমেট্রি অনুসারে):")
    print("1. আসল সমাধান: 92টি")
    print("2. রোটেশনালি ডিসটিংকট: 46টি")
    print("3. মৌলিক সমাধান (ইউনিক আপ টু সিমেট্রি): 12টি")
    
    # ১২টি মৌলিক সমাধান
    fundamental_solutions = [
        [0, 4, 7, 5, 2, 6, 1, 3],
        [0, 5, 7, 2, 6, 3, 1, 4],
        [0, 6, 3, 5, 7, 1, 4, 2],
        [0, 6, 4, 7, 1, 3, 5, 2],
        [1, 3, 5, 7, 2, 0, 6, 4],
        [1, 4, 6, 0, 2, 7, 5, 3],
        [1, 4, 6, 3, 0, 7, 5, 2],
        [1, 5, 0, 6, 3, 7, 2, 4],
        [1, 5, 7, 2, 0, 3, 6, 4],
        [1, 6, 2, 5, 7, 4, 0, 3],
        [1, 6, 4, 7, 0, 3, 5, 2],
        [1, 7, 5, 0, 2, 4, 6, 3]
    ]
    
    print("\n১২টি মৌলিক সমাধান (কলাম পজিশন, সারি 0-7):")
    for i, sol in enumerate(fundamental_solutions, 1):
        print(f"{i:2d}: {sol}")

mathematical_analysis()
```

## হিউরিস্টিক অ্যালগরিদম
```python
def solve_8_queens_heuristic():
    """
    হিউরিস্টিক পদ্ধতিতে এইট কুইন সমাধান।
    মিনি-কনফ্লিক্ট হিউরিস্টিক ব্যবহার করে।
    """
    import random
    
    N = 8
    max_iterations = 1000
    
    def calculate_conflicts(positions):
        """কনফ্লিক্ট সংখ্যা গণনা"""
        conflicts = 0
        for i in range(N):
            for j in range(i+1, N):
                row_i, col_i = i, positions[i]
                row_j, col_j = j, positions[j]
                
                # একই কলাম
                if col_i == col_j:
                    conflicts += 1
                
                # একই ডায়াগোনাল
                if abs(row_i - row_j) == abs(col_i - col_j):
                    conflicts += 1
        
        return conflicts
    
    def find_best_swap(positions):
        """সবচেয়ে ভাল সোয়াপ খুঁজুন"""
        best_swap = None
        best_conflicts = calculate_conflicts(positions)
        
        for i in range(N):
            for j in range(i+1, N):
                # সোয়াপ করুন
                positions[i], positions[j] = positions[j], positions[i]
                new_conflicts = calculate_conflicts(positions)
                
                # যদি ভাল হয়
                if new_conflicts < best_conflicts:
                    best_conflicts = new_conflicts
                    best_swap = (i, j)
                
                # আবার সোয়াপ (আন্ডু)
                positions[i], positions[j] = positions[j], positions[i]
        
        return best_swap, best_conflicts
    
    # এলোমেলো অবস্থান দিয়ে শুরু করুন
    best_solution = None
    best_conflicts = float('inf')
    
    for attempt in range(max_iterations):
        # এলোমেলো অবস্থান তৈরি করুন
        positions = random.sample(range(N), N)
        current_conflicts = calculate_conflicts(positions)
        
        iteration = 0
        while iteration < 100 and current_conflicts > 0:
            # সবচেয়ে ভাল সোয়াপ খুঁজুন
            best_swap, new_conflicts = find_best_swap(positions)
            
            if best_swap is None:
                break
            
            # সোয়াপ করুন
            i, j = best_swap
            positions[i], positions[j] = positions[j], positions[i]
            current_conflicts = new_conflicts
            iteration += 1
        
        # যদি সমাধান পাওয়া যায়
        if current_conflicts == 0:
            best_solution = positions
            break
        
        # যদি এটাই এখন পর্যন্ত সবচেয়ে ভাল হয়
        if current_conflicts < best_conflicts:
            best_conflicts = current_conflicts
            best_solution = positions[:]
    
    if best_solution and calculate_conflicts(best_solution) == 0:
        return best_solution
    return None

# হিউরিস্টিক পদ্ধতি টেস্ট করুন
print("\nহিউরিস্টিক পদ্ধতিতে সমাধান:")
solution = solve_8_queens_heuristic()
if solution:
    print(f"সমাধান পাওয়া গেছে: {solution}")
    
    # বোর্ড প্রিন্ট
    board = [['.' for _ in range(8)] for _ in range(8)]
    for row, col in enumerate(solution):
        board[row][col] = 'Q'
    
    print("\nসমাধান বোর্ড:")
    for row in board:
        print(' '.join(row))
else:
    print("হিউরিস্টিক পদ্ধতিতে সমাধান পাওয়া যায়নি")
```

## এইট কুইন এর ঐতিহাসিক তথ্য
```python
def historical_facts():
    """এইট কুইন সমস্যার ঐতিহাসিক তথ্য"""
    
    print("\n" + "="*60)
    print("এইট কুইন সমস্যা - ঐতিহাসিক তথ্য")
    print("="*60)
    
    facts = [
        "1. এই সমস্যাটি প্রথম ১৮৪৮ সালে চেস প্লেয়ার ম্যাক্স বেজেল দ্বারা প্রস্তাবিত হয়",
        "2. ১৮৫০ সালে কার্ল ফ্রিডরিশ গাউস এই সমস্যা নিয়ে কাজ করেন",
        "3. ফ্রাঞ্জ নাউক ১৮৫০ সালে প্রথম সব ৯২টি সমাধান খুঁজে পান",
        "4. ১৮৭৪ সালে গ্লাইশার প্রুফ করেন যে ১২টি মৌলিক সমাধান আছে",
        "5. এই সমস্যা কম্পিউটার সায়েন্সে ব্যাকট্র্যাকিং এর ক্লাসিক উদাহরণ",
        "6. ১৯৭২ সালে ডিজকস্ট্রা এই সমস্যা ব্যবহার করে স্ট্রাকচার্ড প্রোগ্রামিং ডেমো করেন",
        "7. N-Queens সমস্যা এইট কুইনের সাধারণীকরণ (N x N বোর্ডে N কুইন)",
        "8. ২৭-Queens সমস্যা ছিল ১৯৯০ সালের একটি বিখ্যাত প্রোগ্রামিং প্রতিযোগিতার সমস্যা",
        "9. কুইন সবচেয়ে শক্তিশালী চেস পিস - সে সারি, কলাম ও ডায়াগোনালে আক্রমণ করে",
        "10. এই সমস্যা AI, অপারেশন রিসার্চ ও কম্বিনেটোরিয়াল অপটিমাইজেশনে ব্যাপক ব্যবহৃত"
    ]
    
    for fact in facts:
        print(f"• {fact}")
    
    print("\nকিছু মজার তথ্য:")
    print("- ৮x৮ বোর্ডে ৮ কুইন বসানোর মোট উপায়: C(64, 8) = 4,426,165,368")
    print("- শুধু ৯২টি উপায়েই তারা একে অপরকে আক্রমণ করে না")
    print("- সম্ভাবনা: ৯২/৪,৪২৬,১৬৫,৩৬৮ ≈ ০.০০০০০০০২")

historical_facts()
```

## বোনাস: N-Queens জেনারেলাইজেশন
```python
def n_queens_general(N):
    """যেকোনো N এর জন্য N-Queens সমাধান"""
    
    def solve(N):
        solutions = []
        cols = [0] * N
        diag1 = [0] * (2*N-1)
        diag2 = [0] * (2*N-1)
        
        def backtrack(row, positions):
            if row == N:
                solutions.append(positions[:])
                return
            
            for col in range(N):
                if not cols[col] and not diag1[row+col] and not diag2[row-col+N-1]:
                    cols[col] = diag1[row+col] = diag2[row-col+N-1] = 1
                    positions.append((row, col))
                    
                    backtrack(row + 1, positions)
                    
                    cols[col] = diag1[row+col] = diag2[row-col+N-1] = 0
                    positions.pop()
        
        backtrack(0, [])
        return solutions
    
    solutions = solve(N)
    
    print(f"\n{N}-Queens সমস্যা:")
    print(f"বোর্ড: {N}x{N}")
    print(f"কুইন সংখ্যা: {N}")
    print(f"সমাধান সংখ্যা: {len(solutions)}")
    
    if solutions and N <= 10:
        print("\nপ্রথম সমাধান:")
        board = [['.' for _ in range(N)] for _ in range(N)]
        for row, col in solutions[0]:
            board[row][col] = 'Q'
        
        for row in board:
            print(' '.join(row))
    
    return len(solutions)

# বিভিন্ন N এর জন্য টেস্ট
print("\n" + "="*60)
print("N-Queens জেনারেলাইজেশন")
print("="*60)

for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    count = n_queens_general(n)
    print(f"N={n}: {count} solutions")
```

## উপসংহার

এইট কুইন সমস্যা কম্পিউটার সায়েন্সের একটি মৌলিক সমস্যা যা নিম্নলিখিত বিষয় শেখায়:

1. **ব্যাকট্র্যাকিং**: ভুল পথে গেলে ফিরে আসার কৌশল
2. **রিকার্সন**: সমস্যাকে ছোট ছোট অংশে ভাগ করা
3. **কনস্ট্রেইন্ট স্যাটিসফ্যাকশন**: শর্ত পূরণ করা
4. **অপটিমাইজেশন**: ডায়াগোনাল চেক অপটিমাইজ করা
5. **এলগরিদম ডিজাইন**: বিভিন্ন পদ্ধতিতে সমাধান

**বাস্তব জীবনে ব্যবহার**:
- শিডিউলিং সমস্যা
- রিসোর্স অ্যালোকেশন
- ভিএলএসআই চিপ ডিজাইন
- ডেটাবেজ কুয়েরি অপ্টিমাইজেশন
- জেনেটিক অ্যালগরিদম

এই সমস্যা দেখায় কিভাবে একটি সরল প্রশ্ন গভীর গাণিতিক ও অ্যালগরিদমিক ধারণার দিকে নিয়ে যায়!