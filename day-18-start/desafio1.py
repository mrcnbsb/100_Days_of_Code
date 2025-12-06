from turtle import Turtle, Screen

# Fred, the turtle
fred = Turtle()
fred.shape("turtle")
fred.color("blue")

def make_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


make_square(fred)


tela = Screen()
tela.exitonclick()
