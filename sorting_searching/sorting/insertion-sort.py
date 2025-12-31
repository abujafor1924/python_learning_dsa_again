


"""
 ইনসার্শন সর্ট একটি সহজ, কম্পারিজন-ভিত্তিক সর্টিং অ্যালগরিদম। এটি একটি এলিমেন্টকে তার সঠিক অবস্থানে বসিয়ে সর্টেড অ্যারে তৈরি করে।
কিভাবে কাজ করে?
১. দ্বিতীয় এলিমেন্ট থেকে শুরু করুন (ইনডেক্স ১), প্রথম এলিমেন্টকে ইতিমধ্যে সর্টেড ধরে নিন।
২. বর্তমান এলিমেন্টকে তার আগের এলিমেন্টগুলোর সাথে তুলনা করুন।
৩. বড় এলিমেন্টগুলোকে এক পজিশন ডান দিকে শিফট করুন।
৪. বর্তমান এলিমেন্টকে তার সঠিক জায়গায় বসান।
৫. সব এলিমেন্টের জন্য পুনরাবৃত্তি করুন।
"""

#Func tion Of Practice
def insertion_sort(arr):
     for i in range(1,len(arr)):
          key=arr[i]
          j=i-1
          
          while j >=0 and arr[j] > key :
               arr[j+1]=arr[j]
               j -= 1
          arr[j+1]=key
     return arr

arr = [5, 2, 9, 1, 5, 6]
print(insertion_sort(arr))


def insertion_sort_desending(arr):
     for i in range(1,len(arr)):
          key=arr[i]
          j=i-1
          
          while j >=0 and arr[j] < key :       # change desending
               arr[j+1]=arr[j]
               j -= 1
          arr[j+1]=key
     return arr

arr = [5, 2, 9, 1, 5, 6]
print(insertion_sort_desending(arr))
               
     
     