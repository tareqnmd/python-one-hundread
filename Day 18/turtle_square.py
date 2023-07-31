import random
from turtle import Screen, Turtle, colormode

colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]
# directions = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]
directions = [0, 90, 180, 270, 360]


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

# turtle_new_item = Turtle()
# num_sides = 3
# while num_sides < 10:
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         turtle_new_item.color(random.choice(colors))
#         turtle_new_item.forward(100)
#         turtle_new_item.right(angle)
#     num_sides += 1


colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


turtle_rand_item = Turtle()
turtle_rand_item.pensize(10)
turtle_rand_item.speed("fastest")
for _ in range(200):
    turtle_rand_item.color(random_color())
    turtle_rand_item.forward(30)
    turtle_rand_item.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
