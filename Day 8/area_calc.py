import math

height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
coverage = 5


def calcArea():
    return math.ceil((height * width) / coverage)


result = f"you need {calcArea} cans of paint"

print(result)
