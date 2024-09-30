import numpy as np

k, m = map(int, input().split())

matrix = np.array([list(map(float, input().split())) for _ in range(k)])

def normalize_row(row):
    norm = np.sqrt(np.sum(row ** 2))
    if norm == 0:
        return row
    return row / norm

normalized_matrix = np.array([normalize_row(row) for row in matrix])

normalized_matrix = np.round(normalized_matrix, 2)

for row in normalized_matrix:
    print(' '.join(map(str, row)))
