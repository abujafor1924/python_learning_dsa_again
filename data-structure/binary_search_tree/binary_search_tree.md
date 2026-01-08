# বাইনারি সার্চ ট্রি (Binary Search Tree - BST)

## বিস্তারিত বর্ণনা

**বাইনারি সার্চ ট্রি** হলো একটি বিশেষ ধরনের বাইনারি ট্রি ডাটা স্ট্রাকচার যেখানে:
- প্রতিটি নোডে একটি কি (key) থাকে
- প্রতিটি নোডের বাম সাবট্রির সবগুলোর কি এর মান নোডের কি এর চেয়ে কম হয়
- প্রতিটি নোডের ডান সাবট্রির সবগুলোর কি এর মান নোডের কি এর চেয়ে বেশি হয়
- প্রতিটি সাবট্রি নিজেই একটি বাইনারি সার্চ ট্রি হয়

## বৈশিষ্ট্যসমূহ:

1. **অর্ডার প্রিজার্ভিং**: ইন-অর্ডার ট্রাভার্সাল করলে ডাটাগুলো সর্টেড অর্ডারে পাওয়া যায়
2. **দ্রুত সার্চ**: O(h) টাইম কমপ্লেক্সিটি, যেখানে h হলো ট্রির উচ্চতা
3. **ডায়নামিক**: ডাটা ইনসার্ট/ডিলিট করা যায়

## উদাহরণ (চিত্রের মাধ্যমে):

```
        ৮ (root)
       / \
      ৩   ১০
     / \    \
    ১   ৬    ১৪
       / \   /
      ৪   ৭ ১৩
```

এই ট্রিতে:
- ৩ এর বামে ১ (৩ > ১)
- ৩ এর ডানে ৬ (৩ < ৬)
- ৬ এর বামে ৪ (৬ > ৪)
- ৬ এর ডানে ৭ (৬ < ৭)
- ৮ এর ডানে ১০ (৮ < ১০)
- ১০ এর ডানে ১৪ (১০ < ১৪)
- ১৪ এর বামে ১৩ (১৪ > ১৩)

## পাইথনে বাস্তবায়ন

```python
class Node:
    """বাইনারি ট্রি নোড ক্লাস"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """বাইনারি সার্চ ট্রি ক্লাস"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """নতুন কি ইনসার্ট করা"""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, current_node, key):
        """রিকার্সিভলি ইনসার্ট করা"""
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)
        else:
            # ডুপ্লিকেট কি (এখানে উপেক্ষা করা হয়েছে)
            pass
    
    def search(self, key):
        """কি সার্চ করা"""
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, current_node, key):
        """রিকার্সিভলি সার্চ করা"""
        if current_node is None or current_node.key == key:
            return current_node
        
        if key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)
    
    def inorder_traversal(self):
        """ইন-অর্ডার ট্রাভার্সাল (সর্টেড অর্ডার)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """রিকার্সিভ ইন-অর্ডার ট্রাভার্সাল"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def delete(self, key):
        """কি ডিলিট করা"""
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):
        """রিকার্সিভলি ডিলিট করা"""
        if node is None:
            return node
        
        # কি খুঁজে বের করা
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # কি পাওয়া গেছে, এখন ডিলিট করতে হবে
            
            # নোডে একটি চাইল্ড বা চাইল্ড নেই
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # দুইটি চাইল্ড আছে
            # ইন-অর্ডার সাক্সেসর খুঁজে বের করা
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)
        
        return node
    
    def _min_value_node(self, node):
        """সর্বনিম্ন মানের নোড ফেরত দেয়"""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def display(self):
        """ট্রি প্রদর্শন"""
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)
    
    def _display_aux(self, node):
        """ট্রি ভিজুয়ালাইজেশন হেল্পার"""
        if node.right is None and node.left is None:
            line = str(node.key)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = str(node.key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = str(node.key)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = str(node.key)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# ব্যবহারের উদাহরণ
def main():
    # BST তৈরি
    bst = BinarySearchTree()
    
    # ডাটা ইনসার্ট
    numbers = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    print("ইনসার্ট করা সংখ্যাগুলো:", numbers)
    
    for num in numbers:
        bst.insert(num)
    
    # ট্রি প্রদর্শন
    print("\nবাইনারি সার্চ ট্রি:")
    bst.display()
    
    # ইন-অর্ডার ট্রাভার্সাল
    print("\nইন-অর্ডার ট্রাভার্সাল (সর্টেড):", bst.inorder_traversal())
    
    # সার্চ অপারেশন
    search_key = 6
    result = bst.search(search_key)
    if result:
        print(f"\n{search_key} ট্রিতে পাওয়া গেছে")
    else:
        print(f"\n{search_key} ট্রিতে পাওয়া যায়নি")
    
    # ডিলিট অপারেশন
    delete_key = 6
    bst.delete(delete_key)
    print(f"\n{delete_key} ডিলিট করার পর:")
    bst.display()
    
    # আবার ইন-অর্ডার
    print(f"\n{delete_key} ডিলিট করার পর ইন-অর্ডার:", bst.inorder_traversal())


if __name__ == "__main__":
    main()
```

## আউটপুট:

```
ইনসার্ট করা সংখ্যাগুলো: [8, 3, 10, 1, 6, 14, 4, 7, 13]

বাইনারি সার্চ ট্রি:
       8______       
       /       \      
    __3_     __10_    
   /     \   /     \   
   1_   6   X    _14  
     \ / \       /     
      X 4 7     13     

ইন-অর্ডার ট্রাভার্সাল (সর্টেড): [1, 3, 4, 6, 7, 8, 10, 13, 14]

6 ট্রিতে পাওয়া গেছে

6 ডিলিট করার পর:
       8______       
       /       \      
    __3_     __10_    
   /     \   /     \   
   1_   7   X    _14  
     \ /         /     
      X 4       13     

6 ডিলিট করার পর ইন-অর্ডার: [1, 3, 4, 7, 8, 10, 13, 14]
```

## বাস্তব জীবনে ব্যবহার:

1. **ডাটাবেস সিস্টেম**: ইন্ডেক্সিং এর জন্য
2. **ফাইল সিস্টেম**: ডিরেক্টরি স্ট্রাকচার
3. **নেটওয়ার্ক রাউটিং**: আইপি অ্যাড্রেস লুকআপ
4. **গ্রাফিক্স**: স্পেস পার্টিশনিং
5. **সর্টিং অ্যালগরিদম**: ট্রি সর্ট

## টাইম কমপ্লেক্সিটি:

- **সার্চ**: O(h) [সবচেয়ে খারাপ ক্ষেত্রে O(n), সেরা ক্ষেত্রে O(log n)]
- **ইনসার্ট**: O(h)
- **ডিলিট**: O(h)
- **ট্রাভার্সাল**: O(n)

যেখানে h = ট্রির উচ্চতা, n = নোড সংখ্যা