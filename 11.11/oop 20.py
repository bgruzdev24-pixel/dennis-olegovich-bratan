class User:
    def __init__(self, password):
        self.__password = password

    def check_password(self, password):
        return self.__password == password


user = User("qwerty123")

print(user.check_password("qwerty123"))  # True
print(user.check_password("wrong"))      # False