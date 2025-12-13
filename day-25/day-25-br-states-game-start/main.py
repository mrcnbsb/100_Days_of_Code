import turtle
import pandas
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=740)
screen.title("Fred, a tartaruga viajante do Brasil. Em qual estado ele está?")
image = "br_map.gif"
screen.addshape(image)
turtle.shape(image)

# dados em dataframe
data = pandas.read_csv("br_estados.csv")
data_dict = data.to_dict()

# dados em lista [[estado, x, y]...]
data_list = []
for i in range(27):
    dados = [data_dict["estado"][i], data_dict["x"][i], data_dict["y"][i] ]
    data_list.append(dados)

# somente estados em lista
br_estados = data["estado"].to_list()
#print(br_estados)
# for num in range(len(br_estados)):
#     br_estados[num] = br_estados[num].title().replace(" ", "_")

estados_encontrados = []

fred = Turtle()
fred.color("green")
fred.shape("turtle")
fred.penup()

while len(estados_encontrados) < 27:
    fred_visita = random.choice(data_list) # [estado, x, y]
    if fred_visita in estados_encontrados:
        continue

    fred_visita[0] = (fred_visita[0]
                      .replace(" ", "_")
                      .replace("á", "a")
                      .replace("í", "i")
                      .replace("ã", "a")
                      .replace("ô", "o")
                      .title()) # Rio_De_Janeiro

    fred.goto(fred_visita[1], fred_visita[2]) # posiciona a tartaruga

    resp_usuario = (screen.textinput(title=f"Fred visitou {len(estados_encontrados)}/27 estados!", prompt="Onde Fred está?")
                    .replace(" ", "_")
                    .replace("á", "a")
                    .replace("í", "i")
                    .replace("ã", "a")
                    .replace("ô", "o")
                    .title()) # São_Paulo

    if resp_usuario == "Sair":
        break

    if resp_usuario == fred_visita[0]:
        estados_encontrados.append(fred_visita)
        fred.write(arg=f"{fred_visita[0]}", align="center", font=("Courier", 14, "normal"))
    else:
        fred.color("red")
        fred.write(arg=f"{fred_visita[0]}", align="center", font=("Courier", 14, "normal"))
        break

fred.goto(0,0)
fred.color("red")
fred.write(arg=f"Fred visitou {len(estados_encontrados)} estados e foi dormir.", align="center", font=("Courier", 24, "normal"))
screen.exitonclick()


