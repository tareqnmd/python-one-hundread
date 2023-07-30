# from turtle import Screen, Turtle
#
# turtle = Turtle()
# turtle.forward(100)
# turtle.color("red")
# turtle.shape("turtle")
#
# screen = Screen()
# screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("pokemon_name", ["Tareq", "Sayma"])
table.add_column("pokemon_type", ["Husband", "Wife"])
print(table)
