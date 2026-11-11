class Age:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not (0 <= value <= 120):
            raise ValueError("Возраст должен быть от 0 до 120")

        self.__age = value


person = Age(98)
print(person.age)

person.age = 19
print(person.age)
