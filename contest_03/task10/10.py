import math


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def r(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    @r.setter
    def r(self, value):
        a = self.a
        self._x = value * math.cos(a)
        self._y = value * math.sin(a)

    @property
    def a(self):
        return math.atan2(self._y, self._x)

    @a.setter
    def a(self, value):
        r = self.r
        self._x = r * math.cos(value)
        self._y = r * math.sin(value)


import json

x, y = map(float, input().split())
p = Point(x, y)

moves = json.loads(input())
for move in moves:
    ort, value = move['ort'], move['value']
    if ort == 'x':
        p.x += value
    elif ort == 'y':
        p.y += value
    elif ort == 'r':
        p.r += value
    elif ort == 'a':
        p.a += value
    print(round(p.x, 5), round(p.y, 5))
