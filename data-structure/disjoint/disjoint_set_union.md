# Disjoint Set Union (Union-Find) ডেটা স্ট্রাকচার

## ধারণা
Disjoint Set Union (DSU) বা Union-Find একটি ডেটা স্ট্রাকচার যা disjoint sets (সংযোগহীন সেট) ম্যানেজ করতে ব্যবহৃত হয়। এটি প্রধানত দুইটি অপারেশন সাপোর্ট করে:
1. **Union**: দুইটি সেটকে একত্রিত করা
2. **Find**: কোন এলিমেন্ট কোন সেটে আছে তা বের করা

## প্রধান বৈশিষ্ট্য
- প্রতিটি সেটের একটি representative বা parent নোড থাকে
- Path compression অপ্টিমাইজেশন
- Union by rank/size অপ্টিমাইজেশন

## বাস্তবায়ন (Python)

```python
class DisjointSetUnion:
    def __init__(self, n):
        """
        n: মোট নোডের সংখ্যা
        """
        self.parent = [i for i in range(n)]  # প্রতিটি নোড নিজেই তার parent
        self.rank = [0] * n  # ট্রির উচ্চতা/র‍্যাঙ্ক
        self.size = [1] * n  # প্রতিটি সেটের সাইজ
        
    def find(self, x):
        """
        x নোডের রুট/প্রতিনিধি খুঁজে বের করা
        Path compression ব্যবহার করা হয়েছে
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # পাথ কম্প্রেশন
        return self.parent[x]
    
    def union(self, x, y):
        """
        x এবং y নোডের সেটগুলো একত্রিত করা
        Union by rank ব্যবহার করা হয়েছে
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return  # একই সেটে আছে
        
        # Union by rank: ছোট ট্রিকে বড় ট্রির নিচে যুক্ত করা
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            # র‍্যাঙ্ক সমান হলে যেকোনো একটিকে রুট বানানো
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            self.size[root_x] += self.size[root_y]
    
    def connected(self, x, y):
        """x এবং y একই সেটে আছে কিনা চেক করা"""
        return self.find(x) == self.find(y)
    
    def get_size(self, x):
        """x নোডের সেটের সাইজ রিটার্ন করা"""
        root = self.find(x)
        return self.size[root]
    
    def get_sets(self):
        """সবগুলো সেট আলাদা আলাদা রিটার্ন করা"""
        sets = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in sets:
                sets[root] = []
            sets[root].append(i)
        return list(sets.values())

# উদাহরণ ব্যবহার ১: বেসিক উদাহরণ
print("=== উদাহরণ ১: বেসিক ইউনিয়ন-ফাইন্ড ===")
dsu = DisjointSetUnion(7)  # 0 থেকে 6 পর্যন্ত 7টি নোড

# কিছু ইউনিয়ন অপারেশন
dsu.union(0, 1)
dsu.union(1, 2)
dsu.union(3, 4)
dsu.union(5, 6)

print(f"0 এবং 2 সংযুক্ত? {dsu.connected(0, 2)}")  # True
print(f"0 এবং 3 সংযুক্ত? {dsu.connected(0, 3)}")  # False
print(f"3 এবং 4 সংযুক্ত? {dsu.connected(3, 4)}")  # True
print(f"5 এবং 6 সংযুক্ত? {dsu.connected(5, 6)}")  # True

print(f"\nসকল সেট:")
for s in dsu.get_sets():
    print(s)

# উদাহরণ ব্যবহার ২: গ্রাফের কানেক্টেড কম্পোনেন্ট
print("\n=== উদাহরণ ২: গ্রাফের কানেক্টেড কম্পোনেন্ট ===")

def find_connected_components(n, edges):
    """
    n: নোড সংখ্যা
    edges: এজের তালিকা [(u, v), ...]
    """
    dsu = DisjointSetUnion(n)
    
    for u, v in edges:
        dsu.union(u, v)
    
    return dsu.get_sets()

# গ্রাফ উদাহরণ
n = 6
edges = [(0, 1), (1, 2), (3, 4), (4, 5)]

components = find_connected_components(n, edges)
print(f"কানেক্টেড কম্পোনেন্ট সংখ্যা: {len(components)}")
print(f"কম্পোনেন্টগুলো: {components}")

# উদাহরণ ব্যবহার ৩: ফ্রেন্ড সার্কেল
print("\n=== উদাহরণ ৩: ফ্রেন্ড সার্কেল ===")

class FriendNetwork:
    def __init__(self):
        self.dsu = DisjointSetUnion(10)  # 10 জন বন্ধু
        self.names = {
            0: "রahim", 1: "Karim", 2: "সুইটি", 
            3: "জনি", 4: "মিমি", 5: "রনি",
            6: "বনি", 7: "টনি", 8: "মনি", 9: "সনি"
        }
    
    def add_friendship(self, person1, person2):
        """দুইজন বন্ধুত্ব করানো"""
        self.dsu.union(person1, person2)
        print(f"{self.names[person1]} এবং {self.names[person2]} বন্ধুত্ব করল!")
    
    def are_friends(self, person1, person2):
        """দুইজন পরস্পরের বন্ধু কিনা"""
        return self.dsu.connected(person1, person2)
    
    def show_friend_groups(self):
        """সকল ফ্রেন্ড গ্রুপ দেখানো"""
        groups = self.dsu.get_sets()
        print("\nফ্রেন্ড গ্রুপগুলো:")
        for i, group in enumerate(groups, 1):
            names = [self.names[idx] for idx in group]
            print(f"গ্রুপ {i}: {', '.join(names)}")

# ফ্রেন্ড নেটওয়ার্ক তৈরি
network = FriendNetwork()

# বন্ধুত্ব তৈরি
network.add_friendship(0, 1)  # রahim এবং Karim
network.add_friendship(1, 2)  # Karim এবং সুইটি
network.add_friendship(3, 4)  # জনি এবং মিমি
network.add_friendship(4, 5)  # মিমি এবং রনি
network.add_friendship(6, 7)  # বনি এবং টনি
network.add_friendship(8, 9)  # মনি এবং সনি
network.add_friendship(2, 3)  # সুইটি এবং জনি (দুই গ্রুপ যুক্ত হবে)

# চেক করা
print(f"\nKarim এবং মিমি বন্ধু? {network.are_friends(1, 4)}")
print(f"বনি এবং সনি বন্ধু? {network.are_friends(6, 9)}")

network.show_friend_groups()
```

## টাইম কমপ্লেক্সিটি
- **Find (পাথ কম্প্রেশন সহ)**: প্রায় O(α(n)) - অ্যাকারম্যান ইনভার্স ফাংশন
- **Union**: প্রায় O(α(n))
- **α(n)**: প্রায় ধ্রুবক, n ≤ 10^600 এর জন্য α(n) ≤ 5

## ব্যবহারের ক্ষেত্র
1. **গ্রাফের কানেক্টেড কম্পোনেন্ট** খুঁজে বের করা
2. **Kruskal's অ্যালগরিদম** - Minimum Spanning Tree
3. **সাইকেল ডিটেকশন** - আনডিরেক্টেড গ্রাফে
4. **ইমেজ প্রসেসিং** - পিক্সেল কানেক্টিভিটি
5. **সোশ্যাল নেটওয়ার্ক** - ফ্রেন্ড সার্কেল

## অপ্টিমাইজেশন টেকনিক
1. **Path Compression**: Find অপারেশনের সময় সব নোডকে সরাসরি রুটের সাথে যুক্ত করা
2. **Union by Rank/Size**: ছোট ট্রিকে বড় ট্রির নিচে যুক্ত করা

## সুবিধা
- অত্যন্ত দক্ষ (প্রায় ধ্রুবক সময়)
- ইমপ্লিমেন্টেশন সহজ
- মেমোরি এফিসিয়েন্ট

## অসুবিধা
- ডাইনামিক সেট অপারেশনের জন্য উপযোগী নয়
- সেট থেকে এলিমেন্ট রিমুভ করা যায় না

DSU ডেটা স্ট্রাকচার কম্পিটিটিভ প্রোগ্রামিং এবং বিভিন্ন অ্যালগরিদমে ব্যাপকভাবে ব্যবহৃত হয়, বিশেষ করে যখন গ্রাফ বা নেটওয়ার্ক সম্পর্কিত সমস্যা সমাধান করতে হয়।