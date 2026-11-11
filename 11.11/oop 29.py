class Car:
    def __init__(self):
        self._fuel_level = 0

    @property
    def fuel_level(self):
        return self._fuel_level

    def refuel(self, amount):
        if not (0 < amount < float("inf")):
            raise ValueError("Количество топлива должно быть положительным и конечным")

        self._fuel_level = min(100, self._fuel_level + amount)

    def drive(self, amount):
        if not (0 < amount < float("inf")):
            raise ValueError("Расход топлива должен быть положительным и конечным")

        if amount > self._fuel_level:
            raise ValueError("Недостаточно топлива для поездки")

        self._fuel_level -= amount


car = Car()
car.refuel(80)
car.drive(35)
print(car.fuel_level)  



car.refuel(45)
print(car.fuel_level)  