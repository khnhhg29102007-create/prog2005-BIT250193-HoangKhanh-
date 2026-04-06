class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


book1 = Book("Book 1", 30000)

print("Giá sách:", book1.get_price())