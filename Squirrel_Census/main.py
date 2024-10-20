import pandas
import openpyxl
color_data = {}

s_data = pandas.read_csv("Squirrel_Data.csv")

gray_count = len(s_data[s_data["Primary Fur Color"] == "Gray"])
black_count = len(s_data[s_data["Primary Fur Color"] == "Black"])
red_count = len(s_data[s_data["Primary Fur Color"] == "Cinnamon"])

fur_dict = {
    "Fur Color" : ["Gray", "Black", "Red"],
    "Count" : [gray_count, black_count, red_count]
}

df_fur = pandas.DataFrame(fur_dict)
df_fur.to_csv("squirrel_count.csv")

#shortest way to count values in column data using pandas
# fur_count = fur_color.value_counts()
# print(fur_count)
# fur_dataframe = pandas.DataFrame(fur_count)
# fur_dataframe.to_csv("squirrel_count.csv")
