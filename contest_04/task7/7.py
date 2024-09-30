import numpy as np

input_data = input().strip()

vector = np.array(list(map(int, input_data.split())))

indices = np.where((vector >= -100) & (vector <= 100))[0]

print(' '.join(map(str, indices)))
