import pandas as pd

data = pd.read_csv("Resources\\train.csv")

data[['FirstName', 'LastName']] = data['Name'].str.split(',', n=1, expand=True)


firstNames = data['FirstName'].value_counts()[:10].index.tolist()

lastNames = data['LastName'].value_counts()[:10].index.tolist()

print("First names:")
for name in firstNames:
    print("\t" + name)

print("Last names:")
for name in lastNames:
    print("\t" + name)

