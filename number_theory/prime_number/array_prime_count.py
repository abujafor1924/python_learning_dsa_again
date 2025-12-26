






# ------------------------------
# প্রাইম সংখ্যা চেক করার ফাংশন
# ------------------------------
def is_prime(n):
    # যদি n <= 1 হয়, তাহলে প্রাইম নয়
    if n <= 1:
        print(f"{n} প্রাইম নয় (কারণ এটি 1 বা তার কম)")
        return False
    
    # 2 থেকে sqrt(n) পর্যন্ত চেক করবো
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} প্রাইম নয় (কারণ {i} দ্বারা ভাগ যায়)")
            return False
    
    # যদি কোন divisor না পাওয়া যায়, তাহলে প্রাইম
    print(f"{n} প্রাইম সংখ্যা")
    return True

print(is_prime(11))


arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_in_arr = []

for num in arr:
    if is_prime(num):
        prime_in_arr.append(num)

print("অ্যারে থেকে প্রাইম সংখ্যা:", prime_in_arr)
print("মোট প্রাইম সংখ্যা অ্যারেতে:", len(prime_in_arr))
