n = int(input().strip())

data = list(map(int, input().strip().split()))

smoothed_data = [0] * n

smoothed_data[0] = float(data[0])
smoothed_data[-1] = float(data[-1])

for i in range(1, n - 1):
    smoothed_data[i] = (data[i - 1] + data[i] + data[i + 1]) / 3.0

print(' '.join(f"{value:.15f}" for value in smoothed_data))
