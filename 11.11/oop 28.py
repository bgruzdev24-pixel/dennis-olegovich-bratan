class Email:
    def __init__(self, address):
        self.__address = None
        self.address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if "@" not in value:
            print("Ошибка: адрес должен содержать символ @")
            return

        self.__address = value


email = Email("danil@example.com")
print(email.address)  

email.address = "danil.example.com" 
print(email.address)  