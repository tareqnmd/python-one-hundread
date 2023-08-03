# from turtle import Screen, Turtle

# turtle_item = Turtle()
# screen = Screen()

# turtle_item.speed("fastest")


# def move_forwards():
#     turtle_item.forward(25)


# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()

from turtle import Screen, Turtle

turtle_item = Turtle()
screen = Screen()

turtle_item.speed("fastest")


def move_forwards():
    turtle_item.forward(20)


def move_backwards():
    turtle_item.backward(20)


def turn_left():
    turtle_item.setheading(turtle_item.heading() + 20)


def turn_right():
    turtle_item.setheading(turtle_item.heading() - 20)


def clear():
    turtle_item.clear()
    turtle_item.penup()
    turtle_item.home()
    turtle_item.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
