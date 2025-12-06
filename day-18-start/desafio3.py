from turtle import Turtle, Screen
from random import choice

fred = Turtle()

# a = (lados-2) * 180 / lados
# triângulo = (3-2) * 180 / 3 = 60
# quadrado = (4-2) * 180 / 4 = 90
# pentágono = (5-2) * 180 / 5 = 108
# hexágono = (6-2) * 180 / 6 = 120 ...


cores = ["blue", "brown", "DeepPink", "cyan", "DarkMagenta", "chartreuse", "DarkOrange", "CadetBlue", "black"]

for num_lados in range(3, 11):
    fred.color(choice(cores))
    angulo = 180 - (((num_lados - 2) * 180) / num_lados)
    for _ in range(num_lados):
        fred.forward(100)
        fred.right(angulo)
    num_lados += 1


tela = Screen()
tela.exitonclick()
