class Water:
    def __init__(self, temperature):
        self.temperature = temperature

    def increase(self, amount):
        self.temperature += amount

class Teapot:
    def __init__(self, water):
        self.water = water

    def is_boiling(self):
        return self.water.temperature >= 100

    def heat_up(self, amount):
        self.water.increase(amount)

temperature, count = map(int, input().split())
heat = [int(t) for t in input().split()]

water = Water(temperature)
teapot = Teapot(water)

while not teapot.is_boiling() and heat:
    teapot.heat_up(heat.pop(0))

print(*heat)
