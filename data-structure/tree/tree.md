# Tree Data Structure in Python (বিস্তারিত)

## 🌳 **ট্রি কি?**
**ট্রি** একটি নন-লিনিয়ার ডাটা স্ট্রাকচার যা নোড (Node) এবং এজ (Edge) দিয়ে গঠিত। এটি সত্যিকারের গাছের মতো, যেখানে একটি মূল (Root) থেকে বিভিন্ন শাখা-প্রশাখা বিস্তৃত।

## 📊 **ট্রির প্রাথমিক ধারণা**

```python
# Tree Node Class in Python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # General Tree
        # OR for Binary Tree
        self.left = None
        self.right = None
```

## 🔑 **ট্রির গুরুত্বপূর্ণ টার্মিনোলজি**

### ১. **নোড (Node)**
ট্রির প্রতিটি উপাদানকে নোড বলে। প্রতিটি নোডে ডাটা এবং চাইল্ড নোডের রেফারেন্স থাকে।

### ২. **রুট (Root)**
ট্রির সবচেয়ে উপরের নোড। এটি কোনো নোডের চাইল্ড নয়।

### ৩. **প্যারেন্ট (Parent)**
যে নোডের এক বা একাধিক চাইল্ড নোড আছে।

### ৪. **চাইল্ড (Child)**
প্যারেন্ট নোডের সরাসরি সংযুক্ত নোড।

### ৫. **লিফ (Leaf)**
যে নোডের কোনো চাইল্ড নেই।

### ৬. **সাবট্রি (Subtree)**
কোনো নোড এবং তার সমস্ত ডিসেনডেন্ট নিয়ে গঠিত অংশ।

### ৭. **ডিপথ (Depth)**
রুট থেকে ঐ নোড পর্যন্ত এজের সংখ্যা।

### ৮. **হাইট (Height)**
নোড থেকে সবচেয়ে দূরের লিফ পর্যন্ত পথের দৈর্ঘ্য।

## 🌲 **ট্রির প্রকারভেদ**

### ১. **বাইনারি ট্রি (Binary Tree)**
- প্রতিটি নোডের সর্বোচ্চ ২টি চাইল্ড
```python
# Binary Tree Example
#        1
#       / \
#      2   3
#     / \
#    4   5
```

### ২. **বাইনারি সার্চ ট্রি (Binary Search Tree - BST)**
- বাম সাবট্রির সকল নোড ≤ প্যারেন্ট নোড
- ডান সাবট্রির সকল নোড ≥ প্যারেন্ট নোড
```python
# BST Example
#        50
#       /  \
#     30    70
#    /  \   / \
#   20  40 60 80
```

### ৩. **অ্যাভিএল ট্রি (AVL Tree)**
- সেলফ-ব্যালান্সিং BST
- প্রতিটি নোডের জন্য বাম-ডান সাবট্রির উচ্চতার পার্থক্য ≤ ১

### ৪. **হিপ (Heap)**
- কমপ্লিট বাইনারি ট্রি
- **ম্যাক্স-হিপ:** প্যারেন্ট ≥ চাইল্ড
- **মিন-হিপ:** প্যারেন্ট ≤ চাইল্ড

## 📝 **ট্রি ট্রাভারসাল (অতিক্রম) পদ্ধতি**

### ১. **প্রি-অর্ডার (Pre-order)**
**রুট → বাম → ডান**
```python
def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=" ")  # রুট
    preorder_traversal(root.left)  # বাম
    preorder_traversal(root.right)  # ডান
```

### ২. **ইন-অর্ডার (In-order)**
**বাম → রুট → ডান**
```python
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)  # বাম
    print(root.data, end=" ")  # রুট
    inorder_traversal(root.right)  # ডান
```

### ৩. **পোস্ট-অর্ডার (Post-order)**
**বাম → ডান → রুট**
```python
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)  # বাম
    postorder_traversal(root.right)  # ডান
    print(root.data, end=" ")  # রুট
```

### ৪. **লেভেল-অর্ডার (Level-order)**
**উপরে থেকে নিচে, বাম থেকে ডানে**
```python
from collections import deque

def levelorder_traversal(root):
    if root is None:
        return
    
    queue = deque()
    queue.append(root)
    
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

## 💻 **ট্রি ইমপ্লিমেন্টেশন উদাহরণ**

### Python-এ বাইনারি ট্রি তৈরি:
```python
class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        # Level order insertion (for complete binary tree)
        queue = [node]
        while queue:
            current = queue.pop(0)
            
            if current.left is None:
                current.left = TreeNode(value)
                return
            else:
                queue.append(current.left)
            
            if current.right is None:
                current.right = TreeNode(value)
                return
            else:
                queue.append(current.right)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.data == value:
            return node
        
        # Search in left subtree
        left_result = self._search_recursive(node.left, value)
        if left_result:
            return left_result
        
        # Search in right subtree
        return self._search_recursive(node.right, value)
    
    def print_tree(self, traversal_type='inorder'):
        if traversal_type == 'preorder':
            print("Pre-order: ", end="")
            self.preorder_traversal(self.root)
        elif traversal_type == 'inorder':
            print("In-order: ", end="")
            self.inorder_traversal(self.root)
        elif traversal_type == 'postorder':
            print("Post-order: ", end="")
            self.postorder_traversal(self.root)
        elif traversal_type == 'levelorder':
            print("Level-order: ", end="")
            self.levelorder_traversal(self.root)
        print()
    
    # Traversal methods
    def preorder_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)
    
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")
    
    def levelorder_traversal(self, root):
        if root is None:
            return
        
        from collections import deque
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            print(node.data, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Example Usage
if __name__ == "__main__":
    tree = BinaryTree()
    
    # Insert values
    values = [1, 2, 3, 4, 5, 6, 7]
    for val in values:
        tree.insert(val)
    
    # Different traversals
    tree.print_tree('preorder')    # Pre-order: 1 2 4 5 3 6 7 
    tree.print_tree('inorder')     # In-order: 4 2 5 1 6 3 7
    tree.print_tree('postorder')   # Post-order: 4 5 2 6 7 3 1
    tree.print_tree('levelorder')  # Level-order: 1 2 3 4 5 6 7
    
    # Search for a value
    search_value = 5
    result = tree.search(search_value)
    if result:
        print(f"{search_value} পাওয়া গেছে")
    else:
        print(f"{search_value} পাওয়া যায়নি")
```

### Python-এ Binary Search Tree (BST) তৈরি:
```python
class BSTNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.data:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)
        # Ignore duplicates
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.data == value:
            return node
        
        if value < node.data:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return node
        
        if value < node.data:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.data:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children
            # Get inorder successor (smallest in right subtree)
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete_recursive(node.right, temp.data)
        
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

# Example Usage of BST
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    
    # Inorder traversal should give sorted list
    print("In-order Traversal (Sorted):", bst.inorder_traversal())
    # Output: [20, 30, 40, 50, 60, 70, 80]
    
    # Search operations
    print("Search 40:", "Found" if bst.search(40) else "Not Found")
    print("Search 90:", "Found" if bst.search(90) else "Not Found")
    
    # Delete operation
    bst.delete(30)
    print("After deleting 30:", bst.inorder_traversal())
```

## 📊 **ট্রির অ্যাপ্লিকেশন**

### ১. **ফাইল সিস্টেম**
- ডিরেক্টরি স্ট্রাকচার
- ফাইল অর্গানাইজেশন

### ২. **ডাটাবেস সিস্টেম**
- ইনডেক্সিং (B-tree, B+ tree)
- হায়ারার্কিকাল ডাটা

### ৩. **কম্প্রেশন অ্যালগরিদম**
- হাফম্যান কোডিং ট্রি
```python
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Count frequency of each character
    frequency = Counter(text)
    
    # Create priority queue
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Build Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0]
```

### ৪. **অ্যাক্সপ্রেশন ট্রি**
- গাণিতিক এক্সপ্রেশন পার্সিং
```python
class ExpressionTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate_expression_tree(root):
    if root is None:
        return 0
    
    # If leaf node (operand)
    if root.left is None and root.right is None:
        return int(root.value)
    
    # Evaluate left and right subtrees
    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)
    
    # Apply operator
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val / right_val
    
    return 0

# Example: (3 + 5) * (10 - 6)
#        *
#       / \
#      +   -
#     / \ / \
#    3  5 10 6
```

## ⚡ **ট্রি অ্যালগরিদম উদাহরণ**

### ১. **ট্রির হাইট বের করা**
```python
def tree_height(root):
    if root is None:
        return 0
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return max(left_height, right_height) + 1
```

### ২. **ট্রিতে নোড সংখ্যা**
```python
def count_nodes(root):
    if root is None:
        return 0
    
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

### ৩. **লিফ নোড সংখ্যা**
```python
def count_leaf_nodes(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)
```

### ৪. **ট্রি মিরর/ইনভার্ট করা**
```python
def invert_tree(root):
    if root is None:
        return None
    
    # Swap left and right subtrees
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root
```

### ৫. **ট্রি সিমেট্রিক কিনা চেক করা**
```python
def is_symmetric(root):
    def is_mirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        
        return (left.data == right.data and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    if root is None:
        return True
    
    return is_mirror(root.left, root.right)
```

## 📊 **ট্রি ভিজ্যুয়ালাইজেশন**
```python
def print_tree_visual(root, space=0, level_spacing=5):
    if root is None:
        return
    
    # Increase distance between levels
    space += level_spacing
    
    # Process right child first
    print_tree_visual(root.right, space)
    
    # Print current node after space
    print()
    for _ in range(level_spacing, space):
        print(" ", end="")
    print(root.data)
    
    # Process left child
    print_tree_visual(root.left, space)

# Example tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
```

## 🎯 **প্র্যাকটিস সমস্যা সমাধান**

### সমস্যা ১: BST-তে k-th ক্ষুদ্রতম এলিমেন্ট
```python
def kth_smallest_bst(root, k):
    stack = []
    current = root
    count = 0
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        count += 1
        
        if count == k:
            return current.data
        
        current = current.right
    
    return None
```

### সমস্যা ২: ট্রির ডায়ামিটার (দীর্ঘতম পথ)
```python
def diameter_of_tree(root):
    diameter = [0]  # Use list to pass by reference
    
    def height(node):
        if node is None:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        # Update diameter
        diameter[0] = max(diameter[0], left_height + right_height)
        
        return max(left_height, right_height) + 1
    
    height(root)
    return diameter[0]
```

### সমস্যা ৩: ট্রিতে পাথ সমূহ প্রিন্ট
```python
def print_all_paths(root):
    def dfs(node, current_path, all_paths):
        if node is None:
            return
        
        current_path.append(node.data)
        
        # If leaf node, save the path
        if node.left is None and node.right is None:
            all_paths.append(list(current_path))
        else:
            dfs(node.left, current_path, all_paths)
            dfs(node.right, current_path, all_paths)
        
        # Backtrack
        current_path.pop()
    
    all_paths = []
    dfs(root, [], all_paths)
    return all_paths
```

## 📚 **ট্রি সম্পর্কিত Python লাইব্রেরি**

```python
# ১. heapq - Min Heap implementation
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
print(heapq.heappop(heap))  # 2 (min element)

# ২. bisect - Binary search on sorted lists
import bisect

sorted_list = [1, 3, 4, 4, 6, 8]
pos = bisect.bisect_left(sorted_list, 4)  # First position where 4 can be inserted
print(pos)  # 2

# ৩. collections.deque - Efficient queue for level order traversal
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)  # Add to right
queue.appendleft(0)  # Add to left
```

## 💡 **টিপস এবং ট্রিকস**

১. **রিকার্শন ব্যবহার করুন**: ট্রি অ্যালগরিদম রিকার্শন দিয়ে সহজে ইমপ্লিমেন্ট করা যায়।

২. **Python-এর Recursion Limit**: ডিফল্ট রিকার্শন লিমিট 1000। বড় ট্রির জন্য বাড়াতে পারেন:
```python
import sys
sys.setrecursionlimit(10000)
```

৩. **Generator ব্যবহার**: বড় ট্রি ট্রাভারসালের জন্য জেনারেটর ব্যবহার করুন:
```python
def inorder_generator(root):
    if root:
        yield from inorder_generator(root.left)
        yield root.data
        yield from inorder_generator(root.right)

# Usage
for value in inorder_generator(tree.root):
    print(value)
```

৪. **Memoization**: রিকার্শন সহ পুনরায় গণনা এড়াতে:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def tree_depth_cached(node_id):
    # Implement with caching
    pass
```

## 🎯 **ইন্টারভিউ প্রস্তুতি**

### সাধারণ প্রশ্ন:
১. **ট্রি এবং গ্রাফের পার্থক্য কি?**
   - ট্রিতে সাইকেল নেই, গ্রাফে থাকতে পারে
   - ট্রি ডিরেক্টেড, গ্রাফ ডিরেক্টেড বা আনডিরেক্টেড হতে পারে

২. **BST কেন গুরুত্বপূর্ণ?**
   - O(log n) সার্চ, ইনসার্ট, ডিলিট
   - ইন-অর্ডার ট্রাভারসালে সর্টেড ডাটা দেয়

৩. **AVL ট্রি কেন ব্যবহার করবেন?**
   - BST আনব্যালান্স হতে পারে (লিনিয়ার লিংকড লিস্টের মতো)
   - AVL স্বয়ংক্রিয়ভাবে ব্যালান্স করে

### কোডিং প্রব্লেম:
```python
# চেক করুন ট্রি BST কি না
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    
    if not (min_val < root.data < max_val):
        return False
    
    return (is_valid_bst(root.left, min_val, root.data) and
            is_valid_bst(root.right, root.data, max_val))
```

## 📊 **পারফরম্যান্স বিশ্লেষণ**

| অপারেশন | সাধারণ BST | ব্যালান্স BST | হিপ |
|---------|------------|----------------|-----|
| সার্চ | O(n) | O(log n) | O(n) |
| ইনসার্ট | O(n) | O(log n) | O(log n) |
| ডিলিট | O(n) | O(log n) | O(log n) |
| মিন/ম্যাক্স | O(n) | O(log n) | O(1) |

## 🚀 **নেক্সট স্টেপস**

১. **গ্রাফ ডাটা স্ট্রাকচার** শিখুন
২. **ডাইনামিক প্রোগ্রামিং** দিয়ে ট্রি প্রব্লেম সল্ভ করুন
৩. **ট্রি সিরিয়ালাইজেশন** শিখুন
৪. **Segment Tree** এবং **Fenwick Tree** শিখুন
৫. **Trie** ডাটা স্ট্রাকচার শিখুন (অটোকমপ্লিট, স্পেল চেক)

---

## ✅ **মনে রাখার মূল বিষয়**
- Python-এ ট্রি ইমপ্লিমেন্টেশন সহজ রিকার্শনের মাধ্যমে
- BST গুরুত্বপূর্ণ সর্টেড অপারেশনের জন্য
- ট্রি ট্রাভারসাল চার প্রকার, প্রত্যেকের আলাদা ব্যবহার
- রিয়েল-ওয়ার্ল্ডে ট্রির বহু অ্যাপ্লিকেশন আছে
- ইন্টারভিউতে ট্রি খুব কমন টপিক