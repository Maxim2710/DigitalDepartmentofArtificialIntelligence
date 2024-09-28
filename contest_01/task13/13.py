low, high = map(int, input().split())

def count_odds(n):
    return (n + 1) // 2

count_high = count_odds(high)
count_low_minus_1 = count_odds(low - 1)

result = count_high - count_low_minus_1

print(result)
