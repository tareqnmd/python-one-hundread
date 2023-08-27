squirrel_data_path = "./Python 1-100/Day 25/central_park_squirrel_data.csv"
squirrel_count_file_path = "./Python 1-100/Day 25/squirrel_count.csv"

import pandas

data = pandas.read_csv(squirrel_data_path)

fur_color_gray_count = len(data[data["Primary Fur Color"] == "Gray"])
fur_color_cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
fur_color_black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [fur_color_gray_count, fur_color_cinnamon_count, fur_color_black_count],
}
count_data = pandas.DataFrame(data_dict)
count_data.to_csv(squirrel_count_file_path)
