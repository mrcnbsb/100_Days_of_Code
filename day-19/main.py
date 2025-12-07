from turtle import Turtle, Screen

fred = Turtle()
screen = Screen()

def move_forward():
    fred.forward(50)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()