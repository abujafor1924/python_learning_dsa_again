

"""
বাবল সর্ট একটি সহজ কম্পারিজন-ভিত্তিক সর্টিং অ্যালগরিদম। এটি প্রতিবেশী এলিমেন্টগুলোর মধ্যে তুলনা করে এবং যদি তারা ভুল অর্ডারে থাকে তবে তাদের সোয়াপ করে। এর নাম "বাবল" কারণ বড় এলিমেন্টগুলো পানির বুদবুদের মত উপরে ভেসে ওঠে।

কিভাবে কাজ করে?
১. প্রথম এলিমেন্ট এবং দ্বিতীয় এলিমেন্ট তুলনা করুন।
২. যদি প্রথম > দ্বিতীয় হয়, তাহলে সোয়াপ করুন।
৩. দ্বিতীয় এবং তৃতীয় তুলনা করুন, সোয়াপ করুন যদি প্রয়োজন হয়।
৪. এভাবে শেষ পর্যন্ত চলুন → সবচেয়ে বড় এলিমেন্ট শেষে চলে যাবে।
৫. আবার শুরু থেকে শুরু করুন, কিন্তু শেষের এলিমেন্ট বাদ দিয়ে।
৬. চলতে থাকবে যতক্ষণ না কোন সোয়াপ না হয়।
"""


def bubble_sort(arr):
     n=len(arr)
     for i in range(n):
          for j in range(0, n-i-1):
               if arr[j] > arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
     return arr



arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr.copy()))

def bubble_sort_decending(arr):
     n=len(arr)
     for i in range(n):
          for j in range(0,n-i-1):
               if arr[j] < arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
     return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort_decending(arr))


def bubble_sort_swapped(arr):
     n=len(arr)
     for i in range(n):
          swapped = False
          for j in range(0, n-i-1):
               if arr[j] > arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapped = True
          if not swapped:
               break
     return arr



arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort_swapped(arr))


          
          
          
          
# ===================== Copy From AI =============================


def bubble_sort_with_count(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        
        if not swapped:
            break
    
    return arr, comparisons, swaps

arr = [5, 1, 4, 2, 8]
sorted_arr, comp, swp = bubble_sort_with_count(arr.copy())
print(f"তুলনা: {comp}, সোয়াপ: {swp}")