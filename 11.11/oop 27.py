class Wallet:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    def add_money(self, amount):
        if not (0 < amount < float("inf")):
            raise ValueError("Сумма должна быть положительной и конечной")

        self.__balance += amount

    def spend_money(self, amount):
        if not (0 < amount < float("inf")):
            raise ValueError("Сумма должна быть положительной и конечной")

        if amount > self.__balance:
            raise ValueError("В кошельке недостаточно денег")

        self.__balance -= amount


wallet = Wallet()
wallet.add_money(8000)
wallet.spend_money(3500)
print(wallet.balance)

