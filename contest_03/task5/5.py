from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if token in logged:
            return func(*args, **kwargs)
        else:
            print("Access denied")
            return None
    return wrapper

@login_required
def get_balance():
    login = logged[token]
    print(login, data[login]['balance'])

@login_required
def pay(amount):
    login = logged[token]
    if data[login]['balance'] >= amount:
        data[login]['balance'] -= amount
        print('Payment accepted')
    else:
        print('Not enough money')

data = {
        'john':  {'balance': 9},
        'alice': {'balance': 150},
        'bob':   {'balance': 200}
       }

logged = {}
for pair in input().split(', '):
    login, token_value = pair.split()
    logged[token_value] = login

token = input()

get_balance()
pay(10)
get_balance()
