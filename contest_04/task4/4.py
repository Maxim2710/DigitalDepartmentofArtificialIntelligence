import numpy as np

k, m = map(int, input().strip().split())

matrix_a = np.array([list(map(float, input().strip().split())) for _ in range(k)])

matrix_b = np.array([list(map(float, input().strip().split())) for _ in range(k)])

n = k * m
msd = np.sum((matrix_a - matrix_b) ** 2) / n

print(round(msd, 2))
