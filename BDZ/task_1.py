import pandas as pd

data = pd.read_csv("Resources\\train.csv")

classes = set(data["Pclass"])
result = []

for p_class in classes:
    result.append({
        "pclass": p_class,
        "survived_women": len(data[(data['Survived'] == 1) & (data['Sex'] == "female") & (data["Pclass"] == p_class)]),
        "death_women": len(data[(data['Survived'] == 0) & (data['Sex'] == "female") & (data["Pclass"] == p_class)]),
        "survived_men": len(data[(data['Survived'] == 1) & (data['Sex'] == "male") & (data["Pclass"] == p_class)]),
        "death_men": len(data[(data['Survived'] == 0) & (data['Sex'] == "male") & (data["Pclass"] == p_class)])
    })

for row in result:
    print("\n")
    print(f"Class: {row['pclass']}")
    print(f"\tSurvived_women: {row['survived_women']}")
    print(f"\tDeath_women: {row['death_women']}")
    print(f"\tSurvived_men: {row['survived_men']}")
    print(f"\tDeath_men: {row['death_men']}")