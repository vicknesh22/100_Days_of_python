# Reading csv file

# with open("weather_data.csv", mode="r") as data:
#     weather_data = data.readlines()
#     updated_weather = []
#     for i in weather_data:
#         y = i.strip('\n')
#         updated_weather.append(y)
#     print(updated_weather)

# # Reading the csv using csv library
# import csv
#
# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# using pandas for more complex table analysis

#import pandas

#data = pandas.read_csv("weather_data.csv")

# print(data["temp"])

# temp_list = data["temp"].to_list()
#
# # print(temp_list)
# #
# # average_temp = sum(temp_list) / len(temp_list)
# # print(average_temp)
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data.day)

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
#
# monday_temp = int(monday.temp)
# monday_far = monday_temp * 9/5 + 32
# print(monday_far)

import pandas
data = pandas.read_csv("squirrel_data.csv")

grey_sqr_count = len(data[data["Primary Fur Color"] == "Gray"])
black_sqr_count = len(data[data["Primary Fur Color"] == "Black"])
cin_sqr_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dic = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_sqr_count, black_sqr_count, cin_sqr_count]
}

df = pandas.DataFrame(data_dic)
print(df)
df.to_csv("squirrel_count.csv")









