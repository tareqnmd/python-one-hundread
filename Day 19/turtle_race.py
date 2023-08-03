import random
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

user_prediction = screen.textinput(
    title="Make your prediction",
    prompt="Which turtle will win the race ? Enter the turtle color: ",
)

if user_prediction:
    is_race_on = True

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -75
all_turtles = []
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=-230, y=y_position)
    all_turtles.append(turtle)
    y_position += 30

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_prediction:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
