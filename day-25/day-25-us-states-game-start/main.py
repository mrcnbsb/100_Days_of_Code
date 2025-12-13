import turtle
import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

t = Turtle()
t.hideturtle()
t.penup()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another states's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(arg=f"{state_data.state.item()}", align="center", font=("Courier", 14, "normal"))

# states_to_learn.csv
states_to_learn_list = []
for state in all_states:
    if state not in guessed_states:
        states_to_learn_list.append(state)

states_to_learn_dict = {
    "state":[],
    "x":[],
    "y":[],
}
for state in states_to_learn_list:
    state_data = data[data.state == state]
    states_to_learn_dict["state"].append(state_data.state.item())
    states_to_learn_dict["x"].append(state_data.x.item())
    states_to_learn_dict["y"].append(state_data.y.item())

states_to_learn_df = pandas.DataFrame(states_to_learn_dict)

states_to_learn_df.to_csv("states_to_learn.csv")