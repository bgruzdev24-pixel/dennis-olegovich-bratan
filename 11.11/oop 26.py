class Thermostat:
    def __init__(self, target_temperature):
        self.target_temperature = target_temperature

    @property
    def target_temperature(self):
        return self.__target_temperature

    @target_temperature.setter
    def target_temperature(self, value):
        if not (16 <= value <= 30):
            raise ValueError("Температура должна быть от 16 до 30 °C")

        self.__target_temperature = value


thermostat = Thermostat(18)
print(thermostat.target_temperature)  

thermostat.target_temperature = 25
print(thermostat.target_temperature)  

