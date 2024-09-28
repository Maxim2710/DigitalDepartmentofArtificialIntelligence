def sort_key(a):
    cntA = a.count('1')

    return (cntA, -int(a))

numbers = input().split()

numbers.sort(reverse=True, key=sort_key)

print(' '.join(numbers))
