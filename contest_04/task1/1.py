import numpy as np

input_data = input().strip()

vector = np.array(list(map(int, input_data.split())))

result_vector = np.where(vector > 127, 1, 0)

print(' '.join(map(str, result_vector)))
