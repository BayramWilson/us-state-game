import pandas

data = pandas.read_csv("50_states.csv")
state_coordinate = data[data.state == "Alabama"]
state_x = state_coordinate.x[0]
state_y = state_coordinate.y[0]
print(state_x)
print(state_y)