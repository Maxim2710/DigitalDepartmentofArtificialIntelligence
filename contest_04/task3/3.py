import numpy as np
from scipy.signal import convolve2d

n, m = map(int, input().split())
matrix = np.array([list(map(int, input().split())) for _ in range(n)])

kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])

convolved = convolve2d(matrix, kernel, mode='valid')

convolved = np.clip(convolved, 0, 255)

convolved = convolved.astype(int)

for row in convolved:
    print(" ".join(map(str, row)))
