import pandas as pd

data = pd.read_csv("Resources\\train.csv")

ports = set(data["Embarked"])
print(ports)
result = []

for port in ports:

    if str(port) == 'nan':
        continue

    result.append({
        "embarked": port,
        "surviving_percent": len(data[(data['Survived'] == 1) & (data["Embarked"] == port)])/len(data[(data["Embarked"] == port)]),
    })

for row in result:
    print("\n")
    print(f"Port: {row['embarked']}")
    print(f"\tsurviving_percent: {row['surviving_percent']}")
