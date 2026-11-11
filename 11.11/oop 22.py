class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже -273.15 °C")

        self.__celsius = value


temperature = Temperature(20)
print(temperature.celsius)  # 20

temperature.celsius = -273.15
print(temperature.celsius)  # -273.15
