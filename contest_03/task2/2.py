def is_prime(*numbers, check='mask'):
    def is_single_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = tuple(is_single_prime(num) for num in numbers)

    if check == 'any':
        return any(primes)
    elif check == 'all':
        return all(primes)
    else:
        return primes


nums = [int(i) for i in input().split()]

print(*is_prime(*nums), is_prime(*nums, check='all'), is_prime(*nums, check='any'))
