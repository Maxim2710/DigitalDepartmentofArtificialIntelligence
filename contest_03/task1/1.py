def min_number(n):
    if n == 1:
        return 1

    factors = []

    for i in range(9, 1, -1):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n != 1:
        return 0

    factors.sort()
    result = int(''.join(map(str, factors)))

    return result


n = int(input())

print(min_number(n))
