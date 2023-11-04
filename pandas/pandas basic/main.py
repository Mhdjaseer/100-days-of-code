import pandas

data=pandas.read_csv("pandas/weather_data.csv")

data_dict=data.to_dict()
# print(data_dict)

# temp_list=data["temp"].to_list()

# print(data["temp"].max())

# print(data["condition"])

# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

#  create a dataframe from scratch

data_dict={
    "students":["Amy","james","angla"],
    "scores":[75,65,46]
}
data_d=pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")