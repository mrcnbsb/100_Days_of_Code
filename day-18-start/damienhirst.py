import colorgram
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
fred = Turtle()
fred.speed(10)

# extract 10 color from an image
color_list = colorgram.extract('damienhirst.jpg', 30)
colors = []

for color in color_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color = (r, g, b)
    colors.append(rgb_color)

fred.setheading(225)
fred.up()
fred.hideturtle()
fred.forward(250)
fred.setheading(0)
fred.down()

number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    fred.dot(20, random.choice(colors))
    fred.penup()
    fred.forward(50)
    fred.pendown()
    if dot_count % 10 == 0:
        fred.penup()
        fred.setheading(90)
        fred.forward(50)
        fred.setheading(180)
        fred.forward(500)
        fred.setheading(0)




screen = Screen()
screen.exitonclick()


