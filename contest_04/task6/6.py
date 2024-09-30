import math

k, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(k)]

idf_values = []

for j in range(m):
    nt = sum(1 for i in range(k) if matrix[i][j] > 0)

    idf = math.log((k / (nt + 1))) + 1

    idf_values.append(round(idf, 2))

print(' '.join(map(str, idf_values)))
