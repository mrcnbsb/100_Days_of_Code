from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=700, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()


fred = Turtle()
fred.shape("turtle")
fred.color("purple")

bob = Turtle()
bob.shape("turtle")
bob.color("red")

yug = Turtle()
yug.shape("turtle")
yug.color("yellow")

zed = Turtle()
zed.shape("turtle")
zed.color("blue")

liu = Turtle()
liu.shape("turtle")
liu.color("green")

lia = Turtle(shape="turtle")
lia.color("pink")

fred.penup()
fred.goto(x=-330, y=150)
bob.penup()
bob.goto(x=-330, y=90)
yug.penup()
yug.goto(x=-330, y=30)
zed.penup()
zed.goto(x=-330, y=-30)
liu.penup()
liu.goto(x=-330, y=-90)
lia.penup()
lia.goto(x=-330, y=-150)

win = ""

is_race_on = True

while is_race_on:
    fred.forward(random.randint(0,10))
    if fred.xcor() > 335:
        is_race_on = False
        print("Purple win!")
        win = "purple"

    bob.forward(random.randint(0,10))
    if bob.xcor() > 335:
        is_race_on = False
        print("Red win!")
        win = "red"

    yug.forward(random.randint(0,10))
    if yug.xcor() > 335:
        is_race_on = False
        print("Yellow win!")
        win = "yellow"

    zed.forward(random.randint(0,10))
    if zed.xcor() > 335:
        is_race_on = False
        print("Blue win!")
        win = "blue"

    liu.forward(random.randint(0,10))
    if liu.xcor() > 335:
        is_race_on = False
        print("Green win!")
        win = "green"

    lia.forward(random.randint(0,10))
    if lia.xcor() > 335:
        is_race_on = False
        print("Pink win!")
        win = "pink"


if user_bet == win:
    print("You win. Congratulations!!")
else:
    print("Bad choice!")

screen.exitonclick()

