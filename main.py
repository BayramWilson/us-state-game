from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
map = Turtle()
map.shape(img)



# print(answer_state)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
print(state_list)

score = 0

data = pandas.read_csv("50_states.csv")
# print(state_list)
correct_guesses=[]
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50", prompt="What´s another state´s name")
    while score < 50:
        state_coordinate = data[data.state == answer_state]
        state_x = state_coordinate.x.item()
        state_y = state_coordinate.y.item()
        if answer_state in state_list:
            correct_guesses.append(answer_state)
            writer = Turtle()
            writer.hideturtle()
            writer.penup()
            writer.goto(state_x, state_y)
            writer.write(answer_state)
            score += 1
            break
        elif answer_state not in state_list:
            print("not such state")


# print(state_list)




screen.mainloop()
