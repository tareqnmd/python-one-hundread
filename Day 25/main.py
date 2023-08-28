us_states_file_path = "./Python 1-100/Day 25/50_states.csv"
us_states_img_file_path = "./Python 1-100/Day 25/blank_states_img.gif"
us_states_learn_file_path = "./Python 1-100/Day 25/states_to_learn.csv"

import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(us_states_img_file_path)
turtle.shape(us_states_img_file_path)

data = pandas.read_csv(us_states_file_path)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(us_states_learn_file_path)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
