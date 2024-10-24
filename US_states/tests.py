import pandas
# # import statistics
# # import openpyxl
# # import xlrd
#
data = pandas.read_csv("weather_data.csv")
# print(data)
# # temp = data["temp"]
# # temp_list = data["temp"].tolist()
# # avg_temp = sum(temp) / len(temp)
# # ag_temp = statistics.mean(temp)
# # pan_avg = temp.mean()
# #
# #
# print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
#
print(monday)
monday_temp = monday.temp[0]
print(monday_temp)
monday_far = (monday_temp * 9 / 5 + 32)
print(monday_far)
#
# # print(temp)
# # print(temp.max())
# #
# # # print(avg_temp)
# # # print(ag_temp)
# # print(pan_avg)
#
#
# #DC TEST
# # data = pandas.read_excel("Austerville.xls")
# # section = data["Section name"]
# # question = data["Question"]
# # pandas.
# # print(data)
# # print(section)
# # print(question)