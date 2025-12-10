from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.starting_position = []
        self.create_starting_position()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_starting_position(self):
        x = 300
        y = 225
        for _ in range(1, 20):
            self.starting_position.append((x, y))
            y -= 25

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.goto(choice(self.starting_position))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


    def go_to_start(self):
        for car in self.all_cars:
            car.goto(choice(self.starting_position))