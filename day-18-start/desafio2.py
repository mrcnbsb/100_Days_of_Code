from turtle import Turtle, Screen

fred = Turtle()

def fazer_linha_tracejada(turtle, repeticoes):
    for _ in range(repeticoes):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

fazer_linha_tracejada(fred, 15)




tela = Screen()
tela.exitonclick()