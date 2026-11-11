class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")

        self.__price = value


product = Product(9000)
print(product.price)

product.price = -1000  
print(product.price)  

