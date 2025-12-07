import turtle
from turtle import Turtle, Screen

fred = Turtle()
fred.speed(10)
screen = Screen()

def move_forward():
    fred.forward(10)

def move_backwards():
    fred.backward(10)

def clear_drawing():
    turtle.resetscreen()

def move_left():
    new_heading = fred.heading() + 10
    fred.setheading(new_heading)

def move_right():
    new_heading = fred.heading() - 10
    fred.setheading(new_heading)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.exitonclick()