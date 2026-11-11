class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._validate_amount(amount)
        self._balance += amount

    def withdraw(self, amount):
        self._validate_amount(amount)

        if amount > self._balance:
            raise ValueError("Недостаточно средств на счёте")

        self._balance -= amount

    def get_balance(self):
        return self._balance

    @staticmethod
    def _validate_amount(amount):
        if type(amount) not in (int, float):
            raise TypeError("Сумма должна быть числом")

        if not (0 < amount < float("inf")):
            raise ValueError("Сумма должна быть положительной и конечной")


account = BankAccount()
account.deposit(5000)
account.withdraw(1500)
print(account.get_balance())