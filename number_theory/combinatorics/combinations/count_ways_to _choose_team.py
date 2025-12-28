def nCr(n, r):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) // (i + 1)
    return res

n, k = map(int, input().split())
print(nCr(n, k))
