# файл players.csv был сгенерирован с помощью ChatGPT
import csv


def get_athletes_from_file(file_path):
    result = []
    with open(file_path, "r", encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        flag = 0
        for row in csv_reader:
            if flag == 0:
                flag += 1
                continue

            result.append({
                "athlete": row[0],
                "victories": row[1],
                "scores": row[2]
            })

    return result

def write_results_to_file(file_path, results):
    with open(file_path, "w", encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter=',', lineterminator = '\n')

        csv_writer.writerow(["Спортсмен", "Место"])

        for result in results:
            csv_writer.writerow([result["athlete"], result["place"]])



def process_players(players):
    print(players)
    sorted_players = players
    sorted_players.sort(key=lambda x: (x["victories"], int(x["scores"])), reverse = True)
    print(sorted_players)
    result = []
    place = 1
    for i in range(len(sorted_players)):
        if i == 0:
            result.append({
                "place": place,
                "athlete": sorted_players[i]["athlete"]
            })
            continue

        if sorted_players[i]["scores"] == sorted_players[i-1]["scores"] and sorted_players[i]["victories"] == sorted_players[i-1]["victories"]:
            result.append({
                "place": place,
                "athlete": sorted_players[i]["athlete"]
            })
            continue

        place += 1
        result.append({
            "place": place,
            "athlete": sorted_players[i]["athlete"]
        })
    return result

players = get_athletes_from_file("players.csv")
results = process_players(players)
write_results_to_file("results.csv",results)
