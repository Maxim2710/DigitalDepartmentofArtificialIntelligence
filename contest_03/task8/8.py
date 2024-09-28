class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def bonus(self, percent):
        return round(self.salary * percent)

    def calculate_salary(self):
        return self.salary + self.bonus(bonuses[self.position])

    def __repr__(self):
        return f"{self.name} ({self.position}): {self.calculate_salary()}"

class Manager(Employee):
    def __init__(self, name, salary=16242):
        super().__init__(name, 'manager', salary)

    def bonus(self, percent):
        percent = max(percent, 0.10)  # Минимум 10%
        return round(self.salary * percent)

class Boss(Employee):
    def __init__(self, name, salary=16242):
        super().__init__(name, 'boss', salary)

boss_bonus, manager_bonus = map(float, input().split())
bonuses = {'manager': manager_bonus, 'boss': boss_bonus}

john_money, bob_money, alice_money = map(int, input().split())
john = Boss('John', john_money)
bob = Manager('Bob', bob_money)
alice = Manager('Alice', alice_money)

print(john, bob, alice, sep='\n')
