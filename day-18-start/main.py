# import do módulo turtle com as classes Turtle e Screen
import heroes
from turtle import Turtle, Screen

# instancia um objeto da classe Turtle
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.circle(50)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(200)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(80)
timmy_the_turtle.forward(100)
timmy_the_turtle.penup()
timmy_the_turtle.forward(90)
timmy_the_turtle.pendown()
timmy_the_turtle.right(90)
timmy_the_turtle.forward(150)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(20)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(40)

print(heroes.gen())









# instancia um objeto da classe Screen
screen = Screen()
# o método exit on click congela a janela até que seja clicada
screen.exitonclick()