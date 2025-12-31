


"""
সিলেকশন সর্ট একটি সহজ কম্পারিজন-ভিত্তিক সর্টিং অ্যালগরিদম। এটি প্রতিটি পজিশনের জন্য সর্বনিম্ন (বা সর্বোচ্চ) এলিমেন্ট বাছাই করে এবং সঠিক পজিশনে রাখে।

কিভাবে কাজ করে?
১. সম্পূর্ণ অ্যারে থেকে সর্বনিম্ন এলিমেন্ট খুঁজে বের করুন।
২. সেই এলিমেন্টকে প্রথম পজিশনে সোয়াপ করুন।
৩. এখন অবশিষ্ট অ্যারে থেকে (দ্বিতীয় পজিশন থেকে শেষ পর্যন্ত) আবার সর্বনিম্ন এলিমেন্ট খুঁজুন।
৪. তাকে দ্বিতীয় পজিশনে সোয়াপ করুন।
৫. এভাবে চলতে থাকবে যতক্ষণ না সম্পূর্ণ অ্যারে সর্টেড হয়।
"""
def selection_sort(arr):
     n=len(arr)
     for i in range(n-1):
          min_index=i
          for j in range(i+1,n):
               if arr[j] < arr[min_index] :
                    min_index = j
          arr[i],arr[min_index]=arr[min_index],arr[i]
     return arr


arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))


def selection_sort_dissent(arr):
     n=len(arr)
     for i in range(n-1):
          min_index=i
          for j in range(i+1,n):
               if arr[j] > arr[min_index]:  # chang desenting symble
                    min_index =j
          arr[i],arr[min_index]=arr[min_index],arr[i]
     return arr

arr = [64, 25, 12, 22, 11]
print(selection_sort_dissent(arr))
               






# ===================== Copy From AI =============================
def selection_sort_with_count(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    
    return arr, comparisons, swaps

arr = [64, 25, 12, 22, 11]
sorted_arr, comp, swp = selection_sort_with_count(arr)
print(f"তুলনা: {comp}, সোয়াপ: {swp}")


def selection_sort_strings(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:  # লেক্সিকোগ্রাফিক্যাল তুলনা
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

words = ["banana", "apple", "cherry", "date"]
print(selection_sort_strings(words))
# আউটপুট: ['apple', 'banana', 'cherry', 'date']