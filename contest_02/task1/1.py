from collections import Counter

n = int(input().strip())

numbers = list(map(int, input().strip().split()))

counter = Counter(numbers)

most_common_number = counter.most_common(1)[0][0]

print(most_common_number)
