# with open("./weather_data.csv") as weather_d:
#     data = weather_d.readlines()

# import csv
#
# with open("./weather_data.csv") as weather_d:
#     data = csv.reader(weather_d)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
temp = data["temp"]
print(data)
print(temp)