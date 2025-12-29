# def add(*args): # *args is a tuple
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(3,5, 6, 2, 1, 7, 4, 3))
#
# def calculate(n, **kwargs): # **kwargs is a dict
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key, value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.make)
print(my_car.model)
