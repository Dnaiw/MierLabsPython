import pandas as pd

data = pd.read_csv("Resources\\train.csv")

rows_to_fill = ["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]
data[rows_to_fill] = data[rows_to_fill].fillna(data[rows_to_fill].median())

data.to_csv("Resources\\train.csv")


