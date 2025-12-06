import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

fred = Turtle()
fred.speed(10)

for _ in range(360//15):
    fred.color(random_color())
    fred.circle(100)
    fred.right(15)



tela = Screen()
tela.exitonclick()