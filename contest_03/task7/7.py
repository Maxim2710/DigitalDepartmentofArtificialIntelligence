import random

class Cat:
    def __init__(self):
        self.alive = random.choice([True, False])

    def is_alive(self):
        return self.alive

class Box:
    def open(self):
        return Cat()

box = Box()
cat = box.open()
if cat.is_alive():
    print('alive')
else:
    print('dead')
