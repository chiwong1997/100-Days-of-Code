# remember to call .venv\Scripts\activate to open pandas

import pandas as pd
import numpy as np
from pathlib import Path
import csv

BASE_DIR = Path(__file__).parent

# using the csv module
with open(BASE_DIR / 'weather_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    temperatures = []
    for row in csv_reader:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

print(temperatures)

# using the pandas module - a python data analyis library
df = pd.read_csv(BASE_DIR / 'weather_data.csv')
# a table is a DataFrame, each column is a Series
print(type(df))
print(type(df['temp']))
print(df["temp"])

# Some methods from the DataFrame class
data_dict = df.to_dict()
print(data_dict)

temperature_list = df['temp'].to_list()
print(temperature_list)
avg_temp = np.mean(temperature_list)
print(avg_temp)

print(df['temp'].mean())
print(df['temp'].max())

# two ways to access each column:
df['temp']
df.temp

# Get data in columns 
print(df['condition'])
print(df.condition) # pandas behind the scenes has turned each column into an attribute of the DataFrame object

# Get data in rows & filtering rows
print(df[df.day == "Monday"])
print(df[df.temp == df.temp.max()])

monday = df[df.day == "Monday"]
print(monday.temp)
print(monday.temp[0])
monday_temp = monday.temp[0] * 9/5 + 32
print(monday_temp)
print(f"The temperature of Monday in F is {monday_temp}")

# Create a DataFrame from scratch

data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data = pd.DataFrame(data_dict)

# save df to new csv file 
data.to_csv(BASE_DIR / "new_data.csv")

