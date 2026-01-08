# **Heap Data Structure ও Priority Queue - বাংলা ডিটেইল**

## **হিপ (Heap) কি?**
হিপ একটি **সম্পূর্ণ বাইনারি ট্রি (Complete Binary Tree)** ডাটা স্ট্রাকচার যা **হিপ প্রপার্টি** মেনে চলে।

### **হিপের প্রকারভেদ:**
1. **ম্যাক্স-হিপ (Max-Heap)**: 
   - প্যারেন্ট নোড ≥ চাইল্ড নোড
   - রুট নোডে সবথেকে বড় ভ্যালু থাকে
   
2. **মিন-হিপ (Min-Heap)**:
   - প্যারেন্ট নোড ≤ চাইল্ড নোড
   - রুট নোডে সবথেকে ছোট ভ্যালু থাকে

## **হিপের উপস্থাপনা (Representation)**
হিপ সাধারণত **অ্যারে/লিস্ট** হিসেবে ইমপ্লিমেন্ট করা হয়:

```python
# Index সম্পর্কে সূত্র:
# Parent = (i-1)//2
# Left Child = 2*i + 1
# Right Child = 2*i + 2
```

### **উদাহরণ (মিন-হিপ):**
```
অ্যারে: [10, 20, 15, 30, 40]

ট্রি রূপ:
        10
       /  \
      20   15
     /  \
    30   40
```

## **হিপ অপারেশন**

### **১. ইনসার্ট (Insert)**
```python
def insert(heap, value):
    heap.append(value)  # ১. শেষে ভ্যালু যোগ করুন
    i = len(heap) - 1   # ২. নতুন নোডের ইনডেক্স
    
    # ৩. হিপিফাই আপ (Heapify Up)
    while i > 0 and heap[i] < heap[(i-1)//2]:  # মিন-হিপের জন্য
        heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]  # সোয়াপ
        i = (i-1)//2  # প্যারেন্টের দিকে যান
```

### **২. ডিলিট/পপ (Delete/Pop) - রুট রিমুভ**
```python
def extract_min(heap):
    if not heap:
        return None
    
    # ১. রুট ভ্যালু সেভ করুন
    root = heap[0]
    
    # ২. শেষ ভ্যালু রুটে নিয়ে আসুন
    heap[0] = heap[-1]
    heap.pop()
    
    # ৩. হিপিফাই ডাউন (Heapify Down)
    i = 0
    n = len(heap)
    
    while True:
        smallest = i
        left = 2*i + 1
        right = 2*i + 2
        
        if left < n and heap[left] < heap[smallest]:
            smallest = left
        
        if right < n and heap[right] < heap[smallest]:
            smallest = right
        
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
        else:
            break
    
    return root
```

## **প্রাইওরিটি কিউ (Priority Queue)**
প্রাইওরিটি কিউ হলো একটি **এবস্ট্রাক্ট ডাটা টাইপ** যেখানে:
- প্রতিটি এলিমেন্টের একটি **প্রাইওরিটি** থাকে
- **হাইয়ার প্রাইওরিটি** এর এলিমেন্ট প্রথমে সার্ভ হয়

### **ইমপ্লিমেন্টেশন:**
প্রাইওরিটি কিউ সাধারণত **হিপ** ব্যবহার করে ইমপ্লিমেন্ট করা হয়।

```python
class PriorityQueue:
    def __init__(self):
        self.heap = []  # মিন-হিপ ব্যবহার করব
    
    def enqueue(self, value, priority=None):
        # যদি প্রাইওরিটি আলাদা দেওয়া না হয়, ভ্যালুই প্রাইওরিটি
        if priority is None:
            priority = value
        
        # (প্রাইওরিটি, ভ্যালু) টাপল হিসেবে স্টোর
        self.heap.append((priority, value))
        self._heapify_up(len(self.heap) - 1)
    
    def dequeue(self):
        if not self.heap:
            return None
        
        # রুট এলিমেন্ট রিটার্ন (সবথেকে কম প্রাইওরিটি)
        root = self.heap[0]
        
        # শেষ এলিমেন্ট রুটে নিয়ে আসি
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self._heapify_down(0)
        
        return root[1]  # শুধু ভ্যালু রিটার্ন
    
    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent][0]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
    
    def _heapify_down(self, index):
        n = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            
            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
    
    def peek(self):
        return self.heap[0][1] if self.heap else None
    
    def is_empty(self):
        return len(self.heap) == 0
```

## **হিপ সর্ট (Heap Sort) অ্যালগরিদম**
```python
def heap_sort(arr):
    n = len(arr)
    
    # ১. হিপ বিল্ড করুন (Max-Heap)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # ২. একে একে এলিমেন্ট এক্সট্র্যাক্ট করুন
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # সোয়াপ
        heapify(arr, i, 0)  # রিডিউসড হিপে হিপিফাই
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

## **টাইম কমপ্লেক্সিটি**
| অপারেশন | টাইম কমপ্লেক্সিটি |
|----------|-------------------|
| ইনসার্ট | O(log n) |
| ডিলিট (রুট) | O(log n) |
| পিক/গেট ম্যাক্স-মিন | O(1) |
| হিপ বিল্ড | O(n) |
| হিপ সর্ট | O(n log n) |

## **রিয়েল-লাইফ ব্যবহার**
1. **প্রাইওরিটি স케জুলিং** - OS প্রোসেস স케জুলিং
2. **ডাইজক্সট্রা অ্যালগরিদম** - শর্টেস্ট পাথ ফাইন্ডিং
3. **হাফম্যান কোডিং** - ডাটা কম্প্রেশন
4. **হিপ সর্ট** - সর্টিং অ্যালগরিদম
5. **মিডিয়ান মেইনটেইন** - স্ট্রিমিং ডাটা

## **প্র্যাকটিক্যাল উদাহরণ**
```python
# হাসপাতালে ইমার্জেন্সি প্রাইওরিটি কিউ
hospital_queue = PriorityQueue()

# রোগী যোগ করা (প্রাইওরিটি: 1=সর্বোচ্চ, 5=সর্বনিম্ন)
hospital_queue.enqueue("রোগী-ক (হার্ট অ্যাটাক)", 1)
hospital_queue.enqueue("রোগী-খ (জ্বর)", 4)
hospital_queue.enqueue("রোগী-গ (সিরিয়াস এক্সিডেন্ট)", 1)
hospital_queue.enqueue("রোগী-ঘ (হালকা ইনজুরি)", 3)

# চিকিৎসা দেওয়া (সর্বোচ্চ প্রাইওরিটি প্রথমে)
print(hospital_queue.dequeue())  # রোগী-ক বা রোগী-গ
print(hospital_queue.dequeue())  # বাকি সর্বোচ্চ প্রাইওরিটি
```

## **কোড সম্পূর্ণতা:**
```python
# সম্পূর্ণ হিপ ইমপ্লিমেন্টেশন
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)
    
    def get_min(self):
        return self.heap[0] if self.heap else None
    
    def extract_min(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[(i-1)//2]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2
    
    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left = 2*i + 1
            right = 2*i + 2
            
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break
    
    def size(self):
        return len(self.heap)
```

## **গুরুত্বপূর্ণ পয়েন্ট:**
1. হিপ সবসময় **ব্যালান্সড** থাকে
2. **হিপিফাই** অপারেশনের মাধ্যমে হিপ প্রপার্টি মেইনটেইন করা হয়
3. প্রাইওরিটি কিউ-তে **লোয়ার ভ্যালু = হাইয়ার প্রাইওরিটি** (মিন-হিপের জন্য)
4. Python-এর `heapq` মডিউল ব্যবহার করে সরাসরি হিপ অপারেশন করা যায়

এই ডাটা স্ট্রাকচারগুলি **ইন্টারভিউ এবং কম্পিটিটিভ প্রোগ্রামিং**-এ খুবই গুরুত্বপূর্ণ!