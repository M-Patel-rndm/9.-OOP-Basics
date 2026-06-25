class Car:

    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Speed:", self.speed)


car = Car("Toyota", "Camry", 60)

car.accelerate()
car.display()