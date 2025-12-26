arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primes = []

for num in arr:
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

print("Prime numbers in array:", primes)
print("Total prime numbers:", len(primes))
