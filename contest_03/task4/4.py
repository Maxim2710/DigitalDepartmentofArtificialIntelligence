def hanoi(n, src='a', dest='b', aux='c'):
    if n == 1:
        yield (src, dest)  
    else:
        yield from hanoi(n - 1, src, aux, dest)
        yield (src, dest)
        yield from hanoi(n - 1, aux, dest, src)


n = int(input())
steps = hanoi(n)

towers = {'a': list(range(n, 0, -1)), 'b': [], 'c': []}

for src, dest in steps:
    towers[dest].append(towers[src].pop())

    is_sorted = all(tower[i] > tower[i + 1] for tower in towers.values() for i in range(len(tower) - 1))
    if not is_sorted:
        print('NO')
        exit(1)

expected = {'a': [], 'b': list(range(n, 0, -1)), 'c': []}

print('YES' if towers == expected else 'NO')
