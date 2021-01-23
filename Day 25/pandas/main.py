# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     weather = []
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in column
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # Conversión de grados centígrados a grados Fahrenheit
# print((monday.temp * 9/5) + 32)

# data_dict = {
#     "students": ["Juanito", "Pepito", "Pedrito"],
#     "scores": [76, 81, 62]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_squirrel = data["Primary Fur Color"].to_list()
gray_squirrel = color_squirrel.count("Gray")
cinnamon_squirrel = color_squirrel.count("Cinnamon")
black_squirrel = color_squirrel.count("Black")

count_squirrel = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

new_data = pandas.DataFrame(count_squirrel)
new_data.to_csv("count_color_squirrels.csv")
