weather_file_path = "./Python 1-100/Day 25/weather_data.csv"

# with open(weather_file_path) as weather_file:
#     data = weather_file.readlines()
#     print(data)

# import csv

# with open(weather_file_path) as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         temperature = row[1]
#         if temperature != "temp":
#             temperatures.append(int(temperature))
#     print(temperatures)


import pandas

data = pandas.read_csv(weather_file_path)
print(data)
print(data["temp"])
