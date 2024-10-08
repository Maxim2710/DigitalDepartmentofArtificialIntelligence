def calculate_water(n, heights):
    if n <= 1:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    total_water = 0
    for i in range(n):
        water_at_i = min(left_max[i], right_max[i]) - heights[i]
        if water_at_i > 0:
            total_water += water_at_i

    return total_water


n = int(input())
heights = list(map(int, input().split()))
print(calculate_water(n, heights))
