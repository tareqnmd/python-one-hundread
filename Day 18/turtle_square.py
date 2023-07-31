from turtle import Screen, Turtle

turtle_item = Turtle()
turtle_item.color("red")
turtle_item.shape("turtle")

turtle_item.forward(100)
turtle_item.left(90)
turtle_item.forward(100)
turtle_item.left(90)
turtle_item.forward(100)
turtle_item.left(90)
turtle_item.forward(100)
turtle_item.right(90)

for _ in range(15):
    turtle_item.forward(10)
    turtle_item.penup()
    turtle_item.forward(10)
    turtle_item.pendown()

screen = Screen()
screen.exitonclick()
