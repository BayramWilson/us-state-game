from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
map = Turtle()
map.shape(img)


data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()


data = pandas.read_csv("50_states.csv")
# print(state_list)
correct_guesses = []
missing_states = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50", prompt="What´s another state´s name")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        for missed in data.state:
            if missed not in correct_guesses:
                missing_states.append(missed)
        df = pandas.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break
    if answer_state in state_list:
        state_coordinate = data[data.state == answer_state]
        state_x = state_coordinate.x.item()
        state_y = state_coordinate.y.item()
        correct_guesses.append(answer_state)
        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(state_x, state_y)
        writer.write(answer_state)
