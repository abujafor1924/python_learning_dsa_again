arr = list(map(int, input().split()))

q = int(input())  # কয়টা প্রশ্ন

for _ in range(q):
    i, j = map(int, input().split())
    print(arr[i] + arr[j])
