import pandas

data=pandas.read_csv("pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231102.csv")

grey_squirerels_count= len(data[data["Primary Fur Color"]=="Gray"])
red_squirerels_count= len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirerels_count= len(data[data["Primary Fur Color"]=="Black"])

print(grey_squirerels_count)
print(red_squirerels_count)
print(black_squirerels_count)


data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirerels_count,red_squirerels_count,black_squirerels_count]
}

df=pandas.DataFrame(data_dict)
df.to_csv("pandas/squirrel_count.csv")