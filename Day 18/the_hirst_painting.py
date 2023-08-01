import random
from turtle import Screen, Turtle, colormode

from extract_colors import rgb_colors

colormode(255)
turtle_dot_item = Turtle()
turtle_dot_item.speed("fastest")
turtle_dot_item.penup()
turtle_dot_item.hideturtle()
turtle_dot_item.setheading(225)
turtle_dot_item.forward(300)
turtle_dot_item.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    turtle_dot_item.dot(20, random.choice(rgb_colors))
    turtle_dot_item.forward(50)
    if dot_count % 10 == 0:
        turtle_dot_item.setheading(90)
        turtle_dot_item.forward(50)
        turtle_dot_item.setheading(180)
        turtle_dot_item.forward(500)
        turtle_dot_item.setheading(0)

screen = Screen()
screen.exitonclick()
