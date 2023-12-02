import pandas as pd

data = pd.read_csv("Resources\\train.csv")

median = data[(data["Sex"] == "male")]["Age"].median()

sexes = ["male", "female"]

for sex in sexes:
    active_data = data[(data["Sex"] == sex)]
    print(f"\nSex: {sex}")
    for column in active_data:
        type = active_data.dtypes[column]
        if type != 'int64' and type != 'float64':
            continue

        print(f"\tColumn: {column} Median: {active_data[column].describe()}")

