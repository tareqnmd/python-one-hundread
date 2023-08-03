from turtle import Screen, Turtle

turtle_item = Turtle()
screen = Screen()

turtle_item.speed("fastest")


def move_forwards():
    turtle_item.forward(25)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
