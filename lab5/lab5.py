class Person:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def __str__(self):
        return f"Full name: {self.full_name}, Age: {self.age}"

class Driver(Person):
    def __init__(self, full_name, age, experience):
        super().__init__(full_name, age)
        self.experience = experience

    def __str__(self):
        return f"Full name: {self.full_name}, age: {self.age}, experience: {self.experience}"

class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer

    def __str__(self):
        return f"Power: {self.power}, manufacturer: {self.manufacturer}"

class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def __start__(self):
        return "We are starting"

    def __stop__(self):
        return "The car stopped"

    def __turn_right__(self):
        return "The car turned right"

    def __turn_left__(self):
        return "The car turned left"

    def __str__(self):
        return f'Car Brand: {self.brand}, Car Class: {self.car_class}, Weight: {self.weight}, ' \
               f'Driver: {self.driver}, Engine: {self.engine}'

class Lorry(Car):
    def __init__(self, brand, car_class, weight, driver, engine, capacity):
        super().__init__(brand, car_class, weight, driver, engine)
        self.carrying = capacity

    def __str__(self):
        return f"{super().__str__()}, capacity: {self.carrying}"

class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver, engine, max_speed):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def __str__(self):
        return f"{super().__str__()}, max speed: {self.max_speed} km/h"


person1 = Person('John doe', 10)
engine1 = Engine(200, 'Toyota')
driver1 = Driver('John doe', 10, "2 year experience")
car1 = Car('Toyota Camry', 'sedan', 1500, driver1, engine1)
print(car1.__start__())
print(car1)

engine2 = Engine(300, 'Volvo')
driver2 = Driver('peter parker', 15, "8 year experience")
lorry = Lorry('Volvo FH', 'lorry', 8000, driver2, engine2, 5000)
print(lorry.__turn_left__())
print(lorry)

engine3 = Engine(400, 'Ferrari')
driver3 = Driver('madina abdulgafar', 5, "1 year experience")
sport_car = SportCar('Ferrari 488', 'sport car', 1500, driver3, engine3, 300)
print(sport_car.__stop__())
print(sport_car)
