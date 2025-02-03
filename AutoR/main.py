import pandas
import openpyxl
import json
from datetime import datetime

with open("Trips2.json") as file:
    data = json.load(file)

df = pandas.DataFrame(data)
data_list = df.to_dict('records')

x=0
row = 13
date_col = 1

wb = openpyxl.open("E:/pycharm/Projects/AutoR/recon.xlsx")
sheet = wb["DRIVER'S LOG BOOK"]

for trip in data_list:
    trip_date = (datetime.fromisoformat(data_list[x]['timestamp']).strftime("%d-%m-%Y"))
    print(trip_date)
    print(data_list[x]['fromSite'])
    print(data_list[x]['toSite'])
    print(data_list[x]['startOdo'])
    print(data_list[x]['endOdo'])
    sheet.cell(row=row, column=date_col).value = trip_date

    x += 1
    row += 1




wb.save("E:/pycharm/Projects/AutoR/recon.xlsx")






