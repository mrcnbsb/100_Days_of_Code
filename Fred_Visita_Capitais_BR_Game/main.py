import turtle
import pandas
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=740)
screen.title("Fred, a tartaruga viajante do Brasil. Em qual capital ele está?")
image = "br_map.gif"
screen.addshape(image)
turtle.shape(image)

# dados em dataframe
data = pandas.read_csv("br_estados.csv")
data_dict = data.to_dict()

# dados em lista [[estado, capital, x, y]...]
data_list = []
for i in range(27):
    dados = [data_dict["estado"][i],data_dict["capital"][i], data_dict["x"][i], data_dict["y"][i] ]
    data_list.append(dados)

# somente estados em lista
br_estados = data["estado"].to_list()

capitais_visitadas = []

fred = Turtle()
fred.color("green")
fred.shape("turtle")
fred.penup()

while len(capitais_visitadas) < 27:
    fred_visita = random.choice(data_list) # [estado, x, y]
    if fred_visita in capitais_visitadas:
        continue

    fred_visita[1] = (fred_visita[1]
                      .replace(" ", "_")
                      .replace("á", "a")
                      .replace("í", "i")
                      .replace("ã", "a")
                      .replace("ô", "o")
                      .title()) # Rio_De_Janeiro

    fred.goto(fred_visita[2], fred_visita[3]) # posiciona a tartaruga

    resp_usuario = (screen.textinput(title=f"Fred visitou {len(capitais_visitadas)}/27 estados!", prompt="Onde Fred está?")
                    .replace(" ", "_")
                    .replace("á", "a")
                    .replace("í", "i")
                    .replace("ã", "a")
                    .replace("ô", "o")
                    .title()) # São_Paulo

    if resp_usuario == "Sair":
        break

    if resp_usuario == fred_visita[1]:
        capitais_visitadas.append(fred_visita)
        fred.write(arg=f"{fred_visita[1]}", align="center", font=("Courier", 14, "normal"))
    else:
        fred.color("red")
        fred.write(arg=f"{fred_visita[1]}", align="center", font=("Courier", 14, "normal"))
        break

fred.goto(0,0)
fred.color("red")
fred.write(arg=f"Fred visitou {len(capitais_visitadas)} estados e foi dormir.", align="center", font=("Courier", 24, "normal"))
screen.exitonclick()


