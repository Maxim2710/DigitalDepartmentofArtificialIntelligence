import numpy as np

input_data = input().strip()

vector = np.array(list(map(float, input_data.split())))

sine_squared_vector = np.sin(vector ** 2)

min_value = np.min(sine_squared_vector)

print(round(min_value, 2))
