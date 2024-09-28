n = int(input().strip())

numbers = list(map(int, input().strip().split()))

unique_numbers = set(numbers)

unique_count = len(unique_numbers)

print(unique_count)
