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
fred.shape("turtle")
fred.pensize(10)
fred.speed(10)



for _ in range(150):
    turn = random.randint(0, 3)
    fred.color(random_color())
    if turn == 0:
        fred.right(90)
    elif turn == 1:
        fred.left(90)
    elif turn == 2:
        fred.back(30)
    elif turn == 3:
        fred.forward(30)






tela = Screen()
tela.exitonclick()