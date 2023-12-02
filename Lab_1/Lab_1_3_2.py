import datetime


global dict
dict = {}

def validate_date(date_text):
    try:
        m, d, y = date_text.split(".")
        datetime.date(int(y), int(m), int(d))
    except ValueError:
        return False

    return True


def validate_login(login):
    for letter in login:
        if ord(letter) < ord("A") or ord(letter) > ord("z"):
            return False
    return True


def validate_ip(ip):
    if ip.count(".") != 3:
        return False

    parts = []
    try:
        parts = [int(x) for x in ip.split(".")]
    except:
        return False

    for part in parts:
        if part < 0 or part > 255:
            return False

    return True

def validate_input(string_input):
    if string_input.count(" ") != 2:
        print("s")
        return False

    login, date, ip = string_input.split(" ")

    if not(validate_login(login)) or not(validate_ip(ip)) or not(validate_date(date)):
        return False

    return True

def process_new_log(login, date, ip):
    key = (login, date)

    if not(key in dict):
        dict[key] = {
            "count": 1,
            "ips": [ip]
        }
    elif not(ip in dict[key]["ips"]):
        dict[key]["count"] += 1
        dict[key]["ips"].append(ip)

def get_max_user():
    max = 0
    user = ""
    for key in dict:
        if dict[key]["count"] > max:
            max = dict[key]["count"]
            user = key[0]

    return user

while True:

    try:
        n = int(input("Enter number of logs\n"))
    except:
        print("Error: invalid input")
        continue

    logs = []
    print("Type logs")

    for i in range(n):
        logs.append(input())

    for log in logs:
        if not (validate_input(log)):
            print("Error: invalid input, start again")
            break

        login, date, ip = log.split(" ")
        process_new_log(login, date, ip)

    print(f"Result: {get_max_user()}")
    break
