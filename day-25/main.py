# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# # data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
# #
# # data_dict = data.to_dict()
# # # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
#
# # print(sum(temp_list)/len(temp_list))
# #
# # print(data["temp"].mean())
# #
# # print(data['temp'].max())
#
# # print(data[data.day == 'Monday'])
#
# # print(data[data.temp == data['temp'].max()])
#
# # monday = data[data.day == "Monday"]
# # print(monday.condition)
# #
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # monday_temp_F = monday_temp * 9/5 + 32
# # print(monday_temp_F)
#
# # Create a dataFrame from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("data.cvs")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251211.csv")

cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
print(cinnamon, gray, black)

data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black],
}

df = pandas.DataFrame(data_dic)
print(df)
df.to_csv("squirrel_count.csv")