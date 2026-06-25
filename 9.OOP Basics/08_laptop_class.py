class Laptop:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


laptop = Laptop("HP", 60000)

laptop.apply_discount(10)

laptop.display()