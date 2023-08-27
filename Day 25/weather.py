weather_file_path = "./Python 1-100/Day 25/weather_data.csv"
student_score_file_path = "./Python 1-100/Day 25/student_score.csv"

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
print(data.to_dict())
print(data[data.day == "Tuesday"])
print(data[data.temp == data.temp.max()])

temp = data["temp"]
print(temp)
temp_list = temp.to_list()
avg_temp = sum(temp_list) / len(temp_list)
print(temp_list, avg_temp)
temp_mean = temp.mean()
temp_max = temp.max()
print(temp_mean, temp_max)

condition = data.condition
print(condition)
monday = data[data.day == "Monday"]
monday_temp = monday.temp
print(monday)
print(monday_temp)


data_dict = {"students": ["aaa", "bbb", "ccc"], "scores": [40, 44, 38]}
data = pandas.DataFrame(data_dict)
data.to_csv(student_score_file_path)
