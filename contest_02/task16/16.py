# import csv
#
# def load(filename):
#     data = {'salary': [], 'request': [], 'repaid': []}
#     with open(filename, newline='') as csvfile:
#         reader = csv.DictReader(csvfile, delimiter=';')
#         # Отладочный вывод заголовков
#         for row in reader:
#             data['salary'].append(float(row.get('salary', 0)))
#             data['request'].append(float(row.get('request', 0)))
#             data['repaid'].append(int(row.get('repaid', 0)))
#     return data
#
# def train(data):
#     """Обучает модель на основе данных и возвращает веса и порог."""
#     # Инициализация весов и порога
#     ws = 0.0  # вес для salary
#     wr = 1.0  # вес для request
#     b = 1.0  # порог
#     k = 0.01  # коэффициент скорости обучения
#
#     # Обучение
#     while True:
#         delta_sum = 0
#         for i in range(len(data['salary'])):
#             x1 = data['salary'][i]
#             x2 = data['request'][i]
#             d = data['repaid'][i]
#             z = x1 * ws + x2 * wr - b
#             y = 1 if z >= 0 else 0
#             delta = d - y
#
#             if delta != 0:
#                 ws += x1 * delta * k
#                 wr += x2 * delta * k
#                 b += -delta * k
#                 delta_sum += abs(delta)
#
#         # Окончание обучения, если дельта мала
#         if delta_sum == 0:
#             break
#
#     return {'ws': ws, 'wr': wr, 'b': b}
#
# def predict(model, client):
#     """Делает предсказание на основе обученной модели и данных клиента."""
#     ws = model['ws']
#     wr = model['wr']
#     b = model['b']
#
#     x1 = client['salary']
#     x2 = client['request']
#     z = x1 * ws + x2 * wr - b
#
#     return z >= 0
#
# def main():
#     # Загрузка данных и обучение модели
#     data = load('data.csv')
#     model = train(data)
#
#     # Ввод данных клиента
#     client = dict(zip(['salary', 'request'], map(float, input().split())))
#
#     # Предсказание и вывод результата
#     result = predict(model, client)
#     print('YES' if result else 'NO')
#
# if __name__ == '__main__':
#     main()
#

# import csv
#
# def load(filename):
#     data = {'salary': [], 'request': [], 'repaid': []}
#     with open(filename, newline='') as csvfile:
#         reader = csv.DictReader(csvfile, delimiter=';')
#         for row in reader:
#             data['salary'].append(float(row.get('salary', 0)))
#             data['request'].append(float(row.get('request', 0)))
#             data['repaid'].append(int(row.get('repaid', 0)))
#     return data
#
# def train(data):
#     ws = 0.0
#     wr = 1.0
#     b = 1.0
#     k = 0.01
#     epsilon = 1e-5
#
#     while True:
#         delta_sum = 0
#         for i in range(len(data['salary'])):
#             x1 = data['salary'][i]
#             x2 = data['request'][i]
#             d = data['repaid'][i]
#             z = x1 * ws + x2 * wr - b
#             y = 1 if z >= 0 else 0
#             delta = d - y
#
#             if delta != 0:
#                 ws += x1 * delta * k
#                 wr += x2 * delta * k
#                 b += -delta * k
#                 delta_sum += abs(delta)
#
#         if delta_sum < epsilon:
#             break
#
#     return {'ws': ws, 'wr': wr, 'b': b}
#
# def predict(model, client):
#     ws = model['ws']
#     wr = model['wr']
#     b = model['b']
#
#     x1 = client['salary']
#     x2 = client['request']
#     z = x1 * ws + x2 * wr - b
#
#     return z >= 0
#
# client = dict(zip(['salary', 'request'], map(float, input().split())))
# # Ваш код будет вставлен сюда
# data = load('data.csv')
# brain = train(data)
# print('YES' if predict(brain, client) else 'NO')


import csv

def load(filename):
    data = {'salary': [], 'request': [], 'repaid': []}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            cleaned_row = {k.strip(): v for k, v in row.items()}
            data['salary'].append(float(cleaned_row.get('salary', 0)))
            data['request'].append(float(cleaned_row.get('request', 0)))
            data['repaid'].append(int(cleaned_row.get('repaid', 0)))
    return data

def train(data):
    ws = 0.0
    wr = 1.0
    b = 1.0
    k = 0.01
    epsilon = 1e-5

    while True:
        delta_sum = 0
        for i in range(len(data['salary'])):
            x1 = data['salary'][i]
            x2 = data['request'][i]
            d = data['repaid'][i]
            z = x1 * ws + x2 * wr - b
            y = 1 if z >= 0 else 0
            delta = d - y

            if delta != 0:
                ws += x1 * delta * k
                wr += x2 * delta * k
                b += -delta * k
                delta_sum += abs(delta)

        if delta_sum < epsilon:
            break

    return {'ws': ws, 'wr': wr, 'b': b}

def predict(model, client):
    ws = model['ws']
    wr = model['wr']
    b = model['b']

    x1 = client['salary']
    x2 = client['request']
    z = x1 * ws + x2 * wr - b

    return z >= 0

client = dict(zip(['salary', 'request'], map(float, input().split())))
data = load('data.csv')
brain = train(data)
print('YES' if predict(brain, client) else 'NO')
