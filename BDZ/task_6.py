import pandas as pd
pd.options.mode.chained_assignment = None
import scipy.spatial.distance

data = pd.read_csv("Resources\\train.csv")

def sex_to_num(sex):
    if sex == "male":
        return 1
    return 0

def conver_age(age):
    return age/100

def conver_parch_and_sib(value):
    return value/10

def convert_class(value):
    return value/3


values_to_analyse =["Sex", "Age", "Parch", "SibSp", "Pclass", "Survived"]
prepared_data = data[values_to_analyse]

prepared_data['Sex'] = prepared_data['Sex'].apply(sex_to_num)
prepared_data['Age'] = prepared_data['Age'].apply(conver_age)
prepared_data['Parch'] = prepared_data['Parch'].apply(conver_parch_and_sib)
prepared_data['SibSp'] = prepared_data['SibSp'].apply(conver_parch_and_sib)
prepared_data['Pclass'] = prepared_data['Pclass'].apply(convert_class)

vectors = prepared_data.values

prepared_data.to_csv("Resources\\train_vectors.csv", index=False)
survived_dict = {}

for index, row in prepared_data.iterrows():
    key = []
    for value in values_to_analyse:
        if value == "Survived":
            continue
        key.append(row[value])

    survived_dict[tuple(key)] = row["Survived"]



def get_distance(vector1, vector2):
    return scipy.spatial.distance.cosine(vector1, vector2)


print(survived_dict)
def predict(vector):
    min = 0.01
    result = 0
    for key in survived_dict:
        if get_distance(list(key), vector) < min:
            min = get_distance(list(key), vector)
            result = survived_dict[key]

    return result



test_data = pd.read_csv("Resources\\test.csv")

test_values_to_analyse =["Sex", "Age", "Parch", "SibSp", "Pclass"]
test_prepared_data = test_data[test_values_to_analyse]

test_prepared_data['Sex'] = test_data['Sex'].apply(sex_to_num)
test_prepared_data['Age'] = test_data['Age'].apply(conver_age)
test_prepared_data['Parch'] = test_data['Parch'].apply(conver_parch_and_sib)
test_prepared_data['SibSp'] = test_data['SibSp'].apply(conver_parch_and_sib)
test_prepared_data['Pclass'] = test_data['Pclass'].apply(convert_class)

test_prepared_data.to_csv("Resources\\test_vectors.csv", index=False)
test_vectors = test_prepared_data.values
predictions = pd.DataFrame()
predictions["PassengerId"] = pd.Series(dtype='Int64')
predictions["Survived"] = pd.Series(dtype='Int64')
test_data["Survived"] = pd.Series(dtype='Int64')

length = len(test_vectors)
for i in range(length):
    print(f"Processing vector {i+1}/{length}")
    prediction = predict(test_vectors[i])
    test_data["Survived"][i] = prediction



test_data.to_csv("Resources\\test_predictions.csv", index=False, columns = ["PassengerId", "Survived"])






