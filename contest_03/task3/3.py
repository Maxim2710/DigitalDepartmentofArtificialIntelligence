def prime_nums():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

count = int(input())

prime = prime_nums()
for _ in range(count):
    print(next(prime))
