weather = {
    "Monday": 12,
    "Tuesday": 14,
    "Monday": 15,
    "Wednesday": 14,
    "Thursday": 21,
    "Friday": 22,
    "Saturday": 24,
}


def getFar(cel):
    return (cel * 9 / 5) + 32


far_dict = {day: getFar(cel) for (day, cel) in weather.items()}
print(far_dict)
