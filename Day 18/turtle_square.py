from turtle import Screen, Turtle

# turtle_item = Turtle()
# turtle_item.color("red")
# turtle_item.shape("turtle")
# for _ in range(4):
#     turtle_item.forward(100)
#     turtle_item.left(90)
# for _ in range(15):
#     turtle_item.forward(10)
#     turtle_item.penup()
#     turtle_item.forward(10)
#     turtle_item.pendown()

turtle_new_item = Turtle()

num_sides = 3
while num_sides < 10:
    angle = 360 / num_sides
    print(angle)
    for _ in range(num_sides):
        turtle_new_item.forward(100)
        turtle_new_item.right(angle)
    num_sides += 1


screen = Screen()
screen.exitonclick()
