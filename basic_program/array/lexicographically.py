A = input()
B = input()

i = 0

while i < len(A) and i < len(B):
    if A[i] < B[i]:
        print(A)
        break
    elif A[i] > B[i]:
        print(B)
        break
    i += 1
else:
    # যদি একটার length ছোট হয়
    if len(A) < len(B):
        print(A)
    else:
        print(B)
